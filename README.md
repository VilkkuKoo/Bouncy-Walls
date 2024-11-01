# Bouncy-Walls

Bouncy Walls - An Open Source Game

## Description

Bouncy Walls is a simple game developed using Python and Pygame. The player controls a red square that can move left, right, and jump. The objective of the game is to collect blue balls that appear randomly on the screen. Each time a ball is collected, the player's score increases by one, and a new ball appears at a different location. The game ends if the player touches the top or bottom of the screen.

## Features

- Simple and intuitive controls
- Randomly spawning collectible balls
- Score tracking
- Main menu with "Play" and "Quit" options
- Game title and subtitle displayed on the main menu

## Controls

- Left Arrow: Move left
- Right Arrow: Move right
- Up Arrow: Jump

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install Pygame using pip:
   ```sh
   pip install pygame
   ```
## How to Play

1. Run the game script:

2. On the main menu, click "Play" to start the game.
3. Use the arrow keys to move the red square and collect the blue balls.
4. The game will return to the main menu if the player touches the top or bottom of the screen.

## Code Overview

main.py

The main game script contains the following key components:

- Constants: Define screen dimensions, colors, gravity, jump strength, and other game settings.
- Main Menu: Displays the game title, subtitle, and buttons for "Play" and "Quit".
- Game Loop: Handles player movement, gravity, collision detection, and rendering.
- Score Tracking: Increments the score each time a ball is collected and displays the current score on the screen.
- Contributing
- Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.