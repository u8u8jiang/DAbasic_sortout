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
#create tensor   
tf.constant(1)
tf.constant(1.)
tf.constant(2.2, dtype=tf.int32)
tf.constant(2., dtype=tf.double)  
tf.constant([True, False]) #bool
tf.constant('hello world')  #string

#tensor property  
with tf.device("cpu"):
    a = tf.constant([1])
with tf.device("gpu"):
    a = tf.range(4)
a.device
b.device

aa = a.gpu()
aa.device
bb = b.gpu()
bb.device

b.numpy()
b.ndim
tf.rank(b)
tf.rank(tf.ones([3,4,2]))
b.names







```







