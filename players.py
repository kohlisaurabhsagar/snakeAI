from game import *

class RandomPlayer:
    def __init__(self, i):
        self.i = i
    def get_move(self, board, snake):
        r = rand.randint(0, 3)
        return MOVES[r]