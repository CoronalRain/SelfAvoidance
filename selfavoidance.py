"""
Self-Avoiding Paths Visualizer 1.0

Usage:
  selfavoidance.py [options]
  selfavoidance.py (-h | --help)
  selfavoidance.py --version

Options:
  -l --lower <int>     Sets a lower bound on the length of the random walk.
                       [default: 0]
  -n --size <int>      Width/Height of the lattice containing the random walk.
                       [default: 51]
  -m --ms <int>        Milliseconds between frames in the animation.
                       [default: 50]
  -c --cmap <string>   Colormap to use.
                       [default: jet]
  -h --help            Show this screen.
  -v --verbose         Show runtime info.
  --version            Show version.
"""

from docopt import docopt

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def get_choices(grid, i, j):
    choices = []
    
    if i-1 >= 0:
        if grid[i-1,j] == 0:
            choices.append("North")
    if j+1 < grid.shape[1]:
        if grid[i,j+1] == 0:
            choices.append("East")
    if i+1 < grid.shape[0]:
        if grid[i+1,j] == 0:
            choices.append("South")
    if j-1 >= 0:
        if grid[i,j-1] == 0:
            choices.append("West")
    
    return choices

def run(n):
    grid = np.zeros((n,n))
    i = n/2
    j = n/2
    counter = 1
    grid[i,j] = counter
    sequence = []
    choices = get_choices(grid, i, j)
    while len(choices) > 0:
        counter += 1
        move = np.random.choice(choices)
        sequence.append(move)
        if move == "North":
            i = i-1
        elif move == "East":
            j = j+1
        elif move == "South":
            i = i+1
        elif move == "West":
            j = j-1
        grid[i,j] = counter
        
        choices = get_choices(grid, i, j)
    sequence.append("Stay")
    
    return sequence

def update(data):
    global sequence, grid, i, j, counter
    newGrid = grid.copy()
    
    counter += 1
    move = sequence[counter-2]
    if move != "Stay" and verbose:
        print(move,)
    if move == "North":
        i = i-1
    elif move == "East":
        j = j+1
    elif move == "South":
        i = i+1
    elif move =="West":
        j = j-1
    else:
        counter -= 1
    
    newGrid[i,j] = counter
    
    mat.set_data(newGrid)
    grid = newGrid
    
    return [mat]

if __name__ == "__main__":
    arguments = docopt(__doc__, version = "Self-Avoiding Paths Visualizer 1.0")
    l = int(arguments["--lower"])
    n = int(arguments["--size"])
    ms = int(arguments["--ms"])
    cmap = arguments["--cmap"]
    verbose = arguments["--verbose"]
    
    sequence = run(n)
    while len(sequence) < l:
        sequence = run(n)
    counter = 1
    grid = np.zeros((n,n))
    i = n/2
    j = n/2
    grid[i,j] = counter
    
    fig, ax = plt.subplots()
    mat = ax.matshow(grid, cmap=plt.get_cmap(cmap), vmin=0, vmax=len(sequence))
    if verbose:
        print("Number of moves: ", str(len(sequence)-1))
    if verbose:
        print("Sequence of moves: ",)
    ani = animation.FuncAnimation(fig, update, interval=ms, frames=len(sequence), blit=True, repeat=False)
    plt.show()
