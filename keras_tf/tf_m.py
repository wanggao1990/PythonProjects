from __future__ import print_function
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result


mnist = input_data.read_data_sets('mnist', one_hot=True)

# 数据
xs = tf.placeholder(tf.float32, [None, 784])/255.
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

# 网络
out_layer1 = tf.layers.dense(inputs=xs, units=512, activation=tf.nn.relu)
out_layer1 = tf.layers.dropout(inputs=out_layer1, rate=keep_prob)

out_layer2 = tf.layers.dense(inputs=out_layer1, units=512, activation=tf.nn.relu)
out_layer2 = tf.layers.dropout(out_layer2, rate=keep_prob)

#out_layer3 = tf.layers.dense(inputs=out_layer2, units=10, activation=tf.nn.softmax)
out_layer3 = tf.layers.dense(inputs=out_layer2, units=10)

# 优化函数
prediction = out_layer3
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(labels=ys, logits=prediction)

train_step = tf.train.RMSPropOptimizer(1e-4).minimize(cross_entropy)

# 训练
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1001):
        batch_xs, batch_ys = mnist.train.next_batch(128)
        sess.run(train_step,
                 feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.2}
                 )
   
        if i % 50 == 0:
            print(compute_accuracy(mnist.test.images, mnist.test.labels))
