# main.py
import checkers game
def game():
    """
    Main game function that prompts user for board size and prints the board and counts.
    """
    try:
        size = int(input("Enter the size of the board (between 4 and 16): "))

        if size < 4 or size > 16:
            raise ValueError("Board size must be between 4 and 16.")

        # Build the board
        board = checkers.build_board(size)

        # Print the board
        print("Board:")
        print(board)

        # Count occurrences
        empty_count = checkers.get_count(board, 'Empty')
        red_count = checkers.get_count(board, 'Red')
        black_count = checkers.get_count(board, 'Black')

        # Print counts
        print(f"Empty cells: {empty_count}")
        print(f"Red cells: {red_count}")
        print(f"Black cells: {black_count}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    game()
