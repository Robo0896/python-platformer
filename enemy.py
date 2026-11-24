"""Patrolling enemy. Walks between fixed bounds; touching it hurts (unless stomped)."""

import pygame

from settings import (
    ENEMY_COLOR,
    ENEMY_DARK_COLOR,
    EYE_COLOR,
    GRAVITY,
    MAX_FALL_SPEED,
    PUPIL_COLOR,
)


class Enemy(pygame.sprite.Sprite):
    WIDTH = 34
    HEIGHT = 26

    def __init__(self, pos, min_x, max_x, speed=1.6):
        super().__init__()
        self.image = self._make_image()
        self.rect = self.image.get_rect(topleft=pos)
        self.min_x = min_x
        self.max_x = max_x
        self.speed = speed
        self.dir_x = 1
        self.vel_y = 0.0

    def _make_image(self):
        image = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        pygame.draw.ellipse(image, ENEMY_COLOR, (0, 0, self.WIDTH, self.HEIGHT))
        image.fill(ENEMY_DARK_COLOR, (2, self.HEIGHT - 8, self.WIDTH - 4, 6))
        image.fill(EYE_COLOR, (7, 6, 7, 7))
        image.fill(EYE_COLOR, (20, 6, 7, 7))
        image.fill(PUPIL_COLOR, (10, 8, 3, 4))
        image.fill(PUPIL_COLOR, (23, 8, 3, 4))
        return image

    def update(self, platforms):
        # Patrol horizontally between bounds
        self.rect.x += int(self.speed * self.dir_x)
        if self.rect.left <= self.min_x:
            self.rect.left = self.min_x
            self.dir_x = 1
        elif self.rect.right >= self.max_x:
            self.rect.right = self.max_x
            self.dir_x = -1

        # Gravity so enemies stay on their platform
        self.vel_y = min(self.vel_y + GRAVITY, MAX_FALL_SPEED)
        self.rect.y += int(self.vel_y)
        for plat in platforms:
            if self.rect.colliderect(plat) and self.vel_y > 0:
                self.rect.bottom = plat.top
                self.vel_y = 0.0
