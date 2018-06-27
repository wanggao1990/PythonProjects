import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = "layer%d" % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope("Weights"):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
            tf.summary.histogram(layer_name + '/weights', Weights)                  # 查看训练过程中的变化
        with tf.name_scope("b"):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name="b")
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope("Wx_plus_b"):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
            tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs

x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.1, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

# with tf.name_scope("Input"):
xs = tf.placeholder(tf.float32, [None, 1], name="x_input")
ys = tf.placeholder(tf.float32, [None, 1], name="y_input")

l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

with tf.name_scope("Loss"):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]), name="loss")
    tf.summary.scalar("loss", loss)   ## 纯数值

with tf.name_scope('Train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    merged = tf.summary.merge_all()  # ??合并所有收集的数据
    writer = tf.summary.FileWriter("logs/", sess.graph)
    sess.run(init)
    for i in range(1000):
        # training
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            # to see the step improvement
            #print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
            result = sess.run(merged, feed_dict={xs: x_data, ys: y_data}) #merged也需要run
            writer.add_summary(result, i)
