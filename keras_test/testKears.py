##
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import losses
import numpy as np

np.random.seed(123)

import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"


num_samples = 10000
dim_sample = 1
a = 3
b = 0.1

#x_train = np.random.random((num_samples,dim_sample))
#y_train = x_train*a + b + np.random.random()*0.01

# 创建数据集
X = np.linspace(-1, 1, num_samples)
np.random.shuffle(X)    # 将数据集随机化
Y = a * X + b + np.random.normal(0, 0.2, (num_samples, )) # 假设我们真实模型为：Y=0.5X+2

X_train, Y_train = X[:9900], Y[:9900]     # 把前9000个数据放到训练集
X_test, Y_test = X[9900:], Y[9900:]       # 把后1000个点放到测试集


model = Sequential()
model.name = "test sequential model"
model.add(Dense(1, input_dim=dim_sample, name="dense_1"))

model.compile(loss=losses.mean_squared_error, optimizer='rmsprop', metrics=['mse'])

history = model.fit(X_train, Y_train,
                    #validation_split=0.1,
                    epochs=20, batch_size=32)   # 这里 sgd 比rmsprop快

a_,b_ = model.get_weights()
print('a=', a_, '  b=', b_)

### 绘制训练 & 验证的准确率值 损失，  需要 fit给validation_split

import matplotlib.pyplot as plt

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

##
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

##
import matplotlib.pyplot as plt


Y_pred = model.predict(X_test)

plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred, 'g')
plt.show()

## 
from keras.utils import plot_model
"""
def plot_model( model,
                to_file='model.png',
                show_shapes=False,
                show_layer_names=True,
                rankdir='TB'):
    Converts a Keras model to dot format and save to a file.

    # Arguments
        model: A Keras model instance
        to_file: File name of the plot image.
        show_shapes: whether to display shape information.
        show_layer_names: whether to display layer names.
        rankdir: `rankdir` argument passed to PyDot,
            a string specifying the format of the plot:
            'TB' creates a vertical plot;
            'LR' creates a horizontal plot.
"""

plot_model(model, r'E:\DeepLearning\keras_test\graph.png')

##
model.save_weights(r'E:\DeepLearning\keras_test\weight.h5')

model.save(r'E:\DeepLearning\keras_test\model.h5')


##
# model reconstruction from JSON:
from keras.models import model_from_json
model = model_from_json(json_string)

# model reconstruction from YAML
model = model_from_yaml(yaml_string)
res = model.predict(x_train) - y_train
print(res)

##

# save as JSON

json_string = model.to_json()
##
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import losses
import numpy as np

np.random.seed(123)
num_samples = 10000
dim_sample = 1
# 加载模型 方式一
#from keras.models import model_from_json
#model_1 = model_from_json(json_string)

# 加载模型 方式二
model_1 = Sequential()
model_1.add(Dense(1, input_dim=dim_sample, name="dense_1"))

# 加载权重
model_1.load_weights(b'E:\DeepLearning\keras_test\weight.h5')   

num_samples = 10000
dim_sample = 1
a = 3
b = 0.1

x_train = np.random.random((num_samples,dim_sample))
y_train = x_train*a + b + np.random.random()*0.01

res = model_1.predict(x_train) - y_train
print(res)

##
print(model.get_config())

##
print(model.get_weights())
print(model.get_layer("dense_1").get_weights())

##
from keras.models import load_model

import numpy as np

np.random.seed(123)

import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

num_samples = 10000
dim_sample = 1
a = 3
b = 0.1

x_train = np.random.random((num_samples,dim_sample))
y_train = x_train*a + b + np.random.random()*0.01

model = load_model(r'E:\DeepLearning\keras_test\model.h5')
model.load_weights(b'E:\DeepLearning\keras_test\weight.h5')   
res = model.predict(x_train) - y_train
print(res)

##
# For a single-input model with 2 classes (binary classification):
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import losses

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data_0 = np.random.uniform(-0.5,0,(500,100))
labels_0 = np.zeros((500,1))
data_1 = np.random.uniform(0,0.5,(500,100))
labels_1 = np.ones((500,1))

data = np.concatenate([data_0,data_1])
labels = np.concatenate([labels_0,labels_1])

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)

data_test= np.ones((1,100))*-0.3
res=model.predict(data_test)

res=model.predict(data)


##
import keras

# For a single-input model with 10 classes (categorical classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, one_hot_labels, epochs=10, batch_size=32)


## 基于多层感知器的softmax多分类

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# Generate dummy data
import numpy as np
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)

## MLP的二分类：
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Generate dummy data
x_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
x_test = np.random.random((100, 20))
y_test = np.random.randint(2, size=(100, 1))

model = Sequential()
model.add(Dense(64, input_dim=20, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)

## 

import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

# Generate dummy data
x_train = np.random.random((100, 100, 100, 3))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)

x_test = np.random.random((20, 100, 100, 3))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)

model = Sequential()
# input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(x_train, y_train, batch_size=32, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=32)

##

import numpy as np

a = np.array([[1,2],[3,4]])
sum0 = np.sum(a, axis=0)
sum1 = np.sum(a, axis=1)

##
import tensorflow as tf
from keras.applications import Xception
from keras.utils import multi_gpu_model
import numpy as np

num_samples = 1000
height = 224
width = 224
num_classes = 1000

# Instantiate the base model
# (here, we do it on CPU, which is optional).
with tf.device('/gpu:0'):
    model = Xception(weights=None,
                     input_shape=(height, width, 3),
                     classes=num_classes)

# # Replicates the model on 8 GPUs.
# # This assumes that your machine has 8 available GPUs.
# parallel_model = multi_gpu_model(model, gpus=8)
# parallel_model.compile(loss='categorical_crossentropy',
#                        optimizer='rmsprop')

# Generate dummy data.
x = np.random.random((num_samples, height, width, 3))
y = np.random.random((num_samples, num_classes))



model.compile(loss='categorical_crossentropy',optimizer='rmsprop')
model.fit(x, y, epochs=20, batch_size=256)

# This `fit` call will be distributed on 8 GPUs.
# Since the batch size is 256, each GPU will process 32 samples.
#parallel_model.fit(x, y, epochs=20, batch_size=256)

##
from keras.layers import Input, Dense
from keras.models import Model
import numpy as np

# This returns a tensor
inputs = Input(shape=(784,))

# a layer instance is callable on a tensor, and returns a tensor
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

# This creates a model that includes
# the Input layer and three Dense layers
model = Model(inputs=inputs, outputs=predictions)

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])


data = np.random.random((1000,784))
labels = np.random.random((1000,10))
model.fit(data, labels, epochs = 10, batch_size = 32)  # starts training

##
import keras
from keras.layers import Conv2D, MaxPooling2D, Input, Dense, Flatten
from keras.models import Model

# First, define the vision modules
digit_input = Input(shape=(27, 27, 1))
x = Conv2D(64, (3, 3))(digit_input)
x = Conv2D(64, (3, 3))(x)
x = MaxPooling2D((2, 2))(x)
out = Flatten()(x)

vision_model = Model(digit_input, out)

# Then define the tell-digits-apart model
digit_a = Input(shape=(27, 27, 1))
digit_b = Input(shape=(27, 27, 1))

# The vision model will be shared, weights and all
out_a = vision_model(digit_a)
out_b = vision_model(digit_b)

concatenated = keras.layers.concatenate([out_a, out_b])
out = Dense(1, activation='sigmoid')(concatenated)

classification_model = Model([digit_a, digit_b], out)


## 瞎测试

def getsss():
    with open('G:/Deep Learning/HDF5/readAndWrite/text_file/train_1.txt','r') as f:
        print( "%s samples" % f.readline())
        for line in f:
            # create Numpy arrays of input data
            # and labels, from each line in the file
            #x, y = process_line(line)
            #yield (x, y)
            line = line.rstrip('\n').split(' ')[:-1]
            y = int(line[0])
            x = list(map(lambda i: float(i), line[1:]))
            yield (x, y)
            
res =  getsss()        

##

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import losses
import numpy as np


import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"



def generate_arrays_from_file(path):
    with open('G:/Deep Learning/HDF5/readAndWrite/text_file/train_1.txt','r') as f:
    #  print( "%s samples" % f.readline()
        f.readline()    
        for line in f:
            line = line.rstrip('\n').split(' ')[:-1]
            
            x = list(map(lambda i: float(i), line[1:]))
            y = int(line[0])
            
            x = np.expand_dims(np.array(x),0)
            y = np.expand_dims(np.array(y),0)

            yield (x,y)

dim_sample = 17

model = Sequential()
model.name = "test sequential model"
model.add(Dense(1, input_dim=dim_sample, name="dense_1"))
model.add(Activation('relu'))

model.compile(loss=losses.mean_squared_error, optimizer='rmsprop', metrics=['mse'])

model.fit_generator(generate_arrays_from_file(r'G:\Deep Learning\HDF5\readAndWrite\text_file/train_1.txt'),
        samples_per_epoch=128, epochs=10)    # 总数 1426
        
model.save("111111.h5")        
##
import h5py
f = h5py.File("111111.h5",'r')

f.close()
        
##       
import keras
model = keras.models.load_model("111111.h5") 
evl = model.evaluate_generator(generate_arrays_from_file(r'G:\Deep Learning\HDF5\readAndWrite\text_file/test_1.txt'),steps=30)


##
import tensorflow as tf


x = tf.constant([[1], [2], [3], [4]], dtype=tf.float32)
y_true = tf.constant([[0], [-1], [-2], [-3]], dtype=tf.float32)

linear_model = tf.layers.Dense(units=1)

y_pred = linear_model(x)
loss = tf.losses.mean_squared_error(labels=y_true, predictions=y_pred)

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

config = tf.ConfigProto()  
config.gpu_options.allow_growth=True   
sess = tf.Session(config=config)
sess.run(init)
for i in range(100):
  _, loss_value = sess.run((train, loss))
  print(loss_value)

print(sess.run(y_pred))