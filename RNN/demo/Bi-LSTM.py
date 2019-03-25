import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("../MNIST_data", one_hot = True)
# sess = tf.InteractiveSession()

learning_rate = 0.01
max_samples = 40000
batch_size = 128
display_step  = 10

n_input = 28
n_steps = 28
n_hidden = 256
n_classes = 10


x = tf.placeholder(tf.float32, [None, n_steps, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])

weights = tf.Variable(tf.random_normal([2*n_hidden, n_classes]))
biases = tf.Variable(tf.random_normal([n_classes]))

def BiLSTM(x, weigths, biases):
    x = tf.transpose(x, [1, 0, 2])
    x = tf.reshape(x, [-1, n_input])
    x = tf.split(x, n_steps)

    lstm_fw_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)
    lstm_bw_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)

    output, _, _ = tf.nn.static_bidirectional_rnn(lstm_fw_cell, lstm_bw_cell,
                                                  x, dtype=tf.float32)
    return tf.matmul(output[-1], weigths) + biases

pred = BiLSTM(x, weights, biases)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred,
                                                              labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
init = tf.global_variables_initializer()
saver=tf.train.Saver(max_to_keep=1)
with tf.Session() as sess:
    sess.run(init)
    for step in range(max_samples):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        batch_x = batch_x.reshape((batch_size, n_steps, n_input))
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y})
        if step % display_step == 0:
            acc = sess.run(accuracy, feed_dict={x:batch_x, y:batch_y})
            loss = sess.run(cost, feed_dict={x:batch_x, y:batch_y})
            print("Iter " + str(step * display_step) + ",    loss:" + "{:.6f}".format(loss) + ",   acc:"+
                  ",{:.5f}".format(acc))

    saver.save(sess, 'ckpt/mnist.ckpt')

print("finish")
