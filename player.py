"""The player: simple drawn character with movement, jumping and gravity."""

import pygame

from settings import (
    EYE_COLOR,
    GRAVITY,
    JUMP_SPEED,
    LEVEL_WIDTH,
    MAX_FALL_SPEED,
    MOVE_SPEED,
    PLAYER_BELLY_COLOR,
    PLAYER_COLOR,
    PUPIL_COLOR,
)


class Player:
    """Rect-based character. Collisions are resolved against platform Rects."""

    WIDTH = 28
    HEIGHT = 40

    def __init__(self, pos):
        self.image = self._make_image()
        self.rect = self.image.get_rect(topleft=pos)
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.on_ground = False

    def _make_image(self):
        image = pygame.Surface((self.WIDTH, self.HEIGHT))
        image.fill(PLAYER_COLOR)
        # Belly patch
        image.fill(PLAYER_BELLY_COLOR, (4, 18, self.WIDTH - 8, self.HEIGHT - 18))
        # Eyes
        image.fill(EYE_COLOR, (5, 6, 7, 7))
        image.fill(EYE_COLOR, (16, 6, 7, 7))
        image.fill(PUPIL_COLOR, (8, 8, 3, 4))
        image.fill(PUPIL_COLOR, (19, 8, 3, 4))
        return image

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        # Horizontal input
        self.vel_x = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -MOVE_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = MOVE_SPEED

        # Jump (uses on_ground state from the previous frame)
        if (
            (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w])
            and self.on_ground
        ):
            self.vel_y = -JUMP_SPEED
            self.on_ground = False

        # Gravity
        self.vel_y = min(self.vel_y + GRAVITY, MAX_FALL_SPEED)

        # Move horizontally, then resolve collisions
        self.rect.x += int(self.vel_x)
        self._collide(platforms, horizontal=True)

        # Move vertically, then resolve collisions
        self.rect.y += int(self.vel_y)
        self.on_ground = False
        self._collide(platforms, horizontal=False)

        # Keep the player inside the level
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LEVEL_WIDTH:
            self.rect.right = LEVEL_WIDTH

    def _collide(self, platforms, horizontal):
        for plat in platforms:
            if not self.rect.colliderect(plat):
                continue
            if horizontal:
                if self.vel_x > 0:
                    self.rect.right = plat.left
                elif self.vel_x < 0:
                    self.rect.left = plat.right
                self.vel_x = 0
            else:
                if self.vel_y > 0:
                    self.rect.bottom = plat.top
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = plat.bottom
                self.vel_y = 0
