#!/usr/bin/python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

turtle_names = []

def pose_callback(pose, turtle_name):
    cmd_vel = Twist()

    # Nếu rùa chạm biên, nó quay lại
    if pose.x < 1.5 or pose.x > 9.5 or pose.y < 1.5 or pose.y > 9.5:
        cmd_vel.angular.z = 1.5
        cmd_vel.linear.x = 2.0
    else:
        cmd_vel.linear.x = 4.0
    
    pub = rospy.Publisher(f'/{turtle_name}/cmd_vel', Twist, queue_size=10)
    pub.publish(cmd_vel)

def setup_turtle_motion():
    rospy.init_node('turtle_auto')

    global turtle_names
    turtle_names = rospy.get_param('/spawned_turtles', [])

    if not turtle_names:
        rospy.logerr("Không có rùa nào được spawn! Kiểm tra lại service.")
        return

    for turtle in turtle_names:
        rospy.Subscriber(f'/{turtle}/pose', Pose, pose_callback, turtle)

    rospy.spin()

if __name__ == "__main__":
    setup_turtle_motion()
