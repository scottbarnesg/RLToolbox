# Executable file for Keras training
from train import train
from data import data
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
from keras.callbacks import History
from keras import optimizers
from goal import goal
import numpy as np
import matplotlib.pyplot as plt


# Import data
print('Loading Data')
path = '/home/scottgbarnes/Documents/Simulation/RLToolbox/Test Set/Data1.mat'
print('...')
data = data.load(path)
print('Data Loaded\n')
# Format Data for Training
lim = data.shape[2]
inpt = np.concatenate((data[:, 1, 0:lim-1], data[:, 2, 0:lim-1]), axis=0)
trgt = data[0, 1:3, 1:lim]
inpt = np.transpose(inpt)
trgt = np.transpose(trgt)
inpt = inpt[:, np.newaxis, :]
print(inpt.shape)
print(trgt.shape)
# Create Network Paramaters
print('Creating Network')
print('...')
model = Sequential()
model.add(Dense(9, input_shape=(1, inpt.shape[2])))
model.add(LSTM(9, return_sequences=True))
# model.add(LSTM(9, return_sequences=True))
model.add(LSTM(2))
# model.add(Dense(units=36, input_dim=18))
# model.add(Activation('relu'))
# model.add(Dense(units=18))
# model.add(Activation('relu'))
# model.add(Dense(units=9))
# model.add(Activation('relu'))
# model.add(Dense(units=2))
# model.add(Activation('linear'))
print('Network Structure:')
model.summary()
# Compile Network
# optimizers.rmsprop(lr=0.00001)
model.compile(loss='mean_squared_error',
    optimizer='rmsprop')
print('Model Compiled')
# Define Reward Function
# Define Workspace Paramaters
workspace = (600, 480)
# Train Model
epch = 1000
print('Training Model')
print('...')
hist = model.fit(inpt, trgt, epochs=epch, batch_size=15)
history = History()
plt.plot(range(1, epch+1), hist.history['loss'])
plt.show()
print('Training Complete')
