import numpy as np
import scipy.io as sio


class data:
    def load(filename):
        data = sio.loadmat(filename)  # Returns a dictionary, not the array
        data = np.asarray(data['data'])
        return data

    def multiload(filepath, prefix, index, suffix):
        max_x = 0
        max_y = 0
        max_z = 0
        ind = index[1]-index[0]
        for i in range(index[0], index[1]):
            full = filepath + prefix + str(i) + suffix
            d = sio.loadmat(full)
            da = np.asarray(d['data'])
            if(da.shape[0] > max_x):
                max_x = da.shape[0]
            if(da.shape[1] > max_y):
                max_y = da.shape[1]
            if(da.shape[2] > max_z):
                max_z = da.shape[2]

        data = np.zeros((max_x, max_y, max_z, ind))
        for i in range(index[0], index[1]):
            full = filepath + prefix + str(i) + suffix
            d = sio.loadmat(full)
            da = np.asarray(d['data'])
            x = da.shape[0]
            y = da.shape[1]
            z = da.shape[2]
            data[0:x, 0:y, 0:z, i-index[0]] = da
            # data[:, :, :, i-index[0]] = da
        return data

    def preplstm(d):
        data = np.asarray(d)
        print(data.shape)
        max_x = data.shape[0]
        max_y = data.shape[1]
        max_z = data.shape[2]
        ind = data.shape[3]
        inpt = np.concatenate((data[:, 1, 0:max_z-1, :],
            data[:, 2, 0:max_z-1, :]), axis=0)
        trgt = data[0, 1:3, 1:max_z, :]
        print(inpt.shape)
        print(trgt.shape)
        inpt = np.reshape(inpt, (inpt.shape[0], 1, (max_z-1)*ind))
        trgt = np.reshape(trgt, (2, (max_z-1)*ind))
        inpt = np.transpose(inpt, (2, 1, 0))
        trgt = np.transpose(trgt, (1, 0))
        # inpt = inpt[:, np.newaxis, :]
        print(inpt.shape)
        print(trgt.shape)
        return inpt, trgt
