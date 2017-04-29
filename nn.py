### This file will be where the nn is trained and saves it to file
import numpy as np
import tensorflow as tf

from preprocess import get_nn_x_y

nn_data = get_nn_x_y()

#define hyperparamters
batch_size = 200
complexity = 25
epochs = 50
lr = .01
num_feature_inputs = 268

# create network
_inputs = tf.placeholder(tf.float32, [None, num_feature_inputs],
    name = 'inputs')
_labels = tf.placeholder(tf.float32, [None, 2], name = 'labels')

# define layers
nn = tf.contrib.layers.fully_connected(_inputs, num_outputs = complexity)
nn = tf.contrib.layers.fully_connected(nn, num_outputs = 2)
nn = tf.nn.relu(nn)

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = nn,
    labels = _labels))
optimizer = tf.train.AdamOptimizer(learning_rate = lr).minimize(loss)
corr = tf.equal(tf.argmax(nn, 1), tf.argmax(_labels, 1))
accu = tf.reduce_mean(tf.cast(corr, tf.float32))

init = tf.global_variables_initializer()

with tf.Session() as s:
    s.run(init)

    for e in range(1, epochs + 1):
        _loss = 0
        num_batches = nn_data.num_examples // batch_size

        for i in range(num_batches):
            _x, _y = nn_data.get_batch(batch_size)

            c, _  = s.run([loss, optimizer], feed_dict = {
                _inputs : _x,
                _labels : np.array(_y)
            })

            _loss += (c / num_batches)

        acc = s.run(accu, feed_dict = {
            _inputs : nn_data.get_test()[0],
            _labels : nn_data.get_test()[1]
        })

        print('Epoch:', e, '| Average loss =', _loss, 'Accuracy =', acc)

    print('Done')
