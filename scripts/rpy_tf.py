#!/usr/bin/env python

from tf.transformations import *

pi=3.14

q_orig = quaternion_from_euler(0, 0, 0)
q_rot = quaternion_from_euler(pi, 0, 0)
q_new = quaternion_multiply(q_rot, q_orig)
print q_new


q1_inv[0] = prev_pose.pose.orientation.x
q1_inv[1] = prev_pose.pose.orientation.y
q1_inv[2] = prev_pose.pose.orientation.z
q1_inv[3] = -prev_pose.pose.orientation.w # Negate for inverse

q2[0] = current_pose.pose.orientation.x
q2[1] = current_pose.pose.orientation.y
q2[2] = current_pose.pose.orientation.z
q2[3] = current_pose.pose.orientation.w

qr = tf.transformations.quaternion_multiply(q2, q1_inv)
print qr
