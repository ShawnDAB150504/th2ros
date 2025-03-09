#!/usr/bin/python3

import rospy
from th2.msg import complex
from turtle_service.srv import cplx_service, cplx_serviceRequest

def move_to_goal_client():
    rospy.wait_for_service('move_to_goal')
    move_to_goal = rospy.ServiceProxy('move_to_goal', cplx_service)
    
    while not rospy.is_shutdown():
        try:
            x = float(input("Nhập tọa độ x: "))
            y = float(input("Nhập tọa độ y: "))
            
            goal_x = complex(re=x)
            goal_y = complex(re=y) 
            
            response = move_to_goal(goal_x, goal_y)
            rospy.loginfo(f"Sent goal: x={x}, y={y}")
            rospy.loginfo(f"Success: {response.success}")
            
            if response.success:
                rospy.loginfo("Rùa đã đến đúng vị trí. Thoát chương trình.")
                break  

        except ValueError:
            rospy.logerr("Vui lòng nhập số hợp lệ.")
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed: {e}")

    rospy.signal_shutdown("Goal reached, shutting down client.")  # Dừng client

if __name__ == "_main_":  
    rospy.init_node('move_to_goal_client')
    move_to_goal_client()