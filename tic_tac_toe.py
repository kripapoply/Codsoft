board = [" " for i in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for position in win_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] == player:
            return True

    return False

def board_full():
    return " " not in board

current_player = "X"

while True:

    print_board()

    move = int(input("Player " + current_player + ", enter position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = current_player
    else:
        print("Position already taken!")
        continue

    if check_winner(current_player):
        print_board()
        print("Player", current_player, "wins!")
        break

    if board_full():
        print_board()
        print("It's a draw!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
