# A tic-tac-toe game that can be played in the terminal (hot seat mode)
from itertools import combinations


def introduction():
    return \
        """                 Welcome to Tic-Tac-Toe! 

    This simple game is for two players, X and O, who take 
    turns marking the spaces in a 3×3 grid. The player who 
    succeeds in placing three of their marks in a diagonal, 
    horizontal, or vertical row is the WINNER.

    More info - on https://en.wikipedia.org/wiki/Tic-tac-toe
    """


class Grid:
    """Creates a 3x3 grid and stores player marks on it."""

    def __init__(self):
        self.keys = self.values = range(1, 10)
        self._grid_val = dict(zip(self.keys, self.values))

    def is_full(self):
        """
        Check whether all cells are marked with either X or O.
        """
        return len(set(self._grid_val.values())) == 2

    def reset(self):
        """Reset all cell values of the grid. Is used for restart."""
        self._grid_val = dict(zip(self.keys, self.values))

    def update_position(self, cell, mark):
        """
        Add new marks to the cells.
        """
        try:
            if self._grid_val[cell] not in ("X", "O"):
                self._grid_val[cell] = mark
                return True
            else:
                print(f"The {cell} is already occupied.")
                return False
        except KeyError:
            print("There is no such cell. Please retype.")

    def __repr__(self):
        return f"""
              {self._grid_val[1]} | {self._grid_val[2]} | {self._grid_val[3]}
             --- --- ---
              {self._grid_val[4]} | {self._grid_val[5]} | {self._grid_val[6]}
             --- --- ---
              {self._grid_val[7]} | {self._grid_val[8]} | {self._grid_val[9]}
            """


class Player:
    """Holds info about player name, his/her mark type. Can add marks onto the grid."""
    __instance = 1

    def __init__(self, name):
        self._name = name

        # assign a mark to each player
        if Player.__instance == 1:
            self._mark_type = "X"
            Player.__instance += 1
        else:
            self._mark_type = "O"

    @property
    def mark_type(self):
        return self._mark_type

    def update_grid(self, grid_obj, cell):
        """Player can add marks to the grid."""
        return grid_obj.update_position(cell, self._mark_type)

    def __repr__(self):
        return self._name


class GameController:
    """Receives all info from and about players, tracks their marks
    and controls general flow of the game."""

    def __init__(self):
        self._player_names = {}  # players order and names
        self._player_marks = {}  # list of each player's marks

    def input_names(self):
        """Ask for player names and save them."""

        for each in range(1, 3):
            while True:
                name = input(f"Player #{each}, please enter your name: ")
                # ensure the input does contain symbols
                if name.strip(" ") not in (" ", ""):
                    # ensure there are no duplicated names
                    if name not in self._player_names.values():
                        self._player_names[each] = name
                        self._player_marks[name] = []
                        break
                    else:
                        print("This name is already occupied. Please, choose another one.")
                else:
                    print("Your name cannot be empty.")
        print("Let's play now!".center(40))

    @staticmethod
    def input_mark(player):
        """Get cell number from a player to place a mark."""
        while True:
            input_cell = input(f"{player}, choose a cell (0-9) to place '{player.mark_type}' on it: ")
            try:
                return int(input_cell)
            except ValueError:
                print("Please, type in a cell number using digits only.")

    def check_victory(self, player):
        """
        Per player, create unique combinations out of all marked cells
        and, for each combination, check whether:
            1) sum of its numbers equals to any value from the 'victory' pattern
            2) there aren't more than 2 numbers divisible by 2
        """
        VICTORY_SUM = (6, 12, 15, 18, 24)
        sorted_marks = sorted(self._player_marks[str(player)])
        combinations_ = combinations(sorted_marks, 3)
        for combi in combinations_:
            # check for condition 1
            if sum(combi) in VICTORY_SUM:
                # check for condition 2
                even_num = [num for num in combi if num % 2 == 0]
                if len(even_num) <= 2:
                    return True
        return False

    def gameplay(self, grid_obj, player_1_obj, player_2_obj):
        """Switch turns, place marks onto the grid, check for victory."""
        while True:
            for player in (player_1_obj, player_2_obj):
                while True:
                    # get cell number to place player's mark
                    cell = self.input_mark(player)
                    # try to update the grid with a given mark
                    if player.update_grid(grid_obj, cell):
                        # add cell number to player's list
                        # (is needed to check for victory condition)
                        self.update_player_marks(player, cell)
                        print(grid_obj)
                        if self.check_victory(player):
                            print(f"The winner is {player}. Congrats!\n")
                            self.restart(grid_obj)
                        if grid_obj.is_full():
                            print("It's a tie!\n")
                            self.restart(grid_obj)
                        break

    def restart(self, grid_obj):
        """Ask player to restart the game. If positive, reset grid cells
        and player marks."""
        while True:
            input_restart = input("Do you want to start over? Y/N: ")
            if input_restart in ("Y", "y"):
                grid_obj.reset()
                for key in self._player_marks.keys():
                    self._player_marks[key] = []
                print(grid_obj)
                break
            elif input_restart in ("N", "n"):
                exit()
            else:
                print("Please type 'Y' or 'N' as an answer to continue.")

    def update_player_marks(self, player, position):
        """Add a new mark to player's count. Is used to check for victory."""
        self._player_marks[str(player)].append(position)

    def __getitem__(self, item):
        return self._player_names[item]


if __name__ == "__main__":
    # Present the game introduction
    print(introduction())
    while True:
        # Instantiate a grid object
        grid = Grid()
        # Instantiate a game controller object
        tic_tac_toe = GameController()
        # Call for player names
        tic_tac_toe.input_names()
        # Instantiate player objects
        first_player = Player(tic_tac_toe[1])
        second_player = Player(tic_tac_toe[2])
        # Present the starting grid
        print(grid)
        # Start the game, switch turns, check for victory condition
        # and prompt to restart
        tic_tac_toe.gameplay(grid, first_player, second_player)
