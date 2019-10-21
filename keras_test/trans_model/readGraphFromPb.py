import tensorflow as tf


def read_graph_from_pb(tf_model_path ,input_names,output_name):  
    with open(tf_model_path, 'rb') as f:
        serialized = f.read() 
    tf.reset_default_graph()
    gdef = tf.GraphDef()
    gdef.ParseFromString(serialized) 
    with tf.Graph().as_default() as g:
        tf.import_graph_def(gdef, name='') 
    
    with tf.Session(graph=g) as sess: 
        OPS=get_ops_from_pb(g,input_names,output_name)
    return OPS


def get_ops_from_pb(graph,input_names,output_name,save_ori_network=True):
    if save_ori_network:
        with open('ori_network.txt','w+') as w: 
            OPS=graph.get_operations()
            for op in OPS:
                txt = str([v.name for v in op.inputs])+'---->'+op.type+'--->'+str([v.name for v in op.outputs])
                w.write(txt+'\n') 
    inputs_tf = [graph.get_tensor_by_name(input_name) for input_name in input_names]
    output_tf =graph.get_tensor_by_name(output_name) 
    OPS =get_ops_from_inputs_outputs(graph, inputs_tf,[output_tf] ) 
    with open('network.txt','w+') as w: 
        for op in OPS:
            txt = str([v.name for v in op.inputs])+'---->'+op.type+'--->'+str([v.name for v in op.outputs])
            w.write(txt+'\n') 
    OPS = sort_ops(OPS)
    OPS = merge_layers(OPS)
    return OPS


if __name__ == "__main__":

    #model="model.pb"   #正常输出
    model = "frozen_inference_graph.pb"
    #model = r'..\deeplab\deeplabv3_mnv2_pascal_trainval\frozen_inference_graph.pb'
    with tf.Session() as sess:
        with open(model, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            print(graph_def)
