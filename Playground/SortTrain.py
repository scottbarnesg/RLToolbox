from sortmove import Move, HumanInput, Train
from objects import Blocks
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import time
import matplotlib.pyplot as plt


# Define Workspace and objects
workspace = (100, 100)
numBlocks = 10
numColors = 3
numSizes = 1
# Create model
model = 0
blocks = Blocks.create(numBlocks, numColors, numSizes, workspace)
obj = []
for i in range(0, numBlocks):
    if(blocks[i].color == 'Red'):
        color = 1
    elif(blocks[i].color == 'Blue'):
        color = 2
    elif(blocks[i].color == 'Green'):
        color = 3
    else:
        print('Error: Color not identified')
    obj.append(blocks[i].pos)  # Need to figure out how to append correctly
    # obj.append(color)

obj = np.asarray(obj)
obj = np.reshape(obj, (numBlocks, 2))
# Plot Initial Positions
plt.plot(obj[:, 0], obj[:, 1], 'o')
plt.axis([0, workspace[0], 0, workspace[1]])
plt.show(block=False)
plt.pause(0.1)
time.sleep(0.1)
print(obj)
a = []
r = []
current_pos = []
target = [0, 0]
for i in range(0, numBlocks):
    grid = np.array([0, 0, workspace[0], workspace[1]])
    current_pos.append(obj[i, :])
    target[0] = float(input("X-Coordinate: "))
    target[1] = float(input("Y-Coordinate: "))
    # Select Grid and Point
    [action, reward, grid] = HumanInput.human_moveto(target, grid, 7)
    obj[i, :] = HumanInput.grid_to_point(grid)
    a.append(action)
    r.append(reward)
    # Plot Movement
    plt.clf()
    plt.plot(obj[:, 0], obj[:, 1], 'o')
    plt.axis([0, workspace[0], 0, workspace[1]])
    plt.show(block=False)
    plt.pause(0.1)
    time.sleep(0.1)

a = np.asarray(a)
r = np.asarray(r)
pos = np.asarray(current_pos)
a = np.reshape(a, [1, a.size])
r = np.reshape(r, [1, r.size])
print(a.shape)
print(r.shape)
print(pos.shape)
print(a)
print(r)
print(obj)
# Train Model (Batch) - This should be done to different degrees
#    model = Train.imitation(model, a, r)
