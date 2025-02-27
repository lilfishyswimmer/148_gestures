#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import cv2

# Import the hand tracker classes (make sure these modules are available in your PYTHONPATH)
from HandTrackerRenderer import HandTrackerRenderer
from HandTrackerEdge import HandTracker

class GestureTracker(Node):
    def __init__(self):
        super().__init__('gesture_tracker')
        self.publisher_ = self.create_publisher(Bool, 'hand_gesture/thumb_up', 10)
        self.get_logger().info("Hand Tracker Node Started")

        # Initialize the hand tracker and renderer
        # Pass your own arguments/configuration to HandTracker as needed
        self.tracker = HandTracker(
            # ... add any required parameters here ...
        )
        self.renderer = HandTrackerRenderer(tracker=self.tracker)

    def run_tracker(self):
        """Main loop to process frames and publish gesture status."""
        try:
            while True:
                # Grab the next frame and hand data
                frame, hands, bag = self.tracker.next_frame()
                if frame is None:
                    break

                # Draw hand landmarks and other info on the frame for debugging
                frame = self.renderer.draw(frame, hands, bag)

                # Check if any detected hand shows a 'thumb up' gesture
                thumb_up_detected = any(self.is_thumb_up(hand) for hand in hands)
                msg = Bool()
                msg.data = thumb_up_detected
                self.publisher_.publish(msg)
                self.get_logger().info(f"Published thumb_up: {thumb_up_detected}")

                # Display the frame (optional, for debugging)
                key = self.renderer.waitKey(delay=1)
                if key == 27 or key == ord('q'):
                    break

        finally:
            self.renderer.exit()
            self.tracker.exit()

    def is_thumb_up(self, hand):
        """
        Determine if the provided hand data corresponds to a 'thumb up' gesture.
        This is a placeholder function.
        Adjust the landmark indices and logic according to your hand tracker's data structure.
        """
        # For example, assume that 'hand' is a dictionary with key 'landmarks',
        # and that the landmarks follow a known convention (e.g., MediaPipe).
        landmarks = hand.get('landmarks', [])
        if len(landmarks) < 5:
            return False

        # Example: If landmark[4] (thumb tip) is above landmark[2] (thumb base) in image coordinates,
        # consider it a thumb up. Adjust the indices and comparison as needed.
        if landmarks[4].y < landmarks[2].y:
            return True
        return False

def main(args=None):
    rclpy.init(args=args)
    node = GestureTracker()
    try:
        node.run_tracker()
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard Interrupt, shutting down.")
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

