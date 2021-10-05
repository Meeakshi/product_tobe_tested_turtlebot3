#!/usr/bin/env python

from tf.transformations import *

q_orig = quaternion_from_euler(0, 0, 0)
q_rot = quaternion_from_euler(pi, 0, 0)
q_new = quaternion_multiply(q_rot, q_orig)
print q_new
