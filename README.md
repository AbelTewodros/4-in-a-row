Overview

I worked on a project implementing a Connect Four game where two AI bots play against each other using the minimax algorithm. Player "X" starts with a search depth of 5, making it more strategic, while player "O" begins with a depth of 1, resulting in simpler gameplay. You can adjust the depths of each AI by modifying the parameters in the script.py file—line 7 for player "X" and line 15 for player "O."

Features

Minimax Algorithm: Implements a decision-making algorithm for both AI players to select optimal moves.
Alpha-Beta Pruning: Enhances the minimax algorithm for efficiency by eliminating branches in the game tree.
Custom Evaluation Functions: Allows the implementation of different evaluation strategies, including a random evaluation and a user-defined evaluation function.
Two AI Gameplay: Demonstrates AI competition by letting both AI players take turns until a winner is determined or the game ends in a tie.

Getting Started

Prerequisites
Python 3.x installed on your machine.


Adjusting AI Difficulty:

Modify AI Depths: To change the difficulty of the AI players, edit the values in the script.py file:
Set the depth for player "X" on line 7.
Set the depth for player "O" on line 15.

Game Logic:

Board Representation:
The game board is represented as a 2D list, with columns indexed from 1 to 7 and rows from 0 to 5.

Game Functions:
print_board(board): Displays the current state of the board.
select_space(board, column, player): Allows a player to place their token in a specified column.
has_won(board, symbol): Checks if the specified player has won the game.
minimax(input_board, is_maximizing, depth, alpha, beta, eval_function): Implements the minimax algorithm to evaluate possible moves.

Evaluation Functions:
Random Evaluation: A simple evaluation function that returns a random score.
Custom Evaluation: Implemented in my_evaluate_board(), this function evaluates the board based on the number of two-token streaks for both players.
Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features!

