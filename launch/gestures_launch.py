#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='148_gestures',
            executable='gesture_tracker',
            name='gesture_tracker'
        ),
        Node(
            package='148_gestures',
            executable='gesture_controller',
            name='gesture_controller'
        )
    ])

