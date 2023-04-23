from players import *
from game import *


size = 10
num_snakes = 1
players = [RandomPlayer(0)]
gui_size = 800
pop_size = 100
num_generations = 100
num_trails = 1
window_size = 7
hidden_size = 15
board_size = 10
    
gen_player = GeneticPlayer(pop_size, num_generations, num_trails, window_size, hidden_size, board_size,mutation_chance=0.1, mutation_size=0.1)
gen_player.evolve_pop()

