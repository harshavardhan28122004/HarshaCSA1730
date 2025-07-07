def initialize_board():
    return [' ' for _ in range(9)]

def display_board(board):
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")

def play_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move. Choose from 1 to 9.")
                continue
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("Cell already taken. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # columns
            (0,4,8), (2,4,6)]           # diagonals
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return True
    return False

def check_draw(board):
    return ' ' not in board

def tic_tac_toe():
    board = initialize_board()
    current_player = 'X'

    while True:
        display_board(board)
        play_turn(board, current_player)

        if check_winner(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            display_board(board)
            print("The game is draw")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
print("The program executed successfully.")
