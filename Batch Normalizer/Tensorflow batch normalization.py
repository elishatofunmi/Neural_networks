import tensorflow as tf

"""
    This is the implementation of the batch normalization algorithm in 
    tensorflow making use of mnist dataset as the test set.
    This implementation is carried out using 2 layers
"""

import tensorflow as tf
from functools import partial

# define the input dimension
n_inputs = 28 * 28

# define number of hidden neurons for the first hidden layer
n_hidden1 = 300

# define number of hidden neurons for the second hidden layer
n_hidden2 = 100

# define the number of output neurons for the output layer
n_outputs = 10

# define the training placeholder
"""
    We will set it to True during training, but otherwise it will default to False.
    This will be used to tell the tf.layers.batch_normalization() function 
    whether it should use the current mini-batch's mean and standard deviation
    (during training) or the whole training set's mean and standard deviation
    (during testing).
"""
X = tf.placeholder(tf.float32, shape = (None, n_inputs), name = 'X')
training = tf.placeholder_with_default(False, shape = (), name = 'training')


my_batch_norm_layer = partial(tf.layers.batch_normalization, training = training,
                              momentum = 0.9)

# declaring the first hidden layer with n_hidden1 neurons
hidden1 = tf.layers.dense(X, n_hidden1, name = 'hidden1')
"""
   The Batch normalized algorithm uses exponential decay to compute the  running
   averages, which is why it requires the momentum parameter: given a new value
   v, the running average (vector V) is updated through the equation:
   
   vector(v) = vector(v) * momentum + v * (1 - momentum)
"""
# applying the batch normalization algorithm by parsing the training value and
# momentum value as arguments
bn1 = tf.layers.batch_normalization(hidden1, training = training, momentum = 0.9)
# applying the activation function for the batch normalized data
bn1_act = tf.nn.elu(bn1)


# declaring the second hidden layer with n_hidden2 neurons
hidden2 = tf.layers.dense(bn1_act, n_hidden2, name = 'hidden2')
# applying the batch normalization algorithm to layer 2
bn2 = tf.layers.batch_normalization(hidden2, training = training, momentum = 0.9)
# applying the activation function for the batch normalized data for layer 2
bn2_act = tf.nn.elu(bn2)

# declaring the output layer
logits_before_bn = tf.layers.dense(bn2_act, n_outputs, name = 'outputs')
logits = tf.layers.batch_normalization(logits_before_bn, training = training, 
                                      momentum = 0.9)


# extra_update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
with tf.Session() as sess:
    init.run()
    for epoch in range(n_epochs):
        for iteration in range(mnist.train.num_examples //batch_size):
            X_batch, y_batch = mnist.train.next_batch(batch_size)
            sess.run([training_op, extra_update_ops],
                     feed_dict = {training:True, X:X_batch, y: y_batch})
        accuracy_val =accuracy.eval(feed_dict = {X:mnist.test.images,
                                                 y: mnist.test.labels})
        print(epoch, 'Test accuracy: ', accuracy_val)
    save_path = saver.save(sess, './my_model_final.ckpt')
        