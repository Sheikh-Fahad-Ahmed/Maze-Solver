# 🧩 Maze Solver

A visual maze generator and solver implemented in Python using the `tkinter` library. This project creates a random maze using recursive backtracking, then solves it using depth-first search, all while animating each step.

## ✨ Features

- Random maze generation using recursive backtracking
- Visual maze drawing and solving with animation
- Customizable maze size and cell dimensions
- Unit tests to verify core functionality
- Interactive window using `tkinter`

## 📁 Project Structure

```bash
maze_solver/
├── maze.py        # Maze generation and solving logic
├── cell.py        # Cell representation and wall logic
├── window.py      # Graphics window using tkinter
├── point.py       # Basic 2D point class
├── line.py        # Line class for drawing
├── main.py        # Entry point to run the app (you can create this)
└── tests.py       # Unit tests for maze components
