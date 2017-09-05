import matplotlib.pyplot as plt
import numpy as np
import math
import time
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.callbacks import History
from objects import Blocks
from objects import Robot
from sortreward import SortReward as reward


# Set simulation paramaters
numBlocks = 10
numColors = 3
numSizes = 2
workspace = (10, 10)
# for i in range(0, numBlocks):
#    new_pos = (np.random.uniform(0, workspace[0]),
#        np.random.uniform(0, workspace[1]))
#    blocks[i].update_pos(new_pos)
iters = 1 # Iterations
ttl = 100 # Time to Live (Max number of moves before simulation is terminated)

# Create Network

# Run Simulation
for i in range(0, iters):
    blocks = Blocks.create(numBlocks, numColors, numSizes, workspace)
    robot = Robot(workspace, 'center')
    run = 'true'
    count = 0
    while(run == 'true'):
        # Determine Action to Take by Predicting Reward
        state = np.append(blocks, robot)
        if(count > 0 and np.random.rand() < 0.9):
            max_q = -100
            for j in range(0, numBlocks):
                temp_inpt = np.append(state, j)
                temp_inpt = temp_inpt.reshape(1, (numBlocks+1)*2+1)
                q = model.predict(temp_inpt)
                if q > max_q
                    max_q = q
                    action = j
        else:
            action = np.random.randint(numBlocks)
            temp_inpt = np.append(state, action)
            temp_inpt = temp_inpt.reshape(1, (numBlocks+1)*2+1)
            max_q = model.predict(temp_inpt)

        # Assign Reward
        rwd = reward.color(blocks[i], blocks, numBlocks)
        # Select Goal position

        # Move Robot
        Robot.update_pos(goal)
