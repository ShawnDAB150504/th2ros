#!/usr/bin/python3

import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from th2.msg import complex
from turtle_service.srv import cplx_service, cplx_serviceResponse

pose = None

def pose_callback(msg):
    global pose 
    pose = msg 

def move_to_goal(req):
    global pose 
    rospy.loginfo(f"Received goal: x={req.x.re}, y={req.y.re}")

    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.wait_for_message('/turtle1/pose', Pose)

    rate = rospy.Rate(10)
    success = False

    while not rospy.is_shutdown():
        if pose is None: 
            continue

        error_x = req.x.re - pose.x
        error_y = req.y.re - pose.y
        distance = math.sqrt(error_x**2 + error_y**2)

        if distance < 0.1: 
            success = True
            rospy.loginfo("Goal reached. Stopping turtle.")
            break 

        angletogoal = math.atan2(error_x, error_y)
        angleerror = angletogoal - pose.theta

        cmd = Twist()
        cmd.linear.x = min(1.0, distance)  
        cmd.angular.z = min(2.0, angleerror) 

        pub.publish(cmd)
        rate.sleep()

    stop_cmd = Twist()
    pub.publish(stop_cmd)
    rospy.sleep(1) 

    return cplx_serviceResponse(success=success)
    
def move_to_goal_server():
    rospy.init_node('move_to_goal_server')
    service = rospy.Service('move_to_goal', cplx_service, move_to_goal)
    rospy.loginfo("Service move_to_goal ready")
    rospy.spin()
    
if __name__ == "__main__":
    move_to_goal_server()
