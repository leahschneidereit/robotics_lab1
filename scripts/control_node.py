#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import turtlesim.msg/Pose for control commands
from turtlesim.msg import Pose

# import geometry_msgs.msg for control commands
from geometry_msgs.msg import Twist

# import new message from package
from robotics_lab1.msg import Turtlecontrol

current_pose = Pose()
des_position = Turtlecontrol()
kp = 0.0

# create callback function for pose subscriber
def pose_callback(pose):
	global current_pose
	current_pose = pose
	
#create callback function for control_param topic
def des_position_callback(des_position_msg):	
	global des_position
	des_position = des_position_msg

#----------main-----------------#
if __name__ == "__main__":
	# initialize node
	rospy.init_node('control_node', anonymous = True)
	
	# create publisher to publish to cmd_vel topic
	vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# add subscriber to read position information 
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	# add second subscriber and create new topic for control params
	rospy.Subscriber('turtle1/control_params', Turtlecontrol, des_position_callback)
	
	#set a 10Hz frequency for loop
	loop_rate = rospy.Rate(10)
	
	# create infinite while loop 
	while not rospy.is_shutdown():
		# set message type for vel_cmd
		vel_cmd = Twist()
		
		# calculate error for current position of turtle bot
		error = des_position.xd - current_pose.x
		
		# calculate desired position 
		vel_cmd.linear.x = des_position.kp * error
		
		# publish linear velocity command to vel_cmd topic
		vel_pub.publish(vel_cmd)
		
		# set loop rate to sleep
		loop_rate.sleep()
		
		
		

		
		
		
		




