"""Central configuration: window size, physics constants and colors."""

# --- Window ---------------------------------------------------------------
TITLE = "Pygame Platformer"
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
FPS = 60

# --- Physics --------------------------------------------------------------
GRAVITY = 0.45
MAX_FALL_SPEED = 12.0
MOVE_SPEED = 5.0
JUMP_SPEED = 11.5
STOMP_BOUNCE = 7.0      # upward velocity after stomping an enemy
STOMP_TOLERANCE = 14    # max overlap (px) that still counts as a stomp

# --- Scoring --------------------------------------------------------------
COIN_SCORE = 100
STOMP_SCORE = 25

# --- Level ----------------------------------------------------------------
LEVEL_WIDTH = 2400
PLAYER_START = (40, 420)

# --- Colors ---------------------------------------------------------------
SKY_COLOR = (135, 206, 235)
CLOUD_COLOR = (255, 255, 255)
GROUND_COLOR = (121, 85, 61)
GRASS_COLOR = (96, 175, 78)
PLAYER_COLOR = (36, 96, 220)
PLAYER_BELLY_COLOR = (90, 150, 240)
ENEMY_COLOR = (200, 62, 62)
ENEMY_DARK_COLOR = (150, 40, 40)
EYE_COLOR = (255, 255, 255)
PUPIL_COLOR = (20, 20, 20)
COIN_COLOR = (255, 200, 40)
COIN_SHINE_COLOR = (255, 235, 140)
POLE_COLOR = (120, 120, 130)
FLAG_COLOR = (70, 190, 90)
TEXT_COLOR = (25, 25, 30)
