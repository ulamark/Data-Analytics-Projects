# Chess Capture Checker

**Overview**

The Chess Capture Checker is a Python program designed to simulate the movement and capturing capabilities of chess pieces, specifically the pawn and rook. The program allows users to set up a chessboard, select white pieces (pawn or rook), and add up to 16 black pieces. It then checks which black pieces can be captured by the selected white piece based on the rules of chess.

**Features**

Interactive Gameplay: Users can interactively choose their pieces and coordinates.
Chess Rules Compliance: The program adheres to the rules for capturing with pawns and rooks.
Visual Board Representation: The chessboard is displayed in the terminal, providing a clear visual layout of the game state.
Input Validation: The program validates user input to ensure that only valid figures and coordinates are accepted.

**Requirements**

Python 3.x
A terminal or command-line interface

**Running the Program**

To run the Chess Capture Checker, use the following command in your terminal: python chess_project.py .

The code is originally written on cs50dev virtual environment.

**How to Play**

Upon running the program, you will see an empty chessboard and the main rules for gameplay.
You will be prompted to select a white piece (either a pawn or a rook) and its position on the board (e.g., "pawn a4").
Next, you can add black pieces one at a time by specifying the figure and position (e.g., "knight c5"). Type done when you finish adding black pieces.
The program will then display the black pieces that can be captured by your selected white piece.

**Code Structure**

chess_projcet.py: Contains the main logic for the game, including functions for drawing the board, checking valid moves, and capturing pieces.

Functionality includes:
Drawing the chessboard.
Validating positions and user input.
Logic for pawn and rook movements.
Handling user interactions.
