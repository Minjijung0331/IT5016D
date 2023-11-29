# Initialize the game board with empty spaces
squares = [" "] * 9

# Define players as 'X' and 'O'
players = "XO"

# Define the board display template
board = """
  0   1   2
  {0} | {1} | {2}
 -----------
3 {3} | {4} | {5} 5
 -----------
  {6} | {7} | {8}
  6   7   8
"""

# Define winning conditions for the game
win_conditions = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),  # horizontals
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),  # verticals
    (0, 4, 8),
    (2, 4, 6),  # diagonals
]


# Function to check if a player has won
def check_win(player):
    for a, b, c in win_conditions:
        if {squares[a], squares[b], squares[c]} == {player}:
            return True
    return False


# Function to display the current state of the game board
def display_board():
    print(board.format(*squares))


# Function to get a valid player move
def get_player_move():
    move = input(f"{players[0]} to move [0-8] > ")
    return (
        int(move)
        if move.isdigit() and 0 <= int(move) <= 8 and squares[int(move)] == " "
        else None
    )


# Main game loop
while True:
    # Display the current state of the board
    # print(board.format(*squares))
    display_board()

    # Check if 'O' has won
    if check_win(players[1]):
        print(f"{players[1]} is the winner!")
        break

    # Check for a tie (Cats game)
    if " " not in squares:
        print("Cats game!")
        break

    # Player move input
    move = input(f"{players[0]} to move [0-8] > ")

    # Validate the move input
    # if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != " ":
    #     print("Invalid move!")
    #     continue
    if move is None:
        print("Invalid move!")
        continue

    # Update the board and switch players
    # squares[int(move)], players = players[0], players[::-1]

    # Update the square based on the player's move
    squares[int(move)] = players[0]

    # Switch players for the next move
    players = players[::-1]
