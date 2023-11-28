# Game board representation
squares = [" "] * 9

# Players: 'X' and 'O'
players = "XO"

# Board display template
board = """
  0   1   2
  {0} | {1} | {2}
 -----------
3 {3} | {4} | {5} 5
 -----------
  {6} | {7} | {8}
  6   7   8
"""

# Winning conditions for the game
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


# Main game loop
while True:
    # Display the current state of the board
    print(board.format(*squares))

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
    if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != " ":
        print("Invalid move!")
        continue

    # Update the board and switch players
    squares[int(move)], players = players[0], players[::-1]
