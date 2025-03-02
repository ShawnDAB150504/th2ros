#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
import sys, termios, tty

# Hàm đọc phím từ bàn phím
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

# Hàm điều khiển rùa
def control():
    rospy.init_node("turtle_teleop_control")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(50)

    vel = Twist()  # Khởi tạo tốc độ
    while not rospy.is_shutdown():
        key = get_key()  # Đọc phím nhấn

        # Nếu có phím nhấn, cập nhật tốc độ
        if key == 'w':
            vel.linear.x = 1  # Di chuyển về phía trước
        elif key == 's':
            vel.linear.x = -1  # Di chuyển lùi
        elif key == 'a':
            vel.angular.z = 1  # Xoay theo chiều ngược chiều kim đồng hồ
        elif key == 'd':
            vel.angular.z = -1  # Xoay theo chiều kim đồng hồ
        elif key == '\x03':  # Ctrl+C để thoát
            break
        elif key == 'x':
            # Nếu không có phím nào được nhấn, dừng con rùa ngay lập tức
            vel.linear.x = 0.0
            vel.angular.z = 0.0

        pub.publish(vel)  # Cập nhật tốc độ cho con rùa ngay lập tức
        rate.sleep()


if __name__ == "__main__":
    try:
        control()
    except rospy.ROSInterruptException:
        pass
