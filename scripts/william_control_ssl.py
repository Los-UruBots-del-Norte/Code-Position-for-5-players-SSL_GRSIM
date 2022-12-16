#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import *
from gazebo_msgs.msg import *
from grsim_ros_bridge_msgs.msg import *
from krssg_ssl_msgs.msg import *
import math

pelota = Pose()
robot0 = SSL_DetectionRobot()
robot1 = SSL_DetectionRobot()
robot2 = SSL_DetectionRobot()
robot3 = SSL_DetectionRobot()
robot4 = SSL_DetectionRobot()

def position_ball(data):
	global pelota		
	pelota = data.balls
	
def jugador_blue(data):
	global robot0,robot1,robot2,robot3,robot4
				
	for i in range(0, len(data.robots_blue)):
		id_robots = data.robots_blue[i].robot_id
		if id_robots == 0:
			robot0 = data.robots_blue[i]
		if id_robots == 1:
			robot1 = data.robots_blue[i]
		if id_robots == 2:
			robot2 = data.robots_blue[i]
		if id_robots == 3:
			robot3 = data.robots_blue[i]
		if id_robots == 4:
			robot4 = data.robots_blue[i]
			
if __name__=="__main__":
	rospy.init_node("william_node", anonymous=False)
	
	rospy.Subscriber("/vision", SSL_DetectionFrame, position_ball)
	rospy.Subscriber("/vision", SSL_DetectionFrame, jugador_blue)
	
	r = rospy.Rate(10)
	goaly= 500
	goalx= 500
	while not rospy.is_shutdown():
   		goal_angle = math.atan2(goaly - robot0.y, goalx - robot0.x)
   	
   		
   		
   		
   		
   		
   		
   		
   		
   		
   		
   		
   		
   		
   		
   		
   		r.sleep()
