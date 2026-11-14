import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from my_first_python_pkg.kinematics_math import inverse_kinematics




class InverseKinematicsNode(Node):
    def __init__(self):
        super().__init__("inverse_kinematics_node")
        self.L1 = 14.0
        self.L2 = 15.5

        self.pub_ = self.create_publisher(Vector3, '/miniarm/angles', 10)
        self.create_subscription(Vector3, '/miniarm/target' , self.target_callback, 10)
        self.get_logger().info("Inverse Kinematics Node Started")

    def target_callback(self, msg):
        try: 
            servo1, servo2 = inverse_kinematics(msg.x, msg.y, self.L1, self.L2)

        except ValueError as e:
            self.get_logger().warning(str(e)) #warning
            return

        output = Vector3()
        output.x = float(servo1)
        output.y = float(servo2)
        output.z = 0.0

        self.pub_.publish(output)
        self.get_logger().info(f'Target: ({msg.x:.2f},{msg.y:.2f})\n Angles: ({servo1:.2f},{servo2:.2f})')




def main(args = None):
    rclpy.init(args = args)

    node = InverseKinematicsNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()