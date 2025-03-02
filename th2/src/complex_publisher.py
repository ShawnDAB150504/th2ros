#!/usr/bin/python3

import rospy
from th2.msg import complex
import random

def talker():
    pub = rospy.Publisher('complex_topic', complex, queue_size=10)
    rospy.init_node('complex_publisher', anonymous=True)
    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        msg = complex()
        msg.re = random.uniform(-10, 10)
        msg.im = random.uniform(-10, 10)
        rospy.loginfo(f"Publishing: {msg.re} + {msg.im}j")
        pub.publish(msg)
        rate.sleep()

if __name__ == '_main_':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass