# tf2 adv
## 16 tensor sort

* sort/argsort
* topk
* top5 acc :collision:

```py
#1 sort, argsort: transform back to original one
a = tf.random.shuffle(tf.range(5))          #array([2,0,3,4,1])
tf.sort(a, diretion="DESCENDING")           #array([4,3,2,1,0])
tf.argsort(a, diretion="DESCENDING")        #array([3,2,0,4,1])

idx = tf.argsort(a, diretion="DESCENDING")
tf.gather(a, idx)                           #array([4,3,2,1,0])

#
a = tf.random.uniform([3,3], maxval=10, dtype=tf.int32)
tf.sort(a)
tf.sort(a, direction="DESCENDING")
idx = tf.argsort(a)

#2 topK
a
res = tf.math.top_k(a,2)
res.indices
res.values

```

```py
#3 topk accurancy
#prob: [0.1, 0.2, 0.3, 0.4], label: [2]
#only consider top1 prediction: [3]
#only consider top2 prediction: [3,2]
#only consider top3 prediction: [3,2,1]

prob = tf.constant([[0.1,0.2,0.7], [0.2,0.7,0.1]])
target = tf.constant([2,0])

k_b = tf.math.top_k(prob,3).indices  #map out 最有可能的位置
k_b = tf.transpose(k_b, [1,0])
target = tf.broadcast_to(target, [3,2])


#for example topk accuracy
def accuracy(output, target, topk=(1,)):   #output: [b,N], target: [b]
    maxk = max(topk)
    batch_size = target.shape[0]

    pred = tf.math.top_k(output, maxk).indices
    pred = tf.transpose(pred, perm=[1,0])
    target_ = tf.broadcast_to(target, pred.shape)
    correct = tf.equal(pred, target_)               #[k,b]

    res = []
    for k in topk:
        correct_k = tf.cast(tf.reshape(correct[:k], [-1]), dtype=tf.float32)
        correct_k = tf.reduce_sum(correct_k)
        acc = float(correct_k / batch_size)
        res.append(acc)

    return res



```