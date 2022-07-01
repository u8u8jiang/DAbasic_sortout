# tf2 basic
## 08 create tensor


1. turn *numpy* to tensor, input *list* to tensor
1. create *zeros, ones*, or any number of tensor
1. tensor but numbers *filled* any number
1. create tensor with *random* prob dist
1. *constant*
1. application

```py
#1 from numpy, list
tf.convert_to_tensor(np.ones([2,3]))
tf.convert_to_tensor(np.zeros([2,3]))

tf.convert_to_tensor([1,2])
tf.convert_to_tensor([1,2.])
tf.convert_to_tensor([[1],[2.]])

#2.1 tf.zeros
tf.zeros([])
tf.zeros([1])
tf.zeros([2,2])
tf.zeros([2,3,3])

#tf.zeros_like: 初始化為0
a = tf.zeros([2,3,3])
tf.zeros_like(a) #zeros but the shape accroding to the shape of a
tf.zeros(a.shape)

#2.2 tf.ones
tf.ones(1)
tf.ones([])
tf.ones([2])
tf.ones([2,3])
tf.ones_like(a)

#3 tensor but numbers filled any number
tf.fill([2,2], 0)
tf.fill([2,2], 0.)
tf.fill([2,2], 1)
tf.fill([2,2], 9)

#4 normal: it's different inefficiency of conv with different initial way
tf.random.normal([2,2], mean=1, stddev=1)
tf.random.normal([2,2])
tf.random.truncated_normal([2,2],mean=0, stddev=1)  #截斷的normal  
# Since some function like sigmond fu. might gradient vanish at std=1 sigma, renewing the solution will become slow. Because of that, we  use "truncated" to select without edged numbers.



```
![](images/image2.png)

 

