from sortmove import Move, HumanInput, Train
from objects import Blocks
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np


# Define Workspace and objects
workspace = (100, 100)
numBlocks = 10
numColors = 1
numSizes = 1
# Create model
model = 0
blocks = Blocks.create(numBlocks, numColors, numSizes, workspace)
a = []
r = []
for i in range(0, numBlocks-1):
    grid = np.array([0, 0, workspace[0], workspace[1]])
    [action, reward, grid] = HumanInput.human_moveto(blocks[i].pos, grid, 6)
    a.append(action)
    r.append(reward)

a = np.asarray(a)
r = np.asarray(r)
a = np.reshape(a, [1, a.size])
r = np.reshape(r, [1, r.size])
print(a.shape)
print(r.shape)
print(a)
print(r)
# Train Model (Batch) - This should be done to different degrees
#    model = Train.imitation(model, a, r)
