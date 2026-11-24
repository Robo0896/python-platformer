"""Level layout: platforms, coins, enemies, the goal flag and scenery.

All coordinates are in level pixels. The level is wider than the screen
(see settings.LEVEL_WIDTH); the game uses a camera to follow the player.

Enemy tuples are (spawn_x, spawn_y, patrol_min_x, patrol_max_x).
Coin tuples are the coin's center position.
"""

import pygame

from settings import LEVEL_WIDTH, PLAYER_START

# (x, y, width, height)
PLATFORMS = [
    # Ground segments (gaps in between are deadly pits)
    (0, 500, 640, 40),
    (720, 500, 380, 40),
    (1180, 500, 520, 40),
    (1780, 500, 620, 40),
    # Floating platforms
    (260, 400, 140, 20),
    (470, 310, 130, 20),
    (680, 230, 130, 20),
    (900, 390, 120, 20),
    (1080, 300, 120, 20),
    (1300, 230, 140, 20),
    (1560, 400, 130, 20),
    (1750, 300, 140, 20),
    (1980, 380, 130, 20),
]

COINS = [
    (330, 370),
    (535, 280),
    (745, 200),
    (960, 360),
    (1120, 270),
    (1370, 200),
    (1625, 370),
    (1820, 270),
    (2045, 350),
    # Coins hovering over the gaps
    (680, 445),
    (1140, 445),
    (1740, 445),
]

ENEMIES = [
    (250, 474, 140, 620),
    (900, 474, 760, 1060),
    (1400, 474, 1240, 1660),
    (2050, 474, 1840, 2360),
    (1330, 204, 1310, 1430),
]

FLAG_POS = (2280, 404)

# Decorative cloud positions (x, y), drawn with parallax
CLOUDS = [
    (120, 90),
    (480, 150),
    (860, 70),
    (1260, 130),
    (1700, 100),
    (2150, 160),
]

PLAYER_SPAWN = PLAYER_START
LEVEL_RECT = pygame.Rect(0, 0, LEVEL_WIDTH, 1000)
