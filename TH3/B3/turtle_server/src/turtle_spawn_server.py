#!/usr/bin/python3

import rospy
from turtlesim.srv import Spawn
from turtle_server.srv import turtle_service, turtle_serviceResponse

def spawn_turtle(req):
    rospy.wait_for_service('/spawn')
    try:
        spawn_routine = rospy.ServiceProxy('/spawn', Spawn)

        spawned_turtles = []

        # Spawn rùa 1
        response1 = spawn_routine(req.x1, req.y1, req.z1, req.name1)
        rospy.loginfo(f"Spawned {req.name1} at ({req.x1}, {req.y1})")
        spawned_turtles.append(req.name1)

        # Spawn rùa 2
        response2 = spawn_routine(req.x2, req.y2, req.z2, req.name2)
        rospy.loginfo(f"Spawned {req.name2} at ({req.x2}, {req.y2})")
        spawned_turtles.append(req.name2)

        # Cập nhật danh sách rùa vào parameter server
        rospy.set_param('/spawned_turtles', spawned_turtles)

        return turtle_serviceResponse(True, "Successfully spawned both turtles")

    except Exception as e: 
        return turtle_serviceResponse(False, "Failed to spawn: " + str(e))

if __name__ == "__main__":
    rospy.init_node("spawn_turtle_server")
    service = rospy.Service("spawn_turtles", turtle_service, spawn_turtle)
    rospy.loginfo("Spawn Turtle Service is ready")
    rospy.spin()
