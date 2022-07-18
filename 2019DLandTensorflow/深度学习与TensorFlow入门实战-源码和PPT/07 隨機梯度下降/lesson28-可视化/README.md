# Stochastic Gradient Descent (SGD)
## 28 TensorBoard visualization

* installation  
* curve  
* image visualization

1. installation  
`pip install tensorboard`  

2. principle  
listen logdir  
build summary instance  
fed data into summary instance  

**step1. run listener**  
`tensorboard --logdir logs` in cmd  

**step2. build summary**  
```py
current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = 'log/' + current_time
summary_writer = tf.summary.create_file_writer(log_dir)
```

**step3. fed scalar/image**
```py
#1 scalar
with summary_writer.as_default():
    tf.summary.scalar('loss', float(loss), step=epoch)
    tf.summary.scalar('accuracy', float(train_accuracy), step=epoch)

#2 single image
# get x from (x,y)
sample_img = next(iter(db))[0]
# get first image instance
sample_img = sample_img[0]
sample_img = tf.reshape(sample_img, [1,28,28,1])
with summary_writer.as_default():
    tf.summary.image("Training sample:", sample_img, step=0)

#3 multi-images
val_images = x[:25]
val_images = tf.reshape(val_images, [-1,28,28,1])
with summary_writer.as_default():
    tf.summary.scalar('test-acc', float(loss), step=step)
    tf.summary.image('val-onebyone-images:', val_images, max_outputs=25, step=step)

#or
val_images = tf.reshape(val_images, [-1,28,28])
figure = image_grid(val_images)
tf.summary.image('val-images:' plot_to_image(figure), step=step)


```

complier main.py and watch `localhost:6006`, will see the window different, that the window show result of main.py.
