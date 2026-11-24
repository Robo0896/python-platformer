"""Game class: main loop, input, collisions, camera, HUD and overlays."""

import pygame

from coin import Coin
from enemy import Enemy
from flag import GoalFlag
from level import CLOUDS, COINS, ENEMIES, FLAG_POS, PLATFORMS
from player import Player
from settings import (
    CLOUD_COLOR,
    COIN_SCORE,
    GRASS_COLOR,
    GROUND_COLOR,
    LEVEL_WIDTH,
    PLAYER_START,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SKY_COLOR,
    STOMP_BOUNCE,
    STOMP_SCORE,
    STOMP_TOLERANCE,
    TEXT_COLOR,
    TITLE,
    FPS,
)

PLAYING, DEAD, WON = "playing", "dead", "won"


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 28)
        self.big_font = pygame.font.Font(None, 72)
        self.running = True
        self.state = PLAYING
        self.reset()

    def reset(self):
        """(Re)build the level from scratch. Used on start and on restart."""
        self.platforms = [pygame.Rect(r) for r in PLATFORMS]
        self.player = Player(PLAYER_START)
        self.enemies = pygame.sprite.Group(
            Enemy((x, y), min_x, max_x) for x, y, min_x, max_x in ENEMIES
        )
        self.coins = pygame.sprite.Group(Coin(pos) for pos in COINS)
        self.flag = GoalFlag(FLAG_POS)
        self.total_coins = len(self.coins.sprites())
        self.score = 0
        self.lives = 3
        self.camera_x = 0.0
        self.state = PLAYING

    # ------------------------------------------------------------------ loop
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    # ---------------------------------------------------------------- events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()
                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    self.running = False

    # --------------------------------------------------------------- update
    def update(self):
        if self.state != PLAYING:
            return

        self.player.update(self.platforms)
        self.enemies.update(self.platforms)
        self.coins.update()
        self.update_camera()

        # Coins
        collected = pygame.sprite.spritecollide(self.player, self.coins, True)
        self.score += COIN_SCORE * len(collected)

        # Enemies: stomp from above, otherwise player dies
        for enemy in self.enemies.sprites():
            if not self.player.rect.colliderect(enemy.rect):
                continue
            stomping = (
                self.player.vel_y > 0
                and self.player.rect.bottom - enemy.rect.top <= STOMP_TOLERANCE
            )
            if stomping:
                enemy.kill()
                self.player.vel_y = -STOMP_BOUNCE
                self.score += STOMP_SCORE
            else:
                self.lives -= 1
                if self.lives <= 0:
                    self.state = DEAD
                else:
                    self.player = Player(PLAYER_START)
                return

        # Goal flag
        if self.player.rect.colliderect(self.flag.rect):
            self.state = WON
            return

        # Fell into a pit
        if self.player.rect.top > SCREEN_HEIGHT + 60:
            self.lives -= 1
            if self.lives <= 0:
                self.state = DEAD
            else:
                self.player = Player(PLAYER_START)
                self.camera_x = 0

    def update_camera(self):
        target = self.player.rect.centerx - SCREEN_WIDTH // 2
        max_x = LEVEL_WIDTH - SCREEN_WIDTH
        self.camera_x = max(0, min(target, max_x))

    # ----------------------------------------------------------------- draw
    def draw(self):
        self.screen.fill(SKY_COLOR)
        self.draw_clouds()
        self.draw_platforms()
        self.screen.blit(self.flag.image, self.flag.rect.move(-self.camera_x, 0))
        for coin in self.coins.sprites():
            self.screen.blit(coin.image, coin.rect.move(-self.camera_x, 0))
        for enemy in self.enemies.sprites():
            self.screen.blit(enemy.image, enemy.rect.move(-self.camera_x, 0))
        self.screen.blit(self.player.image, self.player.rect.move(-self.camera_x, 0))
        self.draw_hud()
        if self.state != PLAYING:
            self.draw_overlay()
        pygame.display.flip()

    def draw_clouds(self):
        parallax = 0.5
        for x, y in CLOUDS:
            sx = x - self.camera_x * parallax
            for dx, dy, r in ((0, 0, 22), (24, 4, 16), (-24, 6, 14)):
                pygame.draw.circle(self.screen, CLOUD_COLOR, (sx + dx, y + dy), r)

    def draw_platforms(self):
        for plat in self.platforms:
            rect = plat.move(-self.camera_x, 0)
            pygame.draw.rect(self.screen, GROUND_COLOR, rect)
            pygame.draw.rect(self.screen, GRASS_COLOR, (rect.x, rect.y, rect.w, 5))

    def draw_hud(self):
        score_text = self.font.render(f"Score: {self.score}", True, TEXT_COLOR)
        coins_left = self.total_coins - len(self.coins)
        coins_text = self.font.render(
            f"Coins: {coins_left}/{self.total_coins}", True, TEXT_COLOR
        )
        self.screen.blit(score_text, (12, 10))
        self.screen.blit(coins_text, (SCREEN_WIDTH - coins_text.get_width() - 12, 10))
        lives_text = self.font.render(f"Lives: {self.lives}", True, TEXT_COLOR)
        self.screen.blit(lives_text, (12,40))

    def draw_overlay(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        if self.state == WON:
            title, color = "YOU WIN!", (255, 215, 60)
        else:
            title, color = "YOU DIED", (235, 80, 80)

        title_text = self.big_font.render(title, True, color)
        title_rect = title_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
        )
        self.screen.blit(title_text, title_rect)

        score_text = self.font.render(f"Final score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        )
        self.screen.blit(score_text, score_rect)

        hint_text = self.font.render(
            "Press R to restart  |  Q to quit", True, (255, 255, 255)
        )
        hint_rect = hint_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        )
        self.screen.blit(hint_text, hint_rect)
