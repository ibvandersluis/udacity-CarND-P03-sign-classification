#!/usr/bin/env python3

import tensorflow as tf

tf.compat.v1.disable_eager_execution()

x = tf.add(5, 2) # 7
y = tf.subtract(10, 4) # 6
z = tf.multiply(x, y)  # 10

with tf.compat.v1.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(z)
    print(output)