import matplotlib.pyplot as plt
from objects import Blocks
import numpy as np
import time

workspace = (100, 100)
numBlocks = 10
numColors = 1
numSizes = 1
blocks = Blocks.create(numBlocks, numColors, numSizes, workspace)

found = 'false'  # looking for block index 5
grid = np.array([0, 0, workspace[0], workspace[1]])
for i in range(0, numBlocks):
    grid = np.array([0, 0, workspace[0], workspace[1]])
    for j in range(0, 6):
        plt.plot(blocks[i].pos[0], blocks[i].pos[1], 'o', grid[0], grid[1], 'x'
            , grid[0], grid[3], 'x', grid[2], grid[1], 'x', grid[2], grid[3], 'x')
        plt.axis([0, workspace[0], 0, workspace[1]])
        plt.show(block=False)
        plt.pause(0.2)
        time.sleep(0.2)
        plt.hold(False)
        if (blocks[i].pos[0] <= grid[0] + (grid[2]-grid[0])/2):
            grid[2] = grid[2] - (grid[2]-grid[0])/2
            print('Enters 1')
        else:
            grid[0] = grid[0] + (grid[2]-grid[0])/2
            print('Enters 2')
        if (blocks[i].pos[1] <= grid[1] + (grid[3]-grid[1])/2):
            grid[3] = grid[3] - (grid[3]-grid[1])/2
            print('Enters 3')
        else:
            grid[1] = grid[1] + (grid[3]-grid[1])/2
            print('Enters 4')
        print(grid)
        if (blocks[i].pos[0] >= grid[0] and blocks[i].pos[0] <= grid[2]
            and blocks[i].pos[1] >= grid[1] and blocks[i].pos[1] <= grid[2]):
            print('Correct coordinate selected')
        else:
            print('Incorrect coordinate selected')
            print(grid)
            print(blocks[i].pos)

    # for i in range(0, 3): THIS LOOP WILL EXIST FOR THE NN IMPLEMENTATION
