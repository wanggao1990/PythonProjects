## numpy load save savez
import numpy as np
import pickle as pkl
import struct
import matplotlib.pyplot as plt


def load_mnist(folder):
    
    mnist = [
        (folder+'/train-labels.idx1-ubyte',folder+'/train-images.idx3-ubyte'),
        (folder+'/t10k-labels.idx1-ubyte', folder+'/t10k-images.idx3-ubyte')
    ]
    
    def loadFile(labels,imgages):
        with open(labels, 'rb') as f:
            try:
                magic,num = struct.unpack('>2I',f.read(2*4))
                print(magic,num)
                npObj = np.fromfile(f,'ubyte',num)
                lbs =  npObj.reshape(num).astype('i')        
            except EOFError:
                return None
                
        with open(imgages, 'rb') as f:
            try:
                magic,num,w,h = struct.unpack('>4I',f.read(4*4))
                print(magic,num,w,h)
                npObj = np.fromfile(f,'ubyte',num*w*h*4)
                imgs = npObj.reshape(num,w*h).astype('i')        
            except EOFError:
                return None
            
        return imgs,lbs
        
    train = loadFile(mnist[0][0],mnist[0][1])
    test =  loadFile(mnist[1][0],mnist[1][1])
    
    return train,test


#(x_train, y_train), (x_test, y_test) = load_mnist('./data/mnist/')

#plt.imshow(x_train[0].reshape(28,28))
#plt.show()


#np.savez_compressed("./data/mnist/mnist",x_train=x_train,y_train=y_train,x_test=x_test, y_test=y_test)
#ss = np.load("./data/mnist/mnist.npz")


def load_mnist_2(npz):
    ss = np.load(npz)
    return (ss["x_train"], ss["y_train"]), (ss["x_test"], ss["y_test"])

##
import tensorflow as tf

(x_train, y_train),(x_test, y_test) = load_mnist_2("./data/mnist/mnist.npz")

x_train = x_train.reshape(x_train.shape[0], 28, 28)
x_test = x_test.reshape(x_test.shape[0], 28, 28)

x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)


##
'''Trains a simple convnet on the MNIST dataset.

Gets to 99.25% test accuracy after 12 epochs
(there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
'''

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"     # cpu

batch_size = 128
num_classes = 10
epochs = 12

# input image dimensions
img_rows, img_cols = 28, 28

# the data, split between train and test sets
#(x_train, y_train), (x_test, y_test) =  mnist.load_data()
#(x_train, y_train), (x_test, y_test) =  load_mnist('./data/mnist/mnist')
(x_train, y_train), (x_test, y_test) =  load_mnist_2("./data/mnist/mnist.npz")

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
# x_train -= 0.5
# x_test -= 0.5
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

##
model.save("mnis_sampleconv_model.h5")
model.save_weights("mnis_sampleconv_weights.h5")


## 
model = keras.models.load_model("mnis_sampleconv_model.h5")
imgT = x_test[0]
res = model.predict(np.expand_dims(imgT,0)).argmax()
#res = model.predict(np.expand_dims(imgT,0) + 0.5).argmax()
print(res)
plt.imshow(imgT.squeeze())
plt.show()