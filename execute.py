# Executable file for Keras training
from train import train
from data import data
from keras.models import Sequential
from keras.layers import Dense, Activation
from goal import goal

# Import data
print('Loading Data')
path = '/home/scottgbarnes/Documents/Simulation/RLToolbox/Test Set/Data1.mat'
print('...')
data = data.load(path)
print('Data Loaded')
# Create Network Paramaters
print('Creating Network')
model = Sequential()
model.add(Dense(units=32, input_shape=(9,)))
model.add(Activation('relu'))
model.add(Dense(units=2))
model.add(Activation('linear'))
print('Network Structure')
model.summary()
# Compile Network
model.compile(loss='mean_squared_error',
    optimizer='sgd')
print('Model Compiled')
# Define Reward Function
rew_func = 'copy'
# Define Training Paramaters
gamma = 0.9
epsilon = 0
# Define Workspace Paramaters
workspace = [600, 480]
# Simulate Robot Action
goal = goal.training(numActions, workspace)
