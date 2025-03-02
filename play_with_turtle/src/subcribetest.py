#!/usr/bin/python3

import rospy 
from turtlesim.msg import Pose
import math 

def callback(msg):
    rs = math.sqrt(msg.x**2 + msg.y**2)
    rospy.loginfo("[GET_POS] DISTANCE: (%.2f)" % rs)

    if msg.x <= 0.4 or msg.x >= 10.6 or msg.y <= 0.4 or msg.y >= 10.6:
        rospy.loginfo("[GET_POSE] Turtle almost hit the wall")

if __name__=="__main__":
    rospy.init_node('get_position_node')
    rospy.Subscriber('/turtle1/pose',Pose,callback,queue_size=10)
    rospy.spin()