# tf2 basic
## 10 the transform of dimension 

* shape, ndim: [batch, height/row, width/col, channel]
* reshape
* expand_dims/squeeze
* transpose
* broadcast_to


### 1 view: ensure including every info, but not to disjoint the data
view1: [b, 28, 28]  
view2: [b, 28*28]  
view3: [b, 2, 14*28]  
view4: [b, 28, 28, 1]  
...


```py
#2 reshape, change view(改變視圖)
a = tf.random.normal([4,28,28,3]) #TensorShape([4,28,28,3]), content


#view1
a.shape, a.ndim                   #(TensorShape([4,28,28,3], 4), view

#view2: [batch,pixels,channels], this is different view and there is no 2dim info.
tf.reshape(a, [4,784,3]).shape    #TensorShape([4,784,3]), 4*28*28*3=4*784*3
tf.reshape(a, [4,-1,3]).shape     #TensorShape([4,784,3]), "-1" means unknown number, =(4*784*3)/(4*3)

#view3: [batch,pixels], there is no channel info
tf.reshape(a, [4,784*3]).shape    #TensorShape([4,2352])
tf.reshape(a, [4,-1]).shape       #TensorShape([4,2352])

# Reshape is flexible, but might lead to potential bugs!

#2.1 
a = tf.random.normal([4,28,28,3])
tf.reshape(tf.reshape(a,[4,-1]), [4,28,28,3]).shape
tf.reshape(tf.reshape(a,[4,-1]), [4,14,56,3]).shape
tf.reshape(tf.reshape(a,[4,-1]), [4,1,784,3]).shape
```

```py
#3 tf.transpose, change content(改變內容)
a = tf.random.normal((4,3,2,1))  
a.shape                               #TensorShape([4,3,2,1])
a.transpose(a).shape                  #TensorShape([1,2,3,4])
a.transpose(a,perm=[0,1,3,2]).shape   #TensorShape([4,3,1,2])

a = tf.random.normal([4,28,28,3])     #[b,h,w,c]
tf.transpose(a,[0,2,1,3]).shape       #TensorShape([4,28,28,3]), [b,w,h,c]
tf.transpose(a,[0,3,2,1]).shape       #TensorShape([4,3,28,28]), [b,c,w,h]
tf.transpose(a,[0,3,1,2]).shape       #TensorShape([4,3,28,28]), [b,c,h,w]
```

```py
#4 squeeze & expand_dims
# a:[classes, students, classes]
# add school dim: [1,4,35,8]+[1,4,35,8]

a = tf.random.normal([4,35,8])       #[0,1,2]or[-3,-2,-1]
a = tf.expand_dims(a,axis=0).shape   #TensorShape([1,4,35,8]), [add,0,1,2]
a = tf.expand_dims(a,axis=3).shape   #TensorShape([4,35,8,1]), [0,1,2,add]
a = tf.expand_dims(a,axis=-1).shape  #TensorShape([4,35,8,1]), [-3,-2,-1,add]
a = tf.expand_dims(a,axis=-4).shape  #TensorShape([1,4,35,8]), ...

#squeeze dim: only squeeze for shape=1 dim
tf.squeeze(tf.zeros([1,2,1,1,3])).shape #TensorShape([2,3])
tf.zeros([1,2,1,3])
tf.squeeze(0,axis=0).shape              #TensorShape([2,1,3])
tf.squeeze(0,axis=2).shape              #TensorShape([1,2,3])
tf.squeeze(0,axis=-2).shape             #TensorShape([1,2,3])
tf.squeeze(0,axis=-4).shape             #TensorShape([2,1,3])


```


