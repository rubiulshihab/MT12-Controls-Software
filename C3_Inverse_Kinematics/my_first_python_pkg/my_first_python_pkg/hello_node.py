import rclpy
from rclpy.node import Node

class my_node(Node):
    
    def __init__(self):
        super().__init__('hello_node')
        self.get_logger().info('hello! my first ROS 2 node is running')


def main(args = None):
    rclpy.init(args = args)
    node = my_node()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()



if __name__ == "__main__":
    main()