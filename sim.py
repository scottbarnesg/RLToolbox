# Simulates Robot's Actions
from rf import rf
from rmove import RbtMove
import numpy as np


class sim:
    def run(data, r_pos, net, goal):
        data = np.asarray(data)
        inpt = data[:, 0].reshape(1, 9)
        # print(inpt.shape)
        (dx, dy, t) = RbtMove.path(r_pos, goal)
        # Add loop here?
        for i in range(0, t):
            r_pos = RbtMove.move(r_pos, dx, dy)
            reward = rf.rwd_func(r_pos, h_pos, o_pos)
            net.train_on_batch(inpt, reward)
        return reward

    def test(data, r_pos, net):
        reward = 0
        return reward
