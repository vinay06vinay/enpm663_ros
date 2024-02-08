#!/usr/bin/env python3

"""
This script initializes a ROS2 node using rclpy, which publishes messages using a custom PublisherNode.
The PublisherNode is defined in the first_package package, and it is responsible for publishing messages
to a topic as defined within its implementation. This script is an entry point for running the publisher node,
setting it up, spinning it to keep it alive and processing data, and properly shutting it down afterwards.
"""

import rclpy  # Import ROS Client Library for Python
from first_package.publisher_node import (
    PublisherNode,
)  # Import the custom PublisherNode class


def main(args=None):
    """
    Main function to initialize and run the ROS2 publisher node.

    Args:
        args (list, optional): Command-line arguments passed to the node. Defaults to None.
    """
    rclpy.init(args=args)  # Initialize the ROS client library
    node = PublisherNode("help_pub_py")  # Create an instance of the PublisherNode
    rclpy.spin(node)  # Keep the node alive to listen for incoming data or events
    node.destroy_node()  # Properly destroy the node once it's no longer needed
    rclpy.shutdown()  # Shutdown the ROS client library


if __name__ == "__main__":
    main()  # Execute the main function when the script is run
