# Function to display the Tic Tac Toe board
def display_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Function to get player's move
def get_move():
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input! Row and column should be between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main function to run the game
def main():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        display_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn:")
        row, col = get_move()

        if board[row][col] == " ":
            board[row][col] = player
            if check_win(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                break
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()
