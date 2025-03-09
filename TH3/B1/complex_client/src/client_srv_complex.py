#!/usr/bin/python3

import rospy
from complex_client.msg import complex_num
from complex_service.srv import addComplex, addComplexRequest
import random

def add_complex_client(complex1, complex2):
    rospy.wait_for_service('add_complex_srv')
    try:
        add_complex = rospy.ServiceProxy('add_complex_srv',addComplex) # tao ra giao thuc ket noi cho service
        req = addComplexRequest() # create request instance

        req.input1 = complex1 # instance request co 2 tham so la input1 va input2
        req.input2 = complex2

        res = add_complex(req)

        return res.output
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s " % e)
        return None
