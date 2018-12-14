"""
    it is generally not a good idea to train a very large DNN from scratch: 
    instead, you should always try to find an existing neural network that 
    accomplishes a similar task to the one you are trying to tackle, then just
    reuse the lower layers of this network: this is called TRANSFER LEARNING.
    It will not only speed up training considerably, but will also require much 
    less training data.
"""


class transfer_learning:
    def __init__(self):
        transfer_learning = transfer_learning.__super__()
        return
    
    
    def _restore_model(self, path):
        saver = tf.train.import_meta_graph(path)
        return saver
    
    
    def _get_tensor_by_name(self,X, y):
        X = tf.get_default_graph().get_tensor_by_name("X:0")
        y = tf.get_default_graph().get_tensor_by_name('y:0')
        accuracy = tf.get_default_graph().get_tensor_by_name('eval/accuracy:0')
        training_op = tf.get_default_graph().get_operation_by_name('GradientDescent')
        return
    
    def _list_operation_name(self):
        for op in tf.get_default_graph().get_operation():
            print(op.name)