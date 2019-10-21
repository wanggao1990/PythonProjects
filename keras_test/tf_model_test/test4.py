import tensorflow as tf
import numpy as np

from tensorflow.python.platform import gfile


graph = tf.Graph()


x_data = np.random.rand(3)
y_data = x_data*2+1

with tf.Session(graph=graph) as sess:

    with gfile.FastGFile('./3/model.pb', 'rb') as f: #加载模型
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='')  # 导入计算图

        sess.run(tf.global_variables_initializer())

        #变量可以直接读取
        print(sess.run(['w:0','b:0']))  


        # net input and output
        inp = sess.graph.get_tensor_by_name('input_x:0')  
        outp = sess.graph.get_tensor_by_name('output:0')
   
        result = sess.run(outp,feed_dict={inp:x_data})
        
        print(result,y_data)
