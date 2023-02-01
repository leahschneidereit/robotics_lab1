#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import turtlesim.msg/Pose for control commands
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

# import new message from package
from robotics_lab1.msg import Turtlecontrol

current_pose = Pose()
des_position = Turtlecontrol()
kp = 0.0

def pose_callback(pose):
	global current_pose
	current_pose = pose

def des_position_callback(des_position_msg):	
	global des_position
	des_position = des_postion_msg


if __name__ == "__main__":
	#initialize node
	rospy.init_node('control_node', anonymous = True)
	
	#create publisher 
	vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	
	# add subscriber to read position information 
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	# add second subscriber and create new topic
	rospy.Subscriber('turtle1/control_params', Turtlecontrol, des_position_callback)
	
	
	#set a 10Hz frequency for loop
	loop_rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		vel_cmd = Twist()
		
		error = des_position.xd - current_pose.x
		vel_cmd.linear.x = des_position.kp * error
		
		vel_pub.publish(vel_cmd)
		
		loop_rate.sleep()
		
		
		

		
		
		
		




