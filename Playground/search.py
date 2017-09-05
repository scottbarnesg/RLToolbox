import matplotlib.pyplot as plt
import numpy as np
import math
import time
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import History
from MoveActor import SimpleMove
from keras import optimizers


# Create Network
model = Sequential()
model.add(Dense(units=16, input_shape=(5, )))
model.add(Activation('tanh'))
model.add(Dense(units=8))
model.add(Activation('tanh'))
model.add(Dense(units=1))
model.add(Activation('linear'))
model.summary()
sgd = optimizers.SGD(lr=0.0001)
model.compile(loss='mean_squared_error',
    optimizer=sgd)
# Define Simulation Paramaters
space = (100, 100)  # Size of workspace
numobjs = 1  # Number of objects
iters = 1000000 # Number of iterations
rand = 'true'  # Randomize Initial Conditions?
count = 0
for j in range(0, iters):
    # Set up initial conditions
    x_init = np.random.uniform(0, space[0], size=numobjs)
    y_init = np.random.uniform(0, space[1], size=numobjs)
    objs = np.append(x_init, y_init, axis=0)
    objs = objs.reshape(numobjs, 2)
    actr = np.array([np.random.uniform(0, space[0]), np.random.uniform(0, space[1])])
    actr.reshape(1, 2)
    # plt.plot(objs[:, 0], objs[:, 1], 'o', actr[0], actr[1], '*')
    # plt.axis([0, space[0], 0, space[1]])
    # plt.show(block=False)
    # plt.pause(0.5)
    # time.sleep(0.5)
    # plt.hold(False)
    run = 'true'
    while (run == 'true'):
        # ang = np.random.uniform(-math.pi, math.pi) # replace with direction
        # actr = (actr[0]+math.cos(ang), actr[1]+math.sin(ang))
        state = np.append(objs, actr)
        if(count > 0 and np.random.rand() < j/iters):
            max_q = -100
            for k in range(0, 3):
                temp = np.append(state, k)
                temp = temp.reshape(1, 5)
                q = model.predict(temp)
                if(q > max_q):
                    action = k
                    max_q = q # need to train on prediction max_q
            rwd =
            inpt = np.append(state, action)
            inpt = np.reshape(inpt, (1, 5))
            model.fit(inpt, rwd, epochs=1)
        else:
            action = round(np.random.uniform(0, 3))
        actr = SimpleMove.move(actr, action)
        state_old = state
        state = np.append(objs, actr)
        inpt = np.append(state, action)
        # plt.plot(objs[:, 0], objs[:, 1], 'o', actr[0], actr[1], '*')
        # plt.axis([0, space[0], 0, space[1]])
        # plt.show(block=False)
        # plt.pause(0.001)
        # time.sleep(0.001)
        if(actr[0] > space[0] or actr[1] > space[1] or actr[0] < 0 or actr[1] < 0):
            count = count+1
            run = 'false'
            rwd = -1
            print(j)
        elif(round(actr[0]) == round(objs[0, 0]) and round(actr[0]) == round(objs[0, 0])):
            count = count+1
            run = 'false'
            rwd = 1
            print(j)
        if(run == 'false' and count > 1):
            inpt  = np.reshape(inpt, (1, 5))
            rwd = rwd + 0.7*model.predict(inpt)
    inpt = np.reshape(inpt, (1, 5))
    rwd = np.reshape(rwd, (1, 1))
    # print(inpt.shape)
    # print(rwd.shape)
    model.fit(inpt, rwd, epochs=1)
    count = 1

model.save('testmodel1.h5')
