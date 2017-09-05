from sortmove import Move, HumanInput
from objects import Blocks
import numpy as np


# Define Workspace and objects
workspace = (100, 100)
numBlocks = 10
numColors = 1
numSizes = 1
blocks = Blocks.create(numBlocks, numColorms, numSizes, workspace)
for i in range(0, numBlocks-1):
    grid = np.array([0, 0, workspace[0], workspace[1]])
    HumanInput.human_moveto(blocks[i].pos, )
