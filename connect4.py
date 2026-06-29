
ROWS = 6
COLS = 7
PLAYER_1_PIECE = 'X'
PLAYER_2_PIECE = 'O'
EMPTY = ' '

def create_board():
    """Creates a 6x7 grid filled with empty spaces."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the board to the terminal in a readable format."""
    print("\n")
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('-' * (COLS * 4 + 1))
    # Print column numbers for easy reference
    print('  ' + '   '.join(str(i) for i in range(COLS)))
    print("\n")

def is_valid_location(board, col):
    """Checks if a piece can be dropped into the chosen column."""
    # If the top row (index 0) is empty, the column isn't full
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    """Finds the lowest available row in a specific column."""
    # Loop from the bottom row (ROWS-1) up to the top row (0)
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r

def drop_piece(board, row, col, piece):
    """Places the player's piece on the board."""
    board[row][col] = piece

def check_win(board, piece):
    """Checks all horizontal, vertical, and diagonal lines for 4 in a row."""
    # Check horizontal locations
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals (/)
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals (\)
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def play_game():
    """Main game loop."""
    board = create_board()
    game_over = False
    turn = 0
    pieces = [PLAYER_1_PIECE, PLAYER_2_PIECE]

    print("Welcome to Connect Four!")
    
    while not game_over:
        print_board(board)
        
        # Determine current player
        current_player = turn % 2
        current_piece = pieces[current_player]
        
        # Input loop for validity
        while True:
            try:
                col = int(input(f"Player {current_player + 1} ({current_piece}), choose a column (0-{COLS - 1}): "))
                
                if 0 <= col < COLS:
                    if is_valid_location(board, col):
                        break
                    else:
                        print("That column is full! Choose another one.")
                else:
                    print(f"Invalid column. Please choose a number between 0 and {COLS - 1}.")
            except ValueError:
                print("Invalid input. Please type a number.")

        # Process the move
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, current_piece)

        # Check for a win
        if check_win(board, current_piece):
            print_board(board)
            print(f"*** PLAYER {current_player + 1} ({current_piece}) WINS! ***\n")
            game_over = True
        
        # Check for a tie
        turn += 1
        if turn == ROWS * COLS and not game_over:
            print_board(board)
            print("*** IT'S A TIE! ***\n")
            game_over = True

if __name__ == "__main__":
    play_game()
    