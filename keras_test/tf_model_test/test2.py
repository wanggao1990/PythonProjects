import tensorflow as tf
import numpy as np

x_data = np.random.rand(3)
y_data = 2*x_data+1

x = tf.placeholder(tf.float32)
w = tf.Variable(0.0)
b = tf.Variable(0.0)

y = x*w+b

init = tf.global_variables_initializer()

with tf.Session() as sess:
    #sess.run(init)
    saver = tf.train.Saver()
    saver.restore(sess, "./3/model_final")
    result = sess.run(y,feed_dict={x:x_data})
    print(result,y_data)


