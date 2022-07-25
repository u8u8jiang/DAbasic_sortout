# Kears metrics API
## 31 keras model save and load

* save/load weights: there is orginal code, pkl 
* save/load entire model
* saved_model: similar to ONNX of pytorch 使用python作開發，包成save_model後，以在c++的工廠環境作使用。

**1. save the weights**
```py
# save the weights
model.save_weights('./checkpoints/my_checkpoint')

# Restore the weights
model = create_model()
model.load_weights('./checkpoints/my_checkpoint')

loss, acc = model.evaluate(test_images, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))
```

```py
# after training, save and delete the par.
network.save_weights('weights.ckpt')
print('saved weights.')
del network

network = Sequential([layers.Dense(256, activation='relu'),
                    layers.Dense(128, activation='relu'),
                    layers.Dense(64, activation='relu'),
                    layers.Dense(32, activation='relu'),
                    layers.Dense(10)])
network.compile(optimizer=optimizers.Adam(lr=0.01),
                loss=tf.losses.CategoricalCrossentropy(from_logits=True),
                metrices=['accuracy']
        )
network.load_weights('weights.ckpt')
network.evaluate(ds_val)

```

`save_load_weight.py`

**2. save the entire model**

```py
network.save('model.h5')
print('saved total model.')
del network

print('load model from file')
network = tf.keras.models.load_model('model.h5')

network.evaluate(x_val, y_val)
```
`save_load_model.py`


**3. saved_model save/load**

```py
tf.saved_model.save(m, '/tmp/saved_model/')

imported = tf.saved_model.load(path)
f = imported.signatures["serving_default"]
print(f(x=tf.ones([1,28,28,3])))

```



