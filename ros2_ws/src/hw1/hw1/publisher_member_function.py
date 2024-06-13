import rclpy
from rclpy.node import Node

from std_msgs.msg import String

# Use this https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        # Fill the create_publisher function
        self.publisher_ = self.create_publisher(String, 'hw1/partb/topic', 10)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Fill this function such that msg.data should have your name and publish it.
        msg = String()
        msg.data = 'Hello %s' % "Mr. Aakash Chowhan Mood"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
