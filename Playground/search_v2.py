
<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import math
import time
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import History
=======
# import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
>>>>>>> fbd0af3803fe5f7d5e975dbd2f71ed02300487ea
from MoveRobot import SimpleMove
from keras import optimizers

model = Sequential()
model.add(Dense(units=16, input_shape=(5, )))
model.add(Activation('tanh'))
model.add(Dense(units=8))
model.add(Activation('tanh'))
model.add(Dense(units=1))
model.add(Activation('linear'))
model.summary()
sgd = optimizers.SGD(lr=0.001)
model.compile(loss='mean_squared_error',
<<<<<<< HEAD
    optimizer='SGD')
# Define Simulation Paramaters
space = (20, 20)  # Size of workspace
numobjs = 1  # Number of objects
iters = 10000  # Number of iterations
gamma = 0.99  # discount factor
plt.hold(False)
=======
    optimizer=sgd)
# Define Simulation Paramaters
space = (20, 20)  # Size of workspace
numobjs = 1  # Number of objects
iters = 100000 # Number of iterations
gamma = 0.99  # discount factor
# plt.hold(False)
>>>>>>> fbd0af3803fe5f7d5e975dbd2f71ed02300487ea
inpt = np.reshape(np.zeros(5), (1, 5))
trgt = np.reshape(np.zeros(1), (1, 1))
for i in range(0, iters):
    # Set up initial state
    # inpt = np.append(inpt, np.reshape(np.zeros(5), (1, 5)), axis=0)
    # trgt = np.append(trgt, np.reshape(np.zeros(1), (1, 1)), axis=0)
    x_init = np.random.uniform(0, space[0], size=numobjs)
    y_init = np.random.uniform(0, space[1], size=numobjs)
    objs = np.append(x_init, y_init, axis=0)
    actr = np.array([np.random.uniform(0, space[0]),
        np.random.uniform(0, space[1])])
    objs = objs.reshape(numobjs, 2)
    # actr = actr.reshape(1, 2)
    init_state = np.append(objs, actr)
    state = init_state
    # Start Simulation
    run = 'true'
    count = -1
    rwd = 0
    while(run == 'true'):
        if(count > 0 and np.random.rand() < 0.9):
            max_q = -100
            for k in range(0, 3):
                temp = np.append(state, k)
                temp = temp.reshape(1, 5)
                q = model.predict(temp)
                if(q > max_q):
                    action = k
                    max_q = q
        else:
            action = round(np.random.uniform(0, 3))
            temp = np.append(state, action)
            temp = temp.reshape(1, 5)
            max_q = model.predict(temp)
        old_state = state
        actr = SimpleMove.move(actr, action)  # take action
        state = np.append(objs, actr)
        rwd_old = rwd
        # check termination criteria
        if(actr[0] > space[0] or actr[1] > space[1] or actr[0] < 0 or actr[1] < 0):
            count = count+1
            run = 'false'
            rwd = -1
        elif(round(actr[0]) == round(objs[0, 0]) and round(actr[1]) == round(objs[0, 1])):
            count = count+1
            run = 'false'
            rwd = 1
        else:
            rwd = -0.01
        # Plot Movement
        # plt.plot(objs[:, 0], objs[:, 1], 'o', actr[0], actr[1], '*')
        # plt.axis([0, space[0], 0, space[1]])
        # plt.show(block=False)
        # plt.pause(0.001)
        # time.sleep(0.001)
        # Update Network
        inpt = np.append(inpt, np.reshape(np.append(old_state, action), (1, 5)), axis=0)
        trgt = np.append(trgt, np.reshape(rwd + gamma*max_q, (1, 1)), axis=0)
        count = count + 1
        if(run == 'false'):
            # if(count-i-1 >= 0):
                # for j in range(count, count-i-1, -1):
<<<<<<< HEAD
            for j in range(0, 100):  # Experience Replay
                index = np.random.randint(inpt.shape[0])
                s = np.reshape(inpt[index, :], (1, 5))
                t = np.reshape(trgt[index, :], (1, 1))
                model.fit(s, t, epochs=1)
=======
            for j in range(0, i+1):  # Experience Replay
                index = np.random.randint(inpt.shape[0])
                s = np.reshape(inpt[index, :], (1, 5))
                t = np.reshape(trgt[index, :], (1, 1))
                model.fit(s, t, epochs=1, verbose=0)
>>>>>>> fbd0af3803fe5f7d5e975dbd2f71ed02300487ea
                # model.fit(np.reshape(inpt[j, :], (1, 5)), trgt[j, :], epochs=1)
            # else:
            #    for j in range(count, 0, -1):
            #        model.fit(np.reshape(inpt[j, :], (1, 5)), trgt[j, :], epochs=1)
<<<<<<< HEAD
            print(i)
            # time.sleep(0.01)
model.save('testmodel4.h5')
=======
            # print(i)
            # time.sleep(0.01)
            if(i % 10000 == 0):
                print(i)
                model.save('July24_Model1.h5')
model.save('July24_Model1.h5')
>>>>>>> fbd0af3803fe5f7d5e975dbd2f71ed02300487ea
