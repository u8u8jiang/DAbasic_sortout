# tf2 basic
## 09 indexing and gather

### Index
1. basic indexing: [idx][idx][idx]
2. same with numpy
3. `start:end`
4. `start:end:step`
5. `...`


```py
#1 basic indexing
a = tf.ones([1,5,5,3])
a[0][0]
a[0][0][0]
a[0][0][0][2]

#2 numpy-style indexing
a = tf.random.normal([4,28,28,3])   #seen as 4 images, 28*28, 彩色照片
a[1].shape        #tensorshape([28,28,3])
a[1,2].shape      #tensorshape([28,3])
a[1,2,3].shape    #tensorshape([3]), the 2nd image, the 3rd col and the 4th row element
a[1,2,3,2].shape  #tensorshape([]), the 2nd image, the 3rd col and the 4th row element, the 3rd channel, might be a number in [0,255]

#3 `start:end`, [A:B), is vector
a = tf.range(10)
a[-1:]  #array([9])
a[-2:]  #array([8,9])
a[:2]   #array([0,1])
a[:-1]  #array([0,1,2,3,4,5,6,7,8])

#3.1 indexing by `:`
a = tf.random.normal([4,28,28,3]) 
a.shape            #TensorShape([4,28,28,3])
a[0].shape         #TensorShape([28,28,3])
a[0,:,:,:].shape   #TensorShape([28,28,3])
a[0,1,:,:].shape   #TensorShape([28,3])
a[:,:,:,0].shape   #TensorShape([4,28,28]), R channel
a[:,:,:,2].shape   #TensorShape([4,28,28]), B channel
a[:,0,:,:].shape   #TensorShape([4,28,3])

#4 indexing by `::`, means `start:end:step`
# originally, `:`=`::1`, here step=1
a.shape                      #TensorShape([4,28,28,3])
a[0:2,:,:,:].shape           #TensorShape([2,28,28,3])
a[:,0:28:2,0:28:2,:].shape   #TensorShape([4,14,14,3])
a[:,:14,:14,:].shape         #TensorShape([4,14,14,3])
a[:,14:,14:,:].shape         #TensorShape([4,14,14,3])
a[:,::2,::2,:].shape         #TensorShape([4,14,14,3])
a[:,2:26:2,::2,:].shape      #TensorShape([4,12,14,3])

#4.1 `::-1`
a = tf.range(4)   #array([0,1,2,3])
a[::-1]           #array([3,2,1,0])
a[::-2]           #array([3,1])
a[2::-2]          #array([2,0])

#5. `...`
a = tf.random.normal([2,4,28,28,3])   #2:task
a[0].shape            #TensorShape([4,28,28,3])
a[0,:,:,:,:].shape    #TensorShape([4,28,28,3])
a[0,...].shape        #TensorShape([4,28,28,3]), the meaning same as below,
a[:,:,:,:,0].shape    #TensorShape([2,4,28,28])
a[...,0].shape        #TensorShape([2,4,28,28])
a[0,...,2].shape      #TensorShape([4,28,28])
a[1,0,...,0].shape    #TensorShape([28,28])

```

### Selective indexing
1. tf.gather
2. tf.gather_nd
3. tf.boolean_mask

```py
#1 tf.gather
# such as data:[classes, students, subjects]= [4,35,8]
tf.gather(a, axis=0, indices=[2,3]).shape         #TensorShape([2,35,8])
a[2:4].shape                                      #TensorShape([2,35,8])
tf.gather(a, axis=0, indices=[2,1,3,0]).shape     #TensorShape([4,35,8]), random sampling the four classes
tf.gather(a, axis=1, indices=[2,3,7,9,16]).shape  #TensorShape([4,5,8]), selecting the five of students
tf.gather(a, axis=2, indices=[2,3,7]).shape       #TensorShape([4,35,3]), selecting the three of subjectes



# Q.what if sample several students and their several subjects?
#2 th.gather_nd: select the specific location
a.shape                            #TensorShape([4,35,8])
tf.gather_nd(a, [0]).shape         #TensorShape([35,8]), the 0 class
tf.gather_nd(a, [0,1]).shape       #TensorShape([8])
tf.gather_nd(a, [0,1,2]).shape     #TensorShape([])
tf.gather_nd(a, [[0,1,2]]).shape   #TensorShape([1])

a.shape                                            #TensorShape([4,35,8])
tf.gather_nd(a, [[0,0], [1,1]]).shape              #TensorShape([2,8]), 0class&0student, 1class&1student
tf.gather_nd(a, [[0,0],[1,1],[2,2]]).shape         #TensorShape([3,8]), 0class&0student, 1class&1student, 2class&2student
tf.gather_nd(a, [[0,0,0],[1,1,1],[2,2,2]]).shape   #TensorShape([3]), [[3],[3],[3]]-> [3]
tf.gather_nd(a, [[[0,0,0],[1,1,1],[2,2,2]]]).shape #TensorShape([1,3]), [[98,42,100]]-> [1,3]


#3 tf.boolean_mask
a.shape                                                 #TensorShape([4,28,28,3])
tf.boolean_mask(a, mask=[True,True,False,False]).shape  #TensorShape([2,28,28,3]), task1 open, task2 open, task3 close, task4 close
tf.boolean_mask(a, mask=[True,True,False], axis=3).shape #TensorShape([4,28,28,2]), channel1-R open, channel2-G open, channel-B close

a = tf.ones([2,3,4])
tf.boolean_mask(a, mask=[[True,False,False], [False,True,True]])

```