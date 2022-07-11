# tf2 adv
## 14 Merge and split

* tf.concat: 拼接+   
* tf.split: 分割-  
* tf.stack: 堆疊+  
* tf.unstack: 分割-  


```py
#1 concat
# statistics about scores  
# [class1-4, students, scores]
# [class5-6, students, scores]

a = tf.ones([4,35,8])
b = tf.ones([2,35,8])
tf.concat([a,b], axis=0).shape  #TensorShape([6, 35, 8])

a = tf.ones([4,32,8])
b = tf.ones([4,3,8])
tf.concat([a,b], axis=1).shape  #TensorShape([4, 35, 8])


#2 stack: create new dim
# statistics about scores  
# school1: [classes, students, scores]
# school2: [classes, students, scores]
# [schools, classes, students, scores]


a = tf.ones([4,35,8])
b = tf.ones([4,35,8])
a.shape
b.shape
tf.concat([a,b], axis=-1).shape #TensorShape([4, 35, 16])
tf.stack([a,b], axis=0).shape   #TensorShape([2, 4, 35, 8])
tf.stack([a,b], axis=3).shape   #TensorShape([4, 35, 8, 2])

#dim mismatch
a = tf.ones([4,35,8])
b = tf.ones([3,33,8])
tf.concat([a,b], axis=0)     #invalid

b = tf.ones([2,35,8])
c = tf.concat([a,b], axis=0) #shape=(6,35,8)
tf.stack([a,b], axis=0)      #invalid

#unstack
a.shape                      #TensorShape([4,35,8])
b = tf.ones([4,35,8])
c = tf.stack([a,b])
c.shape                      #TensorShape([2,4,35,8])

aa,bb = tf.unstack(c, axis=0)
aa.shape, bb.shape           #(TensorShape([4,35,8]), TensorShape([4,35,8]))

res = tf.unstack(c, axis=3)  #【2,4,35,8】
res[0].shape, res[7].shape   #(TensorShape([2,4,35]), TensorShape([2,4,35]))

```

```py
#3 split
#stack vs unstack
#after stacking, could unstack and split it 

c.shape                    #TensorShape([2,4,35,8])
res = tf.unstack(c, axis=3)
len(res)  #8

res = tf.split(c, axis=3, num_or_size_splits=2)
len(res)  #2

res[0].shape                #TensorShape([2,4,35,4])
res = tf.split(c, axis=3, num_or_size_splits=[2,2,4])
res[0].shape, res[2].shape  #(TensorShape([2, 4, 35, 2]), TensorShape([2, 4, 35, 4]))

```




