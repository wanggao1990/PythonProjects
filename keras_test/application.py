## https://github.com/fchollet/deep-learning-models/releases
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

### 利用ResNet50网络进行ImageNet分类## 
#from keras.applications.resnet50 import ResNet50
from network.resnet50 import ResNet50

import keras
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = keras.models.load_model("model.h5")

#model = keras.models.load_model(r'E:\DeepLearning\keras_test\models\res50_model.h5')

model = ResNet50()
model = ResNet50(weights= r'C:\Users\wg\Desktop\kerasStudy\models/resnet50_weights_tf_dim_ordering_tf_kernels.h5')

# include_top数据
model.load_weights(r'C:\Users\wg\Desktop\kerasStudy\models/resnet50_weights_tf_dim_ordering_tf_kernels(1).h5')

# by_name 为True时无关紧要，只有input可能是不一样的。
#model.load_weights(r'E:\DeepLearning\keras_test\models\resnet50_weights_tf_dim_ordering_tf_kernels_v2.h5')

#model.save(r'E:\DeepLearning\keras_test\models\res50_model.h5')
#model.save_weights(r'E:\DeepLearning\keras_test\models\res50_weights.h5')

##
from keras.utils import plot_model
plot_model(model,r'e:\deeplearning\keras_test\resnet50_network.png',True)

## 

img_path = r'e:\deeplearning\keras_test\data\images\elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=3)[0])
# Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]


### 从VGG19的任意中间层中抽取特征

from network.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model

import numpy as np


import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"    # gpu OOM

#VGG19(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

# notop数据
#base_model = VGG19()
base_model = VGG19(include_top=False, input_shape = (224,224,3), pooling ="avg")
base_model.load_weights(r"c:\users\wg\desktop\kerasstudy\models\vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5",True)


img_path = r'c:\users\wg\desktop\kerasstudy\data\images\elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = base_model.predict(x)
#print('Predicted:', decode_predictions(preds, top=3)[0])


##

model = Model(input=base_model.input, output=base_model.get_layer('block4_pool').output)

img_path = r'c:\users\wg\desktop\kerasstudy\data\images\elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

block4_pool_features = model.predict(x)

## InceptionV3
from network.inception_v3 import InceptionV3, preprocess_input
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K

from keras.applications.imagenet_utils import decode_predictions

import numpy as np


import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"    # gpu OOM


base_model = InceptionV3(input_shape=(299,299,3))


from keras.utils import plot_model
plot_model(base_model, r'E:\DeepLearning\keras_test\Inception_v3_network.png',True)



base_model.load_weights(r"E:\DeepLearning\keras_test\models\inception_v3_weights_tf_dim_ordering_tf_kernels.h5")


img_path = r'E:\DeepLearning\keras_test\data\images\elephant.jpg'
img = image.load_img(img_path, target_size=(299, 299))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = base_model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

## Xception
from network.xception import Xception, preprocess_input
from keras.preprocessing import image
from keras.models import Model
from keras import backend as K

from keras.applications.imagenet_utils import decode_predictions
from keras.utils import plot_model

import numpy as np

import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"    # gpu OOM

base_model = Xception(input_shape=(299,299,3))

#plot_model(base_model,r'e:\deeplearning\keras_test\Xception_network.png',True)

base_model.load_weights(r'e:\deeplearning\keras_test\models\xception_weights_tf_dim_ordering_tf_kernels.h5')


img_path = r'e:\deeplearning\keras_test\data\images\elephant.jpg'
img = image.load_img(img_path, target_size=(299, 299))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = base_model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

## MobileNetV2
import keras

weights = r"c:\users\wg\desktop\kerasstudy\models\inception_v3_weights_tf_dim_ordering_tf_kernels.h5"

model = keras.applications.mobilenet.MobileNet(input_shape=None, alpha=1.0, depth_multiplier=1, include_top=True, weights='imagenet', input_tensor=None, pooling=None, classes=1000)



