import matplotlib.pyplot as plt
import numpy as np
import math
import time
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.callbacks import History
from MoveRobot import SimpleMove

<<<<<<< HEAD
model = load_model('testmodel4.h5')
=======
model = load_model('July16_Model1.h5')
>>>>>>> fbd0af3803fe5f7d5e975dbd2f71ed02300487ea
# Define Simulation Paramaters
space = (20, 20)  # Size of workspace
numobjs = 1  # Number of objects
iters = 10  # Number of iterations
count = 1000
for i in range(0, iters):
    # Set up initial conditions
    x_init = np.random.uniform(0, space[0], size=numobjs)
    y_init = np.random.uniform(0, space[1], size=numobjs)
    objs = np.append(x_init, y_init, axis=0)
    objs = objs.reshape(numobjs, 2)
    actr = np.array([np.random.uniform(0, space[0]), np.random.uniform(0, space[1])])
    actr.reshape(1, 2)
    plt.plot(objs[:, 0], objs[:, 1], 'o', actr[0], actr[1], '*')
    plt.axis([0, space[0], 0, space[1]])
    plt.show(block=False)
    plt.pause(0.5)
    time.sleep(0.5)
    plt.hold(False)
    run = 'true'
    count = 0
    while (run == 'true'):
        count = count + 1
        # ang = np.random.uniform(-math.pi, math.pi) # replace with direction
        # actr = (actr[0]+math.cos(ang), actr[1]+math.sin(ang))
        state = np.append(objs, actr)
        max_q = -100
        for i in range(0, 3):
            temp = np.append(state, i)
            temp = np.reshape(temp, (1, 5))
            q = model.predict(temp)
            print(q)
            if(q > max_q):
                action = i
                max_q = q
        print(max_q)
        actr = SimpleMove.move(actr, action)
        state = np.append(objs, actr)
        inpt = np.append(state, action)
        plt.plot(objs[:, 0], objs[:, 1], 'o', actr[0], actr[1], '*')
        plt.axis([0, space[0], 0, space[1]])
        plt.show(block=False)
        plt.pause(0.001)
        time.sleep(0.001)
        if(actr[0] > space[0] or actr[1] > space[1] or actr[0] < 0 or actr[1] < 0):
            count = count+1
            run = 'false'
            rwd = -1
            print(max_q)
            print(rwd)
        elif(round(actr[0]) == round(objs[0, 0]) and round(actr[0]) == round(objs[0, 0])):
            count = count+1
            run = 'false'
            rwd = 1
            print(max_q)
            print(rwd)
        elif(count > 100):
            run = 'false'
            rwd = -1
            print (max_q)
