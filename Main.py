# A tic-tac-toe game that can be played in the terminal

import Functions as f

# Print out a greeting
print(f.greeting())

# Ask for player names and save them
players = {}
marks = ["empty", "X", "O"]
for each in range(1, 3):
    print(f"Player #{each}, please enter your name:")
    players[each] = input()
    print(f"You will be playing using {marks[each]}.\n")
print("Let's play now!")

# Create a dictionary that will represent grid cells (str) and their values (int)
grid = {}
for each in range(1, 10):
    grid[f"{each}"] = each
print(grid)


# Draw a grid
def base_grid(grid_values):
    return \
        f"""
      {grid_values["1"]} | {grid_values["2"]} | {grid_values["3"]}
     --- --- ---
      {grid_values["4"]} | {grid_values["5"]} | {grid_values["6"]}
     --- --- ---
      {grid_values["7"]} | {grid_values["8"]} | {grid_values["9"]}
    """


# Game mechanics. Checking turns and prompting players to insert X or O, depending on player's turn.
def turn_switcher(turn):
    switcher = turn % 2 + 1
    print(f"{players[switcher]}, please, type a number of a cell where you want to put your mark {marks[switcher]}.")
    marked_cell = input()
    temp_grid = base_grid(grid)
    if marked_cell in temp_grid:
        grid[marked_cell] = marks[switcher]
        return base_grid(grid)
    else:
        print("Wrong character.")
        turn_switcher(turn)


print(base_grid(grid))

for turns in range(0, 9):
    updated_grid = turn_switcher(turns)
    print(updated_grid)
