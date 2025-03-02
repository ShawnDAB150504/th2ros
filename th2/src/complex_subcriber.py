#!/usr/bin/python3

import rospy
from th2.msg import complex

def callback(msg):
    rospy.loginfo(f"Received: {msg.re} + {msg.im}j")

def listener():
    rospy.init_node('complex_subscriber', anonymous=True)
    rospy.Subscriber('complex_topic', complex, callback)
    rospy.spin()

if __name__== '_main_':
    listener()