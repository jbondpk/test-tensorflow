#!/usr/bin/env python

import os
import tensorflow as tf

print("__file__ " + __file__)
print("[[DIRECTORY CONTENTS]]")
os.system("echo --; pwd 2>&1")
os.system("echo --; cd ..; ls -l; cat requirements.txt")
os.system("echo --; find / -iname 'requirements.txt' 2>/dev/null")
os.system("echo --; find / -iname 'tensorflow-test.py' 2>/dev/null")
os.system("echo --; find /code 2>/dev/null")

import pandas as pd

# Say hello
hello = tf.constant('Hello, TensorWorld!')
# sess = tf.Session()
# Find out which devices are assigned to.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print sess.run(hello)

# Some simple math.
a = tf.constant(10)
b = tf.constant(32)
print sess.run(a+b)
