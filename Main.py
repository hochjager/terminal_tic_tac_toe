# A tic-tac-toe game that can be played in the terminal

# Greeting
greeting = """              Welcome to Tic-Tac-Toe! 

This simple game is for two players, X and O, who take turns marking the spaces in a 3×3 grid. 
The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.

More info can be found on https://en.wikipedia.org/wiki/Tic-tac-toe
"""
print(greeting)

# Ask for player names and save them
players = {}
marks = ["empty", "X", "O"]
for each in range(1, 3):
    print(f"Player #{each}, please enter your name:")
    players[each] = input()
    print(f"You will be playing using {marks[each]}.\n")
print("Let's play now!")

# Create a grid of 9 cells with " " (empty) values
# grid_cells_nums = [each for each in range(0, 9)]
# grid = dict.fromkeys(grid_cells_nums, "")
base_grid = \
    """
  1 | 2 | 3
 --- --- ---
  4 | 5 | 6 
 --- --- ---
  7 | 8 | 9 
"""
print(base_grid)


# Game mechanics. Checking turns and prompting players to insert X or O, depending on player's turn.
def game_switcher(turn):
    switcher = turn % 2 + 1
    print(f"{players[switcher]}, please, type a number of a cell where you want to put your mark {marks[switcher]}.")
    marked_cell = input()
    if marked_cell in base_grid:
        base_grid.replace(marked_cell, marks[switcher])
        print(base_grid)
        base_grid = base_grid
    else:
        print("Wrong character.")
        game_switcher(turn)


for turn in range(0, 9):
    game_switcher(turn)
    print(base_grid)

#     marked_cell = input()
# else:
