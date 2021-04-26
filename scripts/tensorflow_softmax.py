#!/usr/bin/env python3

import tensorflow as tf

tf.compat.v1.disable_eager_execution()

logit_data = [2.0, 1.0, 0.1]
logits = tf.compat.v1.placeholder(tf.float32)

softmax = tf.nn.softmax(logits)  

with tf.compat.v1.Session() as sess:
    output = sess.run(softmax, feed_dict={logits: logit_data})