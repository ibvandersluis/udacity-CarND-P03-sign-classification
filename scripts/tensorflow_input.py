#!/usr/bin/env python3

import tensorflow as tf

tf.compat.v1.disable_eager_execution()

x = tf.compat.v1.placeholder(tf.string)

with tf.compat.v1.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})
    print(output)