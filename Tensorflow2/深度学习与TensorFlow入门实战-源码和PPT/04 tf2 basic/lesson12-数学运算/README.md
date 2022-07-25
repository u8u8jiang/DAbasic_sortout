# tf2 basic
## 12 mathmatic


* +-*/
* **, pow, square
* sqrt
* //, %
* exp, log
* @, matmul
* linear layer
  



## Operation type 
* element-wise: +-*/
* matrix-wise: @, matmul  
* dim-wise: reduce_mean/max/min/sum

```py
#1. +-*/, // %
b = tf.fill([2,2], 2.)
a = tf.ones([2,2])

a+b, a-b, a*b, a/b
b//a, b%a


#2. math.log, exp
a
tf.math.log(a) #log exp
tf.exp(a)

tf.math.log(8.)/tf.math.log(2.)     #since log(a,b)/log(b,c)=log(a,c), numpy=3.0
tf.math.log(100.)/tf.math.log(10.)  #numpy=2.0

#3. pow, sqrt
b
tf.pow(b,3)
b**3
tf.sqrt(b)


#4. @, matmul: matrix multiply
a, b
a@b  
tf.matmul(a,b)


#5. with broadcasting
a = tf.ones([4,2,3])               #TensorShape([4,2,3])
b = tf.ones([3,5])                 #TensorShape([3,5])
bb = tf.broadcast_to(b, [4,3,5])   #TensorShape([4,3,5])
a@bb                               #TensorShape([4,2,5])

```

```py
# Y = X@W + b

x = tf.ones([4,2])
W = tf.ones([2,1])
b = tf.constant(0.1)
x@W+b


# out = relu(X@W+b)
x@W+b
out = x@W+b
out = tf.nn.relu(out)


```

