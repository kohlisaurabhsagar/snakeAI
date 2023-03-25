from players import *
from game import *

if __name__ == "__main__":
    size = 10
    num_snakes = 1
    players = [RandomPlayer(0)]
    gui_size = 800
    game = Game(size, num_snakes, players, gui=None, display=True, max_turns=100)
    gui = Gui(game, gui_size)
    game.play(True, termination=False)
