# Old Training Algorithm - REFERENCE ONLY

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as matplot
from keras.models import Sequential
from keras.layers import Dense, Activation
from rmove import RbtMove

# Import Data Set
data = sio.loadmat('Data.mat')
data = np.asarray(data)

# Create Network
NetSize = [64, 48, 32, 16]
Actv = ['tanh', 'tanh', 'tanh', 'tanh']
# NumInputs = data[:, 0, 0].shape
NumInputs = 20  # remove after data is actually imported
net = Sequential()
# First Layer
net.add(Dense(units=NetSize[0], input_dim=NumInputs))
net.add(Activation(Actv[0]))
# Additional Layers
for i in range(1, len(NetSize)-1):
    net.add(Dense(units=NetSize[i]))
    net.add(Activation(Actv[i]))
net.summary()
# Import Loss Function
lf = 'mean_squared_error'  # add custom loss function later
# Compile Model
model.compile(loss=lf, optimizer='sgd')
# Simluation Paramaters
iterations = data.shape[2]
# Training Paramaters
epsilon = 0
gamma = 0.9  # Future reward discount
goal = 0  # Error Goal
while (l > goal):
    for i in range(0, data.shape[2]):
        datai = data[:, :, i]  # Import Data of Interest
        r_pos = [18, 2]  # Set robot's initial position
        for j in range(0, datai.shape[1]):  # Loop through data
            # Insert network stuff here
            (dx, dy, t) = RbtMove.path(r_pos, goal, speed)  # Plan robot's path
            for j in range(0, t):
                r_pos = RbtMove.move(r_pos, dx, dy)  # Move robot through path
