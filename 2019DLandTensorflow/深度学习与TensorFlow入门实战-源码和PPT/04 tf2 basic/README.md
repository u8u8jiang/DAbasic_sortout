# tf2 basic
## 07 數據類型


### Data container  
1. list: 可插入各類型的資料型態 [1, 1.2, 'hello', (1,2), longers]  
2. np.array: 同類型的資料型態 [64, 224, 224, 3], numpy在tensorflow開發前便已存在，所以這不能作GPU計算
3. tf.Tensor: 


:turtle: what's tensor?  
- scalar, vector, matrix, tensor  
- tensor的概念比較大，幾乎涵蓋了所有的數據類型  
- tensorflow: tensor經過各種運算，在網絡中間不停流動，最後得到我們想要的結果。
![](images/image1.png) 

:turtle: tf的基本數據類型   
- int, float, double  
- bool  
- string  

tf是一個"科學計算庫"(computing lib)，依然可支持bool(equal), string。  

```py
#1 create tensor   
tf.constant(1)
tf.constant(1.)
tf.constant(2.2, dtype=tf.int32)
tf.constant(2., dtype=tf.double)  
tf.constant([True, False]) #bool
tf.constant('hello world')  #string

#2 tensor property  
with tf.device("cpu"):
    a = tf.constant([1])
with tf.device("gpu"):
    b = tf.range(4)
a.device  #a device on CPU
b.device  #a device on GPU

aa = a.gpu()
aa.device
bb = b.cpu()
bb.device

b.numpy() #turn tensor to numpy, array([0,1,2,3])
b.ndim  #=1
tf.rank(b)  #numpy=1
tf.rank(tf.ones([3,4,2]))  #numpy=3
b.name

#3 check whether is tensor, and tensor type
a = tf.constant([1.])
b = tf.constant([True, False])
c = tf.constant('hello world')
d = np.arange(4)

isinstance(a, tf.Tensor)  #true
tf.is_tensor(b) #true
tf.is_tensor(d) #false
a.dtype, b.dtype, c.dtype #(tf.float32, tf.bool, tf.string)

a.dtype == tf.float32 #true
c.dtype == tf.string #true

#4 convert
a = np.arange(5) #array([0, 1, 2, 3, 4])
a.dtype #dtype('int32')

aa = tf.convert_to_tensor(a)
aa = tf.convert_to_tensor(a, dtype=tf.int32)

tf.cast(aa, dtype=tf.float32)
aaa = tf.cast(aa, dtype=tf.double)
tf.cast(aaa, dtype=tf.int32)


# 4.1 convert between bool and int
b = tf.constant([0,1])
tf.cast(b, dtype=tf.bool) #numpy=array([False,  True]
bb = tf.cast(b, dtype=tf.bool)
tf.cast(bb, tf.int32) #numpy=array([0, 1])

# 4.2 tf.Variable, trainable: 可求導
a = tf.range(5)
b = tf.Variable(a)
b.dtype #tf.int32
b.name  #'Variable:0'

b = tf.Variable(a, name='input_data')
b.name  #'input_data:0'
b.trainable  #true, trainable: 可求導 dL/
#When turning variable, 'TRAINABLE' record the info of diff trainable. this is characteristic of NN.

isinstance(b, tf.Tensor)  #false
isinstance(b, tf.Variable) #true
tf.is_tensor(b)  #true

b.numpy()  #array([0,1,2,3,4])


# 4.3 convert to numpy
a.numpy()
array([[ 0.03739073, -1.0016401 ],
       [ 0.26954213, -0.21734552]], dtype=float32)
b.numpy()
array([[ 0.03739073, -1.0016401 ],
       [ 0.26954213, -0.21734552]], dtype=float32)

a = tf.ones([])  #is tensor, here is scalar
a.numpy()  #1.0
int(a)     #1
float(a)   #1.0

```







