# Tic Tac Toe Game

## Description

A python based 2-player Tic Tac Toe game. It takes input of the two players. The two players are named as X and O and will enter alternating moves in attempt to win the game.

## Prerequisites

Ensure you have Python installed on your system. Download the latest version from [python.org](https://www.python.org/).

## Features

- The game is played on a 3x3 grid.
- Players take turns to place their symbol (X or O) on the board.
- The game checks for a winner after each move.
- It declares the winner or a tie (Cats game) accordingly.

## How to Play

1. Run the `tic_tac_toe.py` script.
2. Players take turns entering their moves by specifying the position on the board (0-8).
3. The game will display the updated board after each move.
4. The game declares the winner or a tie when the game ends.

## Winning Conditions

The game checks for winning conditions in the following ways:

- Horizontally
- Vertically
- Diagonally

## Design Principles and Integration with Observer Pattern

the Observer design pattern have applied to Tic Tact Toe Game that separating the subject(game logic) and observer(display logic). Also consider the Single Responsibility Principle (SRP), where each class has a single responsibility and the Open/Closed Principle (OCP) by allowing for easy extension. It allows add more observers or change the display logic to do so without modifying the core game logic.
As the result, it enhances maintainability and extensibility by promoting a modular and loosely-coupled architecture.

## License

This project is licensed under the [MIT License](LICENSE).
