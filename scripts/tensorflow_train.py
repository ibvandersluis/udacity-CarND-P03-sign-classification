#!/usr/bin/env python3

import tensorflow as tf

tf.compat.v1.disable_eager_execution()

x = tf.Variable(5)

n_features = 120
n_labels = 5
weights = tf.Variable(tf.compat.v1.truncated_normal((n_features, n_labels)))

bias = tf.Variable(tf.zeros(n_labels))

init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)