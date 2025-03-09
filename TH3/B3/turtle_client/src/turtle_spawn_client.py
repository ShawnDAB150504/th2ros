import rospy
from turtle_server.srv import turtle_service, turtle_serviceRequest

def spawn_client(): 
    rospy.wait_for_service('spawn_turtles')  # 🔹 Đảm bảo service đã có
    rospy.sleep(1)  # 🔹 Chờ 1 giây để server ổn định
    
    try:
        spawn_turtle = rospy.ServiceProxy('spawn_turtles', turtle_service)

        if not rospy.get_param_names():
            rospy.logerr("Service /spawn_turtles chưa có. Kiểm tra lại server!")
            return

        # Nhập thông tin rùa 1
        x1 = float(input("Nhập X của rùa 1: "))
        y1 = float(input("Nhập Y của rùa 1: "))
        z1 = float(input("Nhập góc quay của rùa 1 (radian): "))
        name1 = input("Nhập tên rùa 1: ")

        # Nhập thông tin rùa 2
        x2 = float(input("Nhập X của rùa 2: "))
        y2 = float(input("Nhập Y của rùa 2: "))
        z2 = float(input("Nhập góc quay của rùa 2 (radian): "))
        name2 = input("Nhập tên rùa 2: ")

        request = turtle_serviceRequest(x1, y1, z1, name1, x2, y2, z2, name2)
        response = spawn_turtle(request)

        if response.success:
            rospy.loginfo("Hai con rùa đã được tạo thành công.")
            rospy.set_param('/spawned_turtles', [name1, name2])  # 🔹 Lưu danh sách rùa
        else:
            rospy.logerr(f"Lỗi spawn rùa: {response.message}")

    except rospy.ServiceException as e:
        rospy.logerr(f"Lỗi khi gọi service: {e}")

if __name__ == "__main__":
    rospy.init_node('spawn_turtle_client')
    spawn_client()
