### This file will be where the nn is trained and saves it to file
import numpy as np
import tensorflow as tf

from preprocess import get_nn_x_y

nn_data = get_nn_x_y()

#define hyperparamters
batch_size = 200
complexity = 25
epochs = 10
learning_rate = .01
num_feature_inputs = 268

# create network
_inputs = tf.placeholder(tf.float32, [None, num_feature_inputs],
    name = 'inputs')
_labels = tf.placeholder(tf.float32, [200], name = 'labels')

biases = {
    'layer_one' : tf.Variable(tf.random_normal([complexity])),
    'layer_two' : tf.Variable(tf.random_normal([1]))
}

weights = {
    'layer_one' : tf.Variable(tf.random_normal([num_feature_inputs,
        complexity])),
    'layer_two' : tf.Variable(tf.random_normal([complexity, 1]))
}

## layer with sigmoid activation
nn = tf.add(tf.matmul(_inputs, weights['layer_one']), biases['layer_one'])
nn = tf.nn.relu(nn)
nn = tf.add(tf.matmul(nn, weights['layer_two']), biases['layer_two'])
nn = tf.nn.sigmoid(nn)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = nn,
    labels = _labels))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as s:
    s.run(init)

    for e in range(1, epochs + 1):
        _cost = 0
        for i in range(nn_data.num_examples // batch_size):
            _x, _y = nn_data.get_batch(batch_size)

            _, c = s.run([optimizer, cost], feed_dict = {
                _inputs : _x,
                _labels : _y
            })

            _cost += c / total_batch

        print('Epoch:', epoch + 1, '| average cost =', '.04f' % avg_cost)

    print('Done')
