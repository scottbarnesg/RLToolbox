# Used to Test Functions
from data import data
import numpy as np
from sim import sim
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
import keras.utils
from data import data
from keras.callbacks import History
import matplotlib.pyplot as plt
from keras import optimizers
# model = Sequential()
# model.add(Dense(units=32, input_shape=(9,)))
# model.add(Activation('relu'))
# model.add(Dense(units=1))
# model.add(Activation('linear'))
# model.summary()
# # comile model
# model.compile(loss='mean_squared_error',
#     optimizer='sgd')
# print('Loading data...')
# fn = '/home/scottgbarnes/Documents/Simulation/Training/Test Set/Data1.mat'
# print('...')
# d = data.load(fn)
# print(d.shape)
# print(d.shape)
# print('Data Successfully Loaded')
# # Test Reshape
# # print('Test Reshaping Array')
# # test = d[:, 0, 0]
# # print(test.shape)
# reward = sim.run(d[:, :, 0], (18, 12), model)
# print(reward)
path = '/home/scottgbarnes/Documents/Simulation/Training/Test Set/'
prefix = 'Data'
index = (20, 32)
suffix = '_rev2'
d = data.multiload(path, prefix, index, suffix)
# print(d.shape)
[inpt, trgt] = data.preplstm(d)
# print(inpt.shape)
# print(trgt.shape)
model = Sequential()
model.add(LSTM(9, input_shape=(1, inpt.shape[2]), return_sequences=True))
# model.add(LSTM(4, return_sequences=True))
model.add(LSTM(2))
model.summary()
optimizers.rmsprop(lr=0.2)
model.compile(loss='mean_squared_logarithmic_error',
    optimizer='rmsprop')
epch = 100
print('Training Model')
print('...')
hist = model.fit(inpt, trgt, epochs=epch)
history = History()
plt.plot(range(1, epch+1), hist.history['loss'])
plt.show()
