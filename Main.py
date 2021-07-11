# A tic-tac-toe game that can be played in the terminal
greeting = """              Welcome to Tic-Tac-Toe! 

This simple game is for two players, X and O, who take turns marking the spaces in a 3×3 grid. 
The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.

More info can be found on https://en.wikipedia.org/wiki/Tic-tac-toe
"""
print(greeting)
# Ask for player names and save them
players = {}
for each in range(1,3):
 print(f"Player {each}, please enter your name:")
 players[each] = input()
# Show a base grid

# Create a grid of 9 cells with None values
grid_cells_nums = [each for each in range(0, 9)]
grid = dict.fromkeys(grid_cells_nums)
print(grid)
print(f"")
# cell_sample = \
#  """
#  ---
# |   |
#  ---
#  """
# print(cell_sample)