from typing import Dict, Tuple, List, Optional

def draw_board(board_state: Dict[Tuple[str, str], Optional[Tuple[str, str]]]) -> None:
    """
    Draws the current state of the chessboard using chess symbols.

    Args:
        board_state (dict): A dictionary where keys are tuples representing the
                            positions of pieces on the board (e.g., ('a', '1')),
                            and values are tuples containing the piece's color
                            ('W' for white, 'B' for black) and type (e.g., 'pawn',
                            'rook').

    The function prints the chessboard in an 8x8 grid format with row and column
    labels. Pieces are displayed using Unicode chess symbols, and the colors of
    the pieces are swapped (white pieces in black and black pieces in white)
    due to the terminal display.
    """

    board = [["." for _ in range(8)] for _ in range(8)]

    # Original white pieces are now displayed in black, and original black pieces are displayed in white
    # due to the black chessboard in the Python terminal
    piece_symbols = {
        "W": {"pawn": "♟", "rook": "♜"},
        "B": {
            "king": "♔",
            "queen": "♕",
            "rook": "♖",
            "knight": "♘",
            "bishop": "♗",
            "pawn": "♙",
        },
    }

    # Place pieces on the board based on their positions in board_state
    for (col, row), piece in board_state.items():
        if piece is not None:
            col_index = ord(col) - ord("a")  # 'a' -> 0, 'b' -> 1, ..., 'h' -> 7
            row_index = 8 - int(row)  # '8' -> 0, '7' -> 1, ..., '1' -> 7

            piece_color, piece_type = piece

            # Use the appropriate chess symbol from the dictionary
            board[row_index][col_index] = piece_symbols[piece_color][piece_type]

    # Print the board
    print("  a b c d e f g h")
    for i in range(8):
        print(8 - i, " ".join(board[i]))


def is_valid_position(position: str) -> bool:
    """
    Checks if a given chessboard position is valid.

    Args:
        position (str): A string representing a position on the chessboard,
                        consisting of a column ('a' to 'h') and a row ('1' to '8').

    Returns:
        bool: True if the position is valid (within 'a-h' for columns and '1-8' for rows),
              False otherwise.

    The function ensures the input is exactly 2 characters long and checks if the
    column is between 'a' and 'h' and the row is between '1' and '8'.
    """
    if len(position) != 2:  # Position should be 2 characters (e.g., a4)
        return False
    col, row = (position[0], position[1])
    return "a" <= col <= "h" and "1" <= row <= "8"


def choose_white_figure(board_state:
                        Dict[Tuple[str, str], Optional[Tuple[str, str]]]) -> Tuple[str, str, str]:
    """
    Allows the user to choose a white piece (pawn or rook) and place it on the chessboard.

    Args:
        board_state (dict): A dictionary representing the current state of the chessboard.
                            Keys are tuples representing positions (e.g., ('a', '4')), and
                            values are tuples containing the color ('W' for white) and type
                            of piece (e.g., 'pawn', 'rook').

    Returns:
        tuple: A tuple containing the chosen piece type (either 'pawn' or 'rook'),
               the column (e.g., 'a'), and the row (e.g., '4') where the piece is placed.

    The function prompts the user to enter a white piece ('pawn' or 'rook') along with
    valid coordinates (e.g., 'a4'). It validates the input and places the chosen piece
    on the board at the specified coordinates. If the input is invalid, it asks the
    user to try again until valid input is provided.
    """
    while True:
        user_input = (
            input("Choose white figure (pawn or rook) and write its coordinates (e.g., pawn a4): ")
            .strip().lower())

        try:
            figure, position = user_input.split()

            if figure not in ["pawn", "rook"]:
                print("Invalid figure! Please choose either 'pawn' or 'rook'.")
                continue

            if not is_valid_position(position):
                print("Invalid coordinates! Please use a letter from a-h and a number from 1-8.")
                continue

            col, row = position[0], position[1]

            # If both checks pass, place the white piece on the board
            board_state[(col, row)] = ("W", figure)
            print(f"White {figure} placed at {col}{row}.")
            return figure, col, row

        # If the input is not in the correct format, display an error message
        except ValueError:
            print("Invalid input! Please enter the figure and coordinates in the format: 'pawn a4'.")


def choose_black_figures(board_state: Dict[Tuple[str, str], Optional[Tuple[str, str]]],
                         valid_black_figures: Dict[str, int]) -> List[Tuple[str, str, str]]:
    """
    Allows the user to choose and place up to 16 black pieces on the chessboard.

    Args:
        board_state (dict): A dictionary representing the current state of the chessboard.
                            Keys are tuples representing positions (e.g., ('a', '4')), and
                            values are tuples containing the color ('B' for black) and type
                            of piece (e.g., 'pawn', 'rook').

        valid_black_figures (dict): A dictionary where keys are valid black piece types
                                    (e.g., 'pawn', 'rook'), and values are the maximum
                                    number of each type of piece that can be placed on
                                    the board.

    Returns:
        list: A list of tuples, where each tuple contains the chosen black piece type,
              the column, and the row (e.g., ('rook', 'h', '5')) for each placed piece.

    The function prompts the user to input a black piece and its coordinates. It validates
    both the piece and the position, ensuring that the chosen position is empty and that
    the user does not exceed the allowed number of pieces. The user can place up to 16
    black pieces. Typing 'done' finishes the input process, provided at least one piece
    has been placed.
    """
    # An empty list where the chosen black pieces will be stored
    black_pieces = []
    while True:
        user_input = (
            input("Choose black figure and write its coordinates (or 'done' to finish): ").strip().lower())

        # If the user enters "done", check if they've added at least one black piece and stop
        if user_input == "done":
            if len(black_pieces) >= 1:
                print("Black pieces input complete.")
                break
            else:
                print("You must add at least one black figure before typing 'done'.")
                continue

        try:
            figure, position = user_input.split()

            if figure not in valid_black_figures:
                print(f"Invalid figure! Choose from: {', '.join(valid_black_figures.keys())}.")
                continue

            if not is_valid_position(position):
                print("Invalid coordinates! Please use a letter from a-h and a number from 1-8.")
                continue

            col, row = position[0], position[1]

            # Check if the position is empty
            if board_state[(col, row)] is not None:
                print(f"Position {col}{row} is already occupied. Choose another coordinate.")
                continue

            # Check if the user hasn't exceeded the allowed number of this figure type
            if valid_black_figures[figure] == 0:
                print(f"No more {figure}s available. Choose another figure.")
                continue

            # Place the black piece on the board
            board_state[(col, row)] = ("B", figure)
            black_pieces.append((figure, col, row))

            # Decrease the count of the available figure
            valid_black_figures[figure] -= 1
            print(f"Black {figure} placed at {col}{row}.")

            draw_board(board_state)

        except ValueError:
            print("Invalid input! Please enter the figure and coordinates in the format: 'rook h5'.")

    return black_pieces  # Return the list of added black pieces


# A dictionary representing the available black chess pieces and their quantities
valid_black_figures_list = {
    "king": 1,
    "queen": 1,
    "rook": 2,
    "knight": 2,
    "bishop": 2,
    "pawn": 8,
}


def update_board_state(board_state: Dict[Tuple[str, str], Optional[Tuple[str, str]]],
                       figure: str, col: str, row: str, color: str) -> Dict[Tuple[str, str], Optional[Tuple[str, str]]]:
    """
    Updates the chessboard state by placing a new piece at the given position.

    Args:
        board_state (dict): A dictionary representing the current state of the chessboard.
                            Keys are tuples representing positions (e.g., ('a', '4')),
                            and values are tuples containing the color ('W' for white,
                            'B' for black) and the piece type (e.g., 'pawn', 'rook').

        figure (str): The type of the chess piece to place (e.g., 'pawn', 'rook').
        col (str): The column where the piece will be placed (from 'a' to 'h').
        row (str): The row where the piece will be placed (from '1' to '8').
        color (str): The color of the piece, either 'W' (white) or 'B' (black).

    Returns:
        dict: The updated chessboard state with the new piece placed at the specified
              position.

    The function modifies the board state by adding or updating the piece at the given
    position and returns the updated dictionary.
    """
    board_state[(col, row)] = (color, figure)
    return board_state


def pawn_can_win(board_state: Dict[Tuple[str, str], Optional[Tuple[str, str]]],
                 pawn_col: str, pawn_row: str) -> List[Tuple[Tuple[str, str], Tuple[str, str]]]:
    """
    Checks if the white pawn can capture any black pieces by moving diagonally forward.

    Args:
        board_state (dict): A dictionary representing the current state of the chessboard.
                            Keys are tuples representing positions (e.g., ('a', '4')),
                            and values are tuples containing the color ('W' for white,
                            'B' for black) and the piece type (e.g., 'pawn', 'rook').
        pawn_col (str): The column where the white pawn is located (from 'a' to 'h').
        pawn_row (str): The row where the white pawn is located (from '1' to '8').

    Returns:
        list: A list of tuples representing the black pieces that the white pawn can capture.
              Each tuple contains the position of the black piece and the piece itself,
              e.g., [(('d', '3'), ('B', 'rook'))].

    The function checks the two diagonal positions (left and right forward) from the pawn's
    current location. If a black piece is located in either of these positions, it is added
    to the list of capturable pieces.
    """
    captured_pieces = []  # List to store black pieces that can be captured

    # Convert the column and row to numbers for easier arithmetic operations with figure positions
    col_index = ord(pawn_col)  # Convert column letter to ASCII value (e.g., 'a' -> 97)
    row_index = int(pawn_row)  # Convert row number to integer

    # Define the two potential diagonal positions where the pawn can capture
    potential_positions = [
        # Diagonally left forward (e.g., from e4 to d3)
        # The chr() function converts the ASCII value back into a letter (a chessboard column)
        (chr(col_index - 1), str(row_index + 1)),
        (chr(col_index + 1), str(row_index + 1)),  # Diagonally right forward (e.g., from e4 to f3)
    ]

    # Check both diagonal positions for a black piece
    for pos in potential_positions:
        if (
            pos in board_state
            and board_state[pos] is not None
            and board_state[pos][0] == "B"
        ):  # Check if there's a black piece
            captured_pieces.append(
                (pos, board_state[pos])
            )

    # Return list of black pieces that can be captured
    return captured_pieces


def rook_can_win(board_state: Dict[Tuple[str, str], Optional[Tuple[str, str]]],
                 rook_col: str, rook_row: str) -> List[Tuple[Tuple[str, str], Tuple[str, str]]]:
    """
    Checks if the white rook can capture any black pieces by moving horizontally or vertically.

    Args:
        board_state (dict): A dictionary representing the current state of the chessboard.
                            Keys are tuples representing positions (e.g., ('a', '4')),
                            and values are tuples containing the color ('W' for white,
                            'B' for black) and the piece type (e.g., 'pawn', 'rook').
        rook_col (str): The column where the white rook is located (from 'a' to 'h').
        rook_row (str): The row where the white rook is located (from '1' to '8').

    Returns:
        list: A list of tuples representing the black pieces that the white rook can capture.
              Each tuple contains the position of the black piece and the piece itself,
              e.g., [(('d', '5'), ('B', 'bishop'))].

    The function checks all possible straight-line movements of the rook (both horizontal
    and vertical directions) and looks for black pieces that the rook can capture.
    The rook can move in a straight line in any direction until it encounters a piece
    or goes out of bounds.
    """
    captured_pieces = []  # List to store black pieces that can be captured

    col_index = ord(rook_col)  # Convert column letter to ASCII value (e.g., 'd' -> 100)
    row_index = int(rook_row)  # Convert row number to integer (e.g., '5' -> 5)

    # Directions the rook can move: (dx, dy) for (horizontal, vertical) moves
    directions = [
        (1, 0),  # Right (horizontal)
        (-1, 0),  # Left (horizontal)
        (0, 1),  # Up (vertical)
        (0, -1),  # Down (vertical)
    ]

    # Check all four possible directions
    for dx, dy in directions:
        step = 1  # Rook can move multiple steps in a straight line

        while True:
            # Calculate the new position the rook would move to
            new_col = chr(col_index + dx * step)
            new_row = str(row_index + dy * step)

            if new_col < "a" or new_col > "h" or new_row < "1" or new_row > "8":
                break

            # Check if the new position is occupied
            if (new_col, new_row) in board_state:
                piece = board_state[(new_col, new_row)]

                if piece is not None:
                    # If it's a black piece, the rook can capture it
                    if piece[0] == "B":
                        captured_pieces.append(((new_col, new_row), piece))
                    # Stop after encountering any piece (can't move past it)
                    break

            # If no piece is in the new position, the rook can keep moving
            step += 1

    # Return the list of black pieces that can be captured
    return captured_pieces


def main():
    """
    Main function to run the Chess Capture Checker program.

    This function initializes an empty chessboard, prompts the user to select
    a white figure (either a pawn or rook), allows the user to place black
    pieces on the board, and checks which black pieces can be captured by
    the chosen white figure. The results are then printed to the console.

    Steps executed in this function:
    1. Displays an empty chessboard.
    2. Prompts the user to choose a white figure (pawn or rook).
    3. Prompts the user to choose black figures (up to 16).
    4. Checks which black pieces can be captured by the selected white piece.
    5. Prints the results, showing the black pieces that can be captured.
    """
    # Show an empty chessboard
    board_state = {(col, str(row)): None for col in "abcdefgh" for row in range(1, 9)}

    print("")
    print("Chess Capture Checker")
    draw_board(board_state)
    print("Main rules: ")
    print("1) Choose 1 white figure either pawn or rook.")
    print("2) Choose from 1 to 16 black figures.")
    print("3) After you choose black figures, write 'done'.")
    print("4) The program will return those black figures, that can be captured by the white figure.")

    # Step 1: Choose a white piece
    white_piece, white_col, white_row = choose_white_figure(board_state)
    draw_board(board_state)

    # Step 2: Choose black pieces
    valid_black_figures = valid_black_figures_list
    black_pieces = choose_black_figures(board_state, valid_black_figures)
    draw_board(board_state)

    # Step 3: Check which black pieces can be captured
    if white_piece == "pawn":
        capturable = pawn_can_win(board_state, white_col, white_row)
    elif white_piece == "rook":
        capturable = rook_can_win(board_state, white_col, white_row)

    # Step 4: Print the result
    if capturable:
        print("The white piece can capture the following black pieces:")
        for pos, piece in capturable:
            col, row = pos
            print(f"{piece[1]} at {col}{row}")
    else:
        print("The white piece cannot capture any black pieces.")


# Run the main function to start the program
if __name__ == "__main__":
    main()