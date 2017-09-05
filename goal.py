# Determines the robot's goal position
import numpy as np


class goal:
    def training(actions, workspace, gamma=0.9, epsilon=0):
        q = rand(1)
        if q >= epsilon:
            goal = [randint(workspace[0]+1, size=1),
                randint(workspace[1]+1, size=1)]
        else:
            # Insert Prediction Function
            goal = max(prediction)
        return goal

    def testing():

        return goal
