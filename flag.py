"""Goal flag: touching it wins the level."""

import pygame

from settings import FLAG_COLOR, POLE_COLOR


class GoalFlag:
    WIDTH = 26
    HEIGHT = 96

    def __init__(self, topleft):
        self.image = self._make_image()
        self.rect = self.image.get_rect(topleft=topleft)

    def _make_image(self):
        image = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        # Pole
        image.fill(POLE_COLOR, (2, 0, 5, self.HEIGHT))
        # Golden ball on top
        pygame.draw.circle(image, (255, 200, 40), (4, 4), 4)
        # Flag cloth
        pygame.draw.polygon(
            image,
            FLAG_COLOR,
            [(7, 6), (self.WIDTH - 1, 16), (7, 26)],
        )
        return image
