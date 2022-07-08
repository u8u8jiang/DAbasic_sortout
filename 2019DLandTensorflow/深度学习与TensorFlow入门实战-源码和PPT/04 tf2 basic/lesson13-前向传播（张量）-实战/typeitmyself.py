import  tensorflow as tf
from    tensorflow import keras
from    tensorflow.keras import datasets


# x: [60k, 28, 28], y: [60k]
(x, y), _ = datasets.mnist.load_data()
# x: [0~255] => [0~1.]
x = tf.convert_to_tensor(x, dtype=tf.float32) / 255.
y = tf.convert_to_tensor(y, dtype=tf.int32)

print(x.shape, y.shape, x.dtype, y.dtype)  #(60000, 28, 28) (60000,) <dtype: 'float32'> <dtype: 'int32'>
print(tf.reduce_min(x), tf.reduce_max(x))
print(tf.reduce_min(y), tf.reduce_max(y))

    