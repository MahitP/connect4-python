# Connect4 Python

An interactive 2D Connect 4 game built in Python. The project focuses on programmatic state management, 2D array matrix traversal algorithms, and dynamic UI rendering using the `cmu_graphics` library.

---

## 🚀 Overview

The application provides a complete, playable Connect 4 interface. It internally tracks the game state on a 6x7 grid, handles alternating player turns, animates pieces falling into place, and programmatically evaluates the board matrix for win conditions after every move.

---

## ✨ Features

- Interactive graphical interface with dynamic piece-dropping animations and column hover states.
- Internal 2D array state management that dictates UI rendering.
- Matrix-based win detection algorithms covering horizontal, vertical, and both diagonal axes.
- Comprehensive game loop handling title screens, player switching, draw conditions, and state resets.

---

## 🛠️ Technical Implementation

The core architectural approach separates the visual representation from the underlying data structure. 

The game board is stored as a 6x7 2D array. When a user clicks:
1. The X-coordinate of the mouse is mathematically converted into a column index.
2. The logic scans that column from the bottom row up to find the lowest available empty slot.
3. An animation state is triggered. The UI loop (`onStep`) updates the Y-coordinate of a dropping piece over multiple frames until it reaches the calculated target row, ensuring the main thread is not blocked by a `while` loop.
4. Once the piece lands, the matrix is updated, and a sequence of four algorithmic checks traverses the 2D array to determine if a win condition has been met.

---

## 🧠 Design Decisions & Challenges

- **Event-Driven Animations:** A major challenge was animating the dropping pieces without freezing the application. Standard `time.sleep()` loops block the UI thread. Instead, an event-driven approach was used. The falling logic relies on an `onStep` timer function that increments a `fallingRow` variable incrementally across frames, creating smooth animation while keeping the application responsive to user input.
- **Matrix Traversal:** Win detection required careful index boundary management. Rather than hardcoding checks for every cell, the logic uses bounded `for` loops (e.g., `range(rows - 3)`) to prevent `IndexError` exceptions while efficiently scanning the grid for 4-in-a-row matches.

---

## 📁 Project Structure

```
├── connect4.py          # Main application file containing state management and rendering logic
├── requirements.txt     # Project dependencies
└── pyproject.toml       # Project metadata
```

---

## ▶️ Running the Project

**Requirements:** Python 3.11+

1. Clone the repository and navigate to the project directory:
   ```bash
   cd connect4-python
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python3 connect4.py
   ```

---

## 🔮 Future Improvements

- Abstracting the game state matrix and win-detection algorithms into a dedicated `Board` class for better object-oriented design.
- Implementing a minimax algorithm with alpha-beta pruning for a single-player AI mode.

---

## ⭐ Technical Highlights

- **Matrix Algorithms:** Efficiently traversing a 2D array to detect multi-directional geometric patterns (win conditions).
- **State Management:** Maintaining a strict separation between internal application state (the 2D grid array) and the visual UI state (falling piece coordinates).
- **Event-Driven Architecture:** Utilizing non-blocking timer loops to handle physics-like animations in a single-threaded environment.

---

## Author

Mahit Pulavarthi — [github.com/MahitP](https://github.com/MahitP)

