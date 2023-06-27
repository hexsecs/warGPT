**README.md**

# Card War Game

This is a simple implementation of the card game "War" with some slight modifications for a single player competing against the computer. The game is terminal-based and also plots the winning probabilities for the player and the computer after each round.

## Getting Started

Clone the repository and navigate to the project directory.

## How to Run

To run the game, use the following command in your terminal:

```bash
python war_game.py
```

This will initiate the game. The game will display the cards dealt and the results of each round. You can follow along in the terminal as the game unfolds.

## How to Play

The game automatically handles the playing, so all you need to do is initiate it.

The rules of the game are simple: a deck of cards is divided equally between the player and the computer. Each player turns up a card at the same time and the player with the higher card takes both cards, placing them on the bottom of their stack. If the cards are the same rank, it is "War". Each player puts an additional face down and one card face up. The player with the higher card takes all six cards, and so on until the tie is broken.

The game ends when one player has won all the cards.

## Game Visualization

The application uses matplotlib to plot the winning probability for the player and the computer after each round. You can see the probability chart by running the application.

## Requirements

Python 3.x, matplotlib

## Dependencies

The dependencies for the application can be installed via pip using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Enjoy the game!

---
**requirements.txt**

```bash
matplotlib
```

Note: The above version for matplotlib is just an example. You should replace it with the version that you have tested your code with. 

The application only uses the Python Standard Library apart from matplotlib, so no other dependencies are required.
