import tensorflow as tf
import numpy as np

from tensorflow.python.framework import graph_util

x_data = np.random.rand(100)
y_data = x_data*2+1

x = tf.placeholder(tf.float32,name="input_x")
y = tf.placeholder(tf.float32,name="input_y")

w = tf.Variable(0.0,name='w')
b = tf.Variable(0.0,name='b')


prediction = tf.add(tf.multiply(w,x),b,  name="output")


loss = tf.reduce_mean(tf.square(y-prediction))
train = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(200):
        sess.run(train,feed_dict={x:x_data,y:y_data})
        if step%10==0:
            print(sess.run([w,b]))
            if step%50 == 0:
                tf.train.Saver().save(sess,"./3/model_iter_%d" % step)

            
    save_path = tf.train.Saver().save(sess,"./3/model_final")

    #指定输出即可
    constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def,['output']) 

    with tf.gfile.FastGFile('./3/model.pb', mode='wb') as f:
        f.write(constant_graph.SerializeToString())
