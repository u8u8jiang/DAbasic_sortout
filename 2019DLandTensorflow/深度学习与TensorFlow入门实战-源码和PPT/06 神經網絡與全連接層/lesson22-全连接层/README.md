# Neural Network and Fully Connected Layer
## 22 fully connected layer

* matmul
* neural network
* deep learning
* multi-layer


### recap  
out = f(X@W+b)
out = relu(X@W+b)
![](x%40w%2Bb.png)

### 1. black magic!
h0 = relu(X@W1+b1)
h1 = relu(h0@W2+b2)
out = relu(h1@W1+b3)

### 2. how comes deep learning
- neural network in the 1980s, 3~5 layers
- Deep learning now, n = 1200 layers

* why not popular before?

* heroes: 
Bigdata,  
ReLU: Solve gradient divergece   
Dropout  
BatchNorm 
ResNet: turn 10~20 layers to 100 layers
Initialization  
Caffe/ Tensorflow/ PyTorch


### 3. fully connected layer
```py
x = tf.random.normal([4,784])
net = tf.keras.layers.Dense(512)
out = net(x)

out.shape                         #TensorShape([4,512])
net.kernel.shape, net.bias.shape  #(TensorShape([784,512]), TensorShape([512]))

# 
net = tf.keras.layers.Dense(10)
net.bias             
net.get_weights()    #[]
net.weights          #[]

net.build(input_shape=(None,4))
net.kernel.shape, net.bias.shape  #(TensorShape([4,10]), TensorShape([10]))

net.build(input_shape=(None,20))
net.kernel.shape, net.bias.shape  #(TensorShape([20,10]), TensorShape([10]))

net.build(input_shape=(2,4))
net.kernel.shape, net.bias.shape


# 
net.build(input_shape=(None,20))
net.kernel.shape, net.bias.shape     #(TensorShape([20,10]), TensorShape([10]))
out = net(tf.random.randn((4,12)))
out = net(tf.random.normal((4,20)))
out.shape                            #TensorShape([4,10])

```

### 4. Multi-Layers
keras.Sequential([layer1, layer2, layer3])

```py
x = tf.random.normal([2,3])

model = keras.Sequential([
        keras.layers.Dense(2, activation='relu'),
        keras.layers.Dense(2, activation='relu'),
        keras.layers.Dense(2)
    ])
model.build(input_shape=[None, 4])
model.summary()

# [w1,b1,w2,b2,w3,b3]
for p in model.trainable_variables:
    print(p.name, p.shape)


```