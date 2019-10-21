import tensorflow as tf
import numpy as np

x_data = np.random.rand(3)
y_data = 2*x_data+1
graph = tf.Graph()

with tf.Session(graph=graph) as sess:
    saver = tf.train.import_meta_graph('./3/model_final.meta')
    saver.restore(sess, tf.train.latest_checkpoint("./3/"))
    
    input = graph.get_tensor_by_name("input:0")
    result = sess.run(tf.get_default_graph().get_tensor_by_name("op:0"),feed_dict={input:x_data})
    print(result,y_data)
