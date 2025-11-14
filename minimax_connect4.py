ROWS = 6
COLS = 7

def create_board():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for r in board:
        print('|' + ''.join(' .' if c==0 else (' X' if c==1 else ' O') for c in r) + ' |')
    print(' ' + ' '.join(str(i) for i in range(COLS)))

def is_valid_move(board, col):
    return 0 <= col < COLS and board[0][col] == 0

def make_move(board, col, player):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == 0:
            board[r][col] = player
            return r
    return None

def undo_move(board, row, col):
    board[row][col] = 0

def is_board_full(board):
    return all(board[0][c] != 0 for c in range(COLS))

def check_winner(board):
    # returns 1 if AI wins, -1 if human wins, 0 otherwise
    for r in range(ROWS):
        for c in range(COLS-3):
            s = board[r][c] + board[r][c+1] + board[r][c+2] + board[r][c+3]
            if s == 4: return 1
            if s == -4: return -1
    for c in range(COLS):
        for r in range(ROWS-3):
            s = board[r][c] + board[r+1][c] + board[r+2][c] + board[r+3][c]
            if s == 4: return 1
            if s == -4: return -1
    for r in range(ROWS-3):
        for c in range(COLS-3):
            s = board[r][c] + board[r+1][c+1] + board[r+2][c+2] + board[r+3][c+3]
            if s == 4: return 1
            if s == -4: return -1
    for r in range(3, ROWS):
        for c in range(COLS-3):
            s = board[r][c] + board[r-1][c+1] + board[r-2][c+2] + board[r-3][c+3]
            if s == 4: return 1
            if s == -4: return -1
    return 0

def evaluate_board(board):
    winner = check_winner(board)
    if winner == 1: return 10
    if winner == -1: return -10
    return 0

def minimax(board, depth, is_maximizing, max_depth):
    score = evaluate_board(board)
    if score == 10: return score - depth
    if score == -10: return score + depth
    if is_board_full(board) or depth == max_depth: return 0

    if is_maximizing:
        best = -10**9
        for col in range(COLS):
            if is_valid_move(board, col):
                row = make_move(board, col, 1)
                val = minimax(board, depth+1, False, max_depth)
                undo_move(board, row, col)
                if val > best: best = val
        return best
    else:
        best = 10**9
        for col in range(COLS):
            if is_valid_move(board, col):
                row = make_move(board, col, -1)
                val = minimax(board, depth+1, True, max_depth)
                undo_move(board, row, col)
                if val < best: best = val
        return best

def find_best_move(board, max_depth=4):
    best_val = -10**9
    best_col = None
    for col in range(COLS):
        if is_valid_move(board, col):
            row = make_move(board, col, 1)
            val = minimax(board, 0, False, max_depth)
            undo_move(board, row, col)
            if val > best_val:
                best_val = val
                best_col = col
    return best_col

def play_cli():
    board = create_board()
    human_turn = True
    print("Connect Four - human (O) vs AI (X). Columns 0..6")
    print_board(board)
    while True:
        if human_turn:
            try:
                col = int(input("Your move (0-6): ").strip())
            except:
                print("Invalid input.")
                continue
            if not is_valid_move(board, col):
                print("Invalid move.")
                continue
            make_move(board, col, -1)
        else:
            print("AI is thinking...")
            col = find_best_move(board, max_depth=4)
            if col is None:
                print("No moves left.")
                break
            print(f"AI chooses column {col}")
            make_move(board, col, 1)

        print_board(board)
        winner = check_winner(board)
        if winner == 1:
            print("AI (X) wins.")
            break
        if winner == -1:
            print("Human (O) wins.")
            break
        if is_board_full(board):
            print("Draw.")
            break
        human_turn = not human_turn

if __name__ == "__main__":
    play_cli()