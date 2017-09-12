import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation


class Move:
    def pickup(index, objects):
        position = blocks[index].pos

        return position

    def moveto(quadrant, grid):
        if (quadrant == 1):  # Upper Left
            grid[2] = grid[2] - (grid[2]-grid[0])/2
            grid[1] = grid[1] + (grid[3]-grid[1])/2
        elif (quadrant == 2):  # Upper Right
            grid[0] = grid[0] + (grid[2]-grid[0])/2
            grid[1] = grid[1] + (grid[3]-grid[1])/2
        elif (quadrant == 3):  # Lower Right
            grid[0] = grid[0] + (grid[2]-grid[0])/2
            grid[3] = grid[3] - (grid[3]-grid[1])/2
        elif (quadrant == 4):  # Lower Left
            grid[2] = grid[2] - (grid[2]-grid[0])/2
            grid[3] = grid[3] - (grid[3]-grid[1])/2

        return grid


class HumanInput:
    def human_moveto(target, grid, iters, rwd):
        action = []
        reward = []
        for i in range(0, iters-1):
            if (target[0] <= grid[0] + (grid[2]-grid[0])/2):
                if (target[1] <= grid[1] + (grid[3]-grid[1])/2):
                    quad = 4
                else:
                    quad = 1
            else:
                if (target[1] <= grid[1] + (grid[3]-grid[1])/2):
                    quad = 3
                else:
                    quad = 2
            grid = Move.moveto(quad, grid)
            action.append(quad)
            reward.append(rwd-0.01*i*rwd)
        return action, reward, grid

    def grid_to_point(grid):
        point = [(grid[2]+grid[0])/2, (grid[3]+grid[1])/2]
        return point


class Train:
    def imitation(net, action, reward):
        action = np.reshape(action, (action.shape[0]*action.shape[1], 0))
        model.fit(model, action, reward)
        return net
