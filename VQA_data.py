
import numpy as np
import os
num_channels = 10
height = 1
width = 3
X_train = np.zeros((2, 10,3))
X_val = np.zeros((2, 10,3))
print X_val.shape
X_train[0] = [[1, 0, 0], [0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1 ]]
X_train[1] = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1],[0, 0, 1 ],[0, 0, 1], [0, 0, 1 ]]
#y_train = [1,2]
y_train = [[1,0],[0,1]]
X_val[0][:][:] = [[0, 0, 0], [0, 0, 1],[ 1, 0, 0],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1],[ 0, 0, 1 ]]
X_val[1][:][:] = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 0],[0, 0, 1 ],[0, 0, 1], [0, 0, 1 ]]
#y_val = [1,2]
y_val = [[1,0],[0,1]]

# caffe needs your data to be in float32
X_train = np.array(X_train,dtype = 'float32')
y_train = np.array(y_train,dtype = 'float32')
X_val = np.array(X_val,dtype = 'float32')
y_val = np.array(y_val,dtype = 'float32')

X_train = np.reshape(X_train, (2,num_channels,height,width))
X_val = np.reshape(X_val, (2,num_channels,height,width))

# Check the data shape again! 
print 'Modified Train data shape: ', X_train.shape
print 'Modified Validation data shape: ', X_val.shape
# proceed to creating HDF5. We will create and store the data in folder `hdf5-data` folder 
import h5py
# with h5py.Fil('/path/to/whatever-name-you-want.h5','w') as f:
with h5py.File('train.h5', 'w') as f:
    f['data'] = X_train # f['name'] - the name field is very important as that is what caffe will recognize
    f['labels'] = y_train
with h5py.File('test.h5', 'w') as f:
    f['data'] = X_val
    f['labels'] = y_val
print 'HDF5 files are written. Need to make the txt files!'
