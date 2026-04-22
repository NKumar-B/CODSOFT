import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(player):
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

def get_available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

# The Minimax Algorithm
def minimax(is_maximizing):
    # Base cases: evaluate terminal states
    if check_win('O'): # AI wins
        return 1
    elif check_win('X'): # Human wins
        return -1
    elif check_draw(): # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves():
            board[move] = 'O'
            score = minimax(False)
            board[move] = ' ' # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves():
            board[move] = 'X'
            score = minimax(True)
            board[move] = ' ' # Undo move
            best_score = min(score, best_score)
        return best_score

def get_best_move():
    best_score = -math.inf
    best_move = -1
    for move in get_available_moves():
        board[move] = 'O'
        score = minimax(False)
        board[move] = ' ' # Undo move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the AI is 'O'.")
    print("Positions are numbered 0-8, corresponding to the board from left to right, top to bottom.")
    print_board()

    while True:
        # Human Player's turn
        try:
            human_move = int(input("Enter your move (0-8): "))
            if board[human_move] != ' ':
                print("That space is already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        board[human_move] = 'X'
        if check_win('X'):
            print_board()
            print("Congratulations! You won! (Wait, that shouldn't happen...)")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break

        # AI's turn
        print("\nAI is making a move...")
        ai_move = get_best_move()
        board[ai_move] = 'O'
        print_board()

        if check_win('O'):
            print("AI wins! Better luck next time.")
            break
        elif check_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()