# Kears metrics API
## 30 keras metrics API

## keras != tf.keras 
keras -> tf.maimoid, torch.maimoid  
The packages often top use in keras.   
* datasets  
* layers  
* losses  
* metrics :star:  
* optimizers  

## 1. metrics 計算loss 
* metrics
* update_state  
* result().numpy()
* reset_states
`metrics.py`

```py
#step1 build a meter
acc_meter = metrics.Accuracy()
loss_meter = metrics.Mean()

#step2 update data
loss_meter.update_state(loss)
acc_meter.update_state(y, pred)

#step3 get average data
print(step, 'loss:', loss_meter.result().numpy())

print(step, 'Evaluate Acc:', total_correct/total, acc_meter.result().numpy())


#clear buffer
if step % 100 == 0:
    print(step, 'loss:', loss_meter.result().numpy())
    loss_meter.reset_states()

    #evaluate
if step 500 == 0:
    total, total_correct = 0., 0
    acc_meter.reset_states()

```

## 2. Compile & Fit 快捷訓練
* compile: train loss, optimizer, evaluate indeces  
* fit: after compile, standardize training process with "fit"  
* evaluate: test
* predict: predict sample

**(1) Individual loss and optimize**  
```py
# without keras, while training
# forward, caclulate loss, gradient

with tf.GradientTape() as tape:
    # [b,28,28] => [b,784]
    x = tf.reshape(x, (-1, 28*28))
    # [b,784] => [b,10]
    out = network(x)
    # [b] => [b,10]
    y_onehot = tf.one_hot(y, depth=10)
    # [b]
    loss = tf.reduce_mean(tf.losses.categorical_crossentropy(y_onehot, out, from_logits=True))

grads = tape.gradient(loss, network.trainable_variables)
optimizer.apply_gradients(zip(grads, network.trainable_variables))
```


**(2) Individual epoch and step**  
```py
for epoch in range(epochs):
    for step, (x,y) in enumerate(db):
        ...
```


**(3) Individual evaluation**
```py
if step % 500 == 0:
    total, total_correct = 0.,0

    for step, (x, y) in enumerate(ds_val): 
        # [b, 28, 28] => [b, 784]
        x = tf.reshape(x, (-1, 28*28))
        # [b, 784] => [b, 10]
        out = network(x) 

        # [b, 10] => [b] 
        pred = tf.argmax(out, axis=1) 
        pred = tf.cast(pred, dtype=tf.int32)
        # bool type 
        correct = tf.equal(pred, y)
        # bool tensor => int tensor => numpy
        total_correct += tf.reduce_sum(tf.cast(correct, dtype=tf.int32)).numpy()
        total += x.shape[0]

    print(step, 'Evaluate Acc:', total_correct/total)
```

**:japanese_goblin:Now**  
```py
#1 loss and optimize*
network.compile(optimizer=optimizers.Adam(lr=0.01),
    loss=tf.losses.CategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
    )


#2 epoch and step
network.fit(db, epochs=10, validation_data=ds_val, validation_freq=2)
#3 evaluation
network.evaluate(ds_val) #test

#4 predict
sample = next(iter(ds_val))
x = sample[0], y = sample[1]  #onehot
pred = network.predict(x)     #[b,10]
# convert back to number
y = tf.argmax(y, axis=1)
pred = tf.argmax(pred, axis=1)

print(pred)
print(y)

```

## 3. auto-def network 自定義層

* keras.Sequential
* keras.layers.Layer
* keras.Model

**(1) keras.Sequential**
```py
# use sequential container to collect all of coff., [w1,b1,w2,b2...], transfer to the layer backward coveniently, 

network = Sequential([layers.Dense(256, activation='relu'),
                     layers.Dense(128, activation='relu'),
                     layers.Dense(64, activation='relu'),
                     layers.Dense(32, activation='relu'),
                     layers.Dense(10)])
network.build(input_shape=(None, 28*28))
network.summary()
```

* model.trainable_variables
* model.call()
  
  
**(2) layer/model**

* inherit from `keras.layers.Layer`, `keras.Model`
* `__init__`
* `call`: `model.__call__()`
* Model: compile, fit, evaluate  

model的概念較大，layer的概念較小，  
model可以繼承layer，使用compile and fit的功能。  


```py
class MyDense(layers.Layer):

    def __int__(self, inp_dim, outp_dim):
        super(MyDense, self).__init__()

        self.kernel = self.add_variable('w', [inp_dim, outp_dim])
        self.bias = self.add_variable('b', [outp_dim])
    
    def call(self, inputs, training=None):
        out = input @ self.kernel + self.bias

        return out


class MyModel(keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = MyDense(28*28, 256)
        self.fc2 = MyDense(256, 128)
        self.fc3 = MyDense(128, 64)
        self.fc4 = MyDense(64, 32)
        self.fc5 = MyDense(32, 18)

    def call(self, inputs, training=None):
        x = self.fc1(inputs)
        x = tf.nn.relu(x)
        x = self.fc2(x)
        x = tf.nn.relu(x)
        x = self.fc3(x)
        x = tf.nn.relu(x)
        x = self.fc4(x)
        x = tf.nn.relu(x)
        x = self.fc5(x)
        return x

```


