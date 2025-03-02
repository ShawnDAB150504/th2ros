#!/usr/bin/python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def pose_callback(pose):
    cmd_vel = Twist()
    if pose.x < 1.0 or pose.x > 10.0 or pose.y < 1.0 or pose.y > 10.0:
        cmd_vel.angular.z = 1.57
        cmd_vel.linear.x = 0.3 
    else:
        cmd_vel.linear.x = 1.0
    
    pub.publish(cmd_vel)

rospy.init_node('turtle_auto')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
rospy.spin()