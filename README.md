# Pygame Platformer

A small 2D platformer written in Python and [Pygame](https://www.pygame.org/).
Everything is drawn with simple shapes — no external image assets required.

Collect coins, stomp enemies from above, avoid falling into pits, and reach the
green flag at the far right of the level to win.

## Gameplay

- Move left and right with the arrow keys (or **A**/**D**).
- Jump with **Space**, the up arrow, or **W**.
- Land on top of an enemy to stomp it (+25 points); touching it any other way
  costs you a life.
- Coins are worth 100 points each. Falling into a pit ends the run.
- Touch the flag at the end of the level to win.

### Keys

| Key                  | Action                          |
| -------------------- | ------------------------------- |
| Left / A             | Move left                       |
| Right / D            | Move right                      |
| Space / Up / W       | Jump                            |
| R                    | Restart the level at any time   |
| Q or Esc             | Quit                            |
| Close window         | Quit                            |

## Project layout

| File          | Purpose                                                  |
| ------------- | -------------------------------------------------------- |
| `main.py`     | Entry point — starts the game loop.                      |
| `game.py`     | Game loop, input, collisions, camera, HUD, overlays.     |
| `level.py`    | Level data: platforms, coins, enemies, flag, scenery.    |
| `player.py`   | Player movement, jumping, gravity, platform collisions.  |
| `enemy.py`    | Patrolling enemies.                                      |
| `coin.py`     | Collectible coins with a bobbing animation.              |
| `flag.py`     | Goal flag sprite.                                        |
| `settings.py` | Window size, physics constants, colors, scoring values.  |

## Running on Arch Linux

### Option 1: Install Pygame from the official repos (recommended)

```bash
sudo pacman -S python-pygame
```

Then run the game:

```bash
cd /home/Robo/Projects/platformer
python main.py
```

(On Arch, `python` is Python 3. `python3 main.py` works too.)

### Option 2: Use a virtual environment

Arch marks the system Python as externally managed (PEP 668), so if you prefer
pip-installed packages, use a venv:

```bash
sudo pacman -S python-pip        # if pip isn't installed yet
cd /home/Robo/Projects/platformer
python -m venv .venv
source .venv/bin/activate
pip install pygame
python main.py
```

Leave the venv afterwards with `deactivate`.

### Troubleshooting

- `ModuleNotFoundError: No module named 'pygame'` — Pygame isn't installed;
  use one of the options above.
- No audio — the game runs fine without it; Pygame simply skips audio output.

## Tweaking

All gameplay tuning lives in `settings.py` (gravity, jump strength, move
speed, scoring, colors) and the level layout lives in `level.py`. Edit those
files and restart the game to see your changes.
