# The application prompts the user to enter a square board size between minimum of 4 and maximum of 16.
# The application prints out a random board where each cell is either empty or contains a red or black checker.

# checkers.py

from numpy import

def build_board(size):
    """
    Generate a board of the given size with random values of 'Empty', 'Red', or 'Black'.
    """
    if size < 4 or size > 16:
        raise ValueError("Board size must be between 4 and 16.")

    # Define the possible values
    values = ['Empty', 'Red', 'Black']

    # Create a random board
    board = random.choice(values, (size, size))

    return board


def get_count(board, color):
    """
    Count occurrences of 'Empty', 'Red', or 'Black' in the board.
    """
    if color not in ['Empty', 'Red', 'Black']:
        raise ValueError("Color must be 'Empty', 'Red', or 'Black'.")

    return (board == color).sum()


if __name__ == "__main__":
    print("This file is not intended to be run as a main program.")
