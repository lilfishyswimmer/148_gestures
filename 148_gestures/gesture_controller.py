#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32

class GestureController(Node):
    def __init__(self):
        super().__init__('gesture_controller')
        self.subscription = self.create_subscription(
            Bool,
            'hand_gesture/thumb_up',
            self.gesture_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher to send a forward command to the VESC.
        self.vesc_pub = self.create_publisher(Float32, 'vesc/commands/forward', 10)
        self.forward_speed = 0.5  # Adjust to match your RC car configuration

    def gesture_callback(self, msg: Bool):
        if msg.data:
            self.get_logger().info("Thumb up detected. Commanding RC car to move forward.")
            forward_msg = Float32()
            forward_msg.data = self.forward_speed
            self.vesc_pub.publish(forward_msg)
        else:
            self.get_logger().info("No thumb up detected. Stopping RC car.")
            stop_msg = Float32()
            stop_msg.data = 0.0
            self.vesc_pub.publish(stop_msg)

def main(args=None):
    rclpy.init(args=args)
    node = GestureController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard Interrupt, shutting down Gesture Controller.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

