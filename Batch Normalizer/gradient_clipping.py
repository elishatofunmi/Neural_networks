"""
    A popular technique to lessen the exploding gradients problem is to simply 
    clip the gradients during backpropagation so that they never exceed some
    threshold (this is mostly useful for recurrent neural networks).
    This is called gradient clipping.
    
    In tensorflow, the optimizer's minimize() function takes care of both computing
    the gradients and applying them, so you must instead call the optimizer's
    compute_gradients() method first, then create an operation to clip the 
    gradients using the clip_by_value(), and finally create an operation to apply
    the clipped gradients using the optimizer's apply_gradients() method.
"""

class gradient_clipping:
    def __init__(self):
        grad_clip = gradient_clipping.__super__()
        threshold = 1.0
        return
    
    def _clip_val(self):
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        grads_and_vars = optimizer.compute_gradients(loss)
        capped_gvs = [(tf.clip_by_value(grad, -threshold, threshold), var)
                      for grad, var in grads_and_vars]
        training_op = optimizer.apply_gradients(capped_gvs)
        
        return