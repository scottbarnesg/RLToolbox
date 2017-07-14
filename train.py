# Trains Network

import numpy as np
import matplotlib.pyplot as matplot
from keras.models import Sequential
from data import data
from sim import sim


class train:
    def train(net, data, rwd_func, error_goal=0, batch=1, gamma=0.9, epsilon=0,
            d_eps=0.01):
        # filepath = \
        #    "/home/scottgbarnes/Documents/Simulation/Training/Test Set/Data1.mat"
        data = data.load(filepath)
        error = 100
        while(error > error_goal):
            for i in range(0, data.shape[2]):
                inpt = data[:, :, i]  # Import Data of Interest
                r_pos = (325, 58)  # Set robot's initial position
                reward = sim.train(inpt, r_pos, rwd_func)
        return net


class Test:
    def test(net):
        data = data.importdata('Insert File Name')

        return perf
