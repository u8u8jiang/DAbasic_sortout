# tf2 basic
## 11 Broadcasting

* expand
* without coping data (vs.tf.tile)
* tf.broadcast_to


## Key idea
* Insert 1 dim ahead if needed  
* expand dims with size 1 to same size  
such as there are [4,16,16,32], [32] 
turn [32] to [1,1,1,32], and broadcast to [4,16,16,32] with [1,1,1,32] 
extend 4, 16, 16 times, sequentially

## Why broadcasting?
1. for real demanding 

such as [classes, students, scores],   
add bias for every student: +5 score  
[4,32,8] + [5.0]-> [4,32,8]  

2. memory consumption  

[4,32,8] -> 1024*4  
bias= [8]:[5.0, 5.0, 5.0, ...] -> 8*4  
diff between them is 2^10/2^3=2^7  
  
  
## *Some situation*  
situation1:  
[4,32,14,14]  
[1,32,1,1]-> [4,32,14,14] -> broadcastable  

situation2: 
[4,32,14,14]  
[14,14]-> [1,1,14,14]-> [4,32,14,14] -> broadcastable  

situation3: 
[4,32,14,14]  
[2,32,14,14]-> this is not size1 at 0 dim  
  
  
it's efficient and intuitive  

```py
x = tf.random.normal([4,32,32,3])         
(x + tf.random.normal([3])).shape         #TensorShape([4,32,32,3])
(x + tf.random.normal([32,32,1])).shape   #TensorShape([4,32,32,3])
(x + tf.random.normal([4,1,1,1])).shape   #TensorShape([4,32,32,3])
(x + tf.random.normal([1,4,1,1])).shape   #invalid, incompatible  

x.shape                                   #TensorShape([4,32,32,3])
(x + tf.random.normal([4,1,1,1])).shape   #TensorShape([4,32,32,3])
b = tf.broadcast_to(tf.random.normal([4,1,1,1]), [4,32,32,3])
b.shape                                   #TensorShape([4,32,32,3])

```

## broadcast vs tile
```py
a = tf.ones([3,4])
a1 = tf.broadcast_to(a, [2,3,4])

a2 = tf.expand_dims(a, axis=0)
a2 = tf.tile(a2, [2,1,1])

```
