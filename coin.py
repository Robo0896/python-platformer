"""Collectible coin with a gentle bobbing animation."""

import math
import random

import pygame

from settings import COIN_COLOR, COIN_SHINE_COLOR


class Coin(pygame.sprite.Sprite):
    RADIUS = 9

    def __init__(self, center):
        super().__init__()
        size = self.RADIUS * 2 + 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, COIN_COLOR, (size // 2, size // 2), self.RADIUS)
        pygame.draw.circle(
            self.image, COIN_SHINE_COLOR, (size // 2 - 3, size // 2 - 3), 3
        )
        self.rect = self.image.get_rect(center=center)
        self.base_y = center[1]
        self.t = random.uniform(0, math.tau)

    def update(self):
        self.t += 0.08
        self.rect.centery = self.base_y + int(math.sin(self.t) * 3)
