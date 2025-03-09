#!/usr/bin/python3

import rospy
from complex_client.msg import complex_num
from complex_service.srv import addComplex, addComplexResponse

def add_complex(request):
    rs = complex_num()
    rs.real = request.input1.real + request.input2.real
    rs.imaginary = request.input1.imaginary + request.input2.imaginary  # Fixed typo
    return addComplexResponse(rs)

if __name__ == "__main__":
    rospy.init_node('add_complex_srv')
    service = rospy.Service('addComplex', addComplex, add_complex)
    rospy.loginfo("Service [add_complex_srv] is ready.")
    rospy.spin()
