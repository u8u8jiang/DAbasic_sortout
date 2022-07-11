# tf2 adv
## 18 clip

* clip_by_value
* relu
* clip_by_norm
* gradient clipping


```py
#1 clip_by_value
a
tf.maximum(a,2)    #max(0,x), if x<0, res 0 else x
tf.minimum(a,8)    #min(0,x), if x>0, res 0 else x
tf.clip_by_value(a,2,8)

#2 relu
a = a-5            #array([-5,-4,-3,-2,-1,0,1,2,3,4])
tf.nn.relu(a)      #array([0,0,0,0,0,0,1,2,3,4])
tf.maximum(a,0)    #array([0,0,0,0,0,0,1,2,3,4])
```

```py
#3 clip_by_norm
a = tf.random.normal([2,2],mean=10)
tf.norm(a)         #22.14333
aa = tf.clip_by_norm(a,15)
tf.norm(aa)        #15.000001

#4 gradient clipping
# gradient exploding(步長太長, 震盪) or vanishing(不動了)
# set lr=1 -> set larger, and might be vanishing
# new_greds, total_norm=tf.clip_by_global_norm(greds,25) 


#before
(x, y), _ = dataset.mnist.load_data()

# $python main.py 2.0.0-dev20190225



x = tf.convert_to_tensor(x, dtype=tf.float32) / 50.
x:(6000,28,28) y:(60000,10)
sample:(128,28,28) (128,18)

==before==
tf.Tensor(89.03711, shape=(), dtype=float32)
tf.Tensor(2.6175494, shape=(), dtype=float32)
tf.Tensor(118.17449, shape=(), dtype=float32)
tf.Tensor(2.1617627, shape=(), dtype=float32)
tf.Tensor(134.27968, shape=(), dtype=float32)
tf.Tensor(2.5254946, shape=(), dtype=float32)

==before==
tf.Tensor(1143.292, shape=(), dtype=float32)
tf.Tensor(35.841225, shape=(), dtype=float32)
tf.Tensor(1279.236, shape=(), dtype=float32)
tf.Tensor(24.312374, shape=(), dtype=float32)
tf.Tensor(1185.6311, shape=(), dtype=float32)
tf.Tensor(17.80448, shape=(), dtype=float32)

```