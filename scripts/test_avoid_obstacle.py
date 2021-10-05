#!/usr/bin/env python

import rospy
import unittest
import xmlrunner
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
#import HtmlTestRunner
import time


#global flag
global runner
class testObstacle(unittest.TestCase):

	def setUp(self):
		print("Running test setup function")
		#out = io.BytesIO()
		#print(out)
		'''front_range = msg.ranges[0]
		left_range = msg.ranges[90]
		right_range = msg.ranges[270]
		back_range = msg.ranges[180]'''

	def test_obstacleavoidance(self):
		print('Start of test')
		#if msg.ranges[0] > laserthreshold1 and msg.ranges[90] > laserthreshold2 and msg.ranges[270] > laserthreshold2 and flag == 1:
		if flag ==1:
			self.assertEqual(1, flag)
			print("Achieved obastcle avoidance")
		else:
			print("No obastcle yet")
		print('End of test')

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
	    global flag
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
	
	    with open('/home/meenakshi/catkin_ws/src/test_simulation/results/results.xml', 'a+') as output:
        	unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), buffer=False) 
	      
#xmlrunner.XMLTestRunner
#unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False, exit=False)
rospy.init_node('obstacle_avoidance')
sub=rospy.Subscriber('/scan', LaserScan, callback)
pub=rospy.Publisher('/cmd_vel', Twist)
move=Twist()
rospy.spin()
#unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/meenakshi/catkin_ws/src/test_simulation/results'))
	
 	
