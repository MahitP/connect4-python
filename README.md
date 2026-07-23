# Connect4 Python

A complete, interactive Connect 4 game built with Python. This project demonstrates programmatic game logic, 2D grid state management, and event-driven UI updates using `cmu_graphics`.

## Features

- **Interactive UI:** A fully playable graphical interface with smooth piece-dropping animations and hover states.
- **State Management:** Maintains a 6x7 grid representation of the board to track player moves.
- **Win Detection Algorithms:** Calculates win conditions (vertical, horizontal, diagonal) programmatically after every move.
- **Game Loops & State Resets:** Handles title screens, game-over states, and resets cleanly without restarting the application.

## Technologies Used

- **Python 3.11+**
- **cmu_graphics:** Used for rendering 2D shapes, handling mouse events, and managing the application step loop.
- **uv / pyproject.toml:** Modern Python dependency management.

## Installation

This project manages dependencies using `uv` or standard `pip`.

1. Clone the repository and navigate to the project directory:
   ```bash
   cd connect4-python
   ```

2. Install dependencies via pip:
   ```bash
   pip install -r requirements.txt
   ```
   *Alternatively, if using `uv`:*
   ```bash
   uv sync
   ```

## Usage

Run the game script from your terminal:

```bash
python connect4.py
```
*If using `uv`: `uv run connect4.py`*

## Technical Details

The core challenge in this project was managing the separation between the underlying board data structure and the visual representation. 

The game board is represented internally as a 2D array (`holes`), where each index maps to a specific column and row. When a player drops a piece:
1. The column index is calculated from the mouse's X-coordinate.
2. The logic determines the lowest available row in that column.
3. An animation state (`fallingPiece`) updates the UI over multiple frames until it reaches the target row.
4. Once landed, a sequence of four algorithmic checks (horizontal, vertical, diagonal-up, diagonal-down) evaluates the board to determine if a win condition has been met.

## Author

Mahit
