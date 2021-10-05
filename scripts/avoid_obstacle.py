#!/usr/bin/env python

import rospy
import random
import unittest
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import test_avoid_obstacle

global flag

def callback(msg):
    print('=====================================')
    laserthreshold1= 0.8
    laserthreshold2= 0.8
      
    print('s2 [0]: front')
    print(msg.ranges[0])
                 
    print('s3 [90]: Left')
    print(msg.ranges[90])

    print('s1 [270]: Right')
    print(msg.ranges[270])
    print('=====================================')

    if msg.ranges[0] > laserthreshold1 and msg.ranges[90] > laserthreshold2 and msg.ranges[270] > laserthreshold2:
        move.linear.x =0.5
        move.angular.z = 0.0
	flag = 0
    else:
        move.linear.x=0.0
        move.angular.z=0.5
	if msg.ranges[0] > laserthreshold1 and msg.ranges[90] > laserthreshold2 and msg.ranges[270] > laserthreshold2:
		move.linear.x =0.5
		move.angular.z = 0.0
        flag = 1
    pub.publish(move)
    	
rospy.init_node('obstacle_avoidance')
sub=rospy.Subscriber('/scan', LaserScan, callback)
pub=rospy.Publisher('/cmd_vel', Twist)
move=Twist()
rospy.spin()

