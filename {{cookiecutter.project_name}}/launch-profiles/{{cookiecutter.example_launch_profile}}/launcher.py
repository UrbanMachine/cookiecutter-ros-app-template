"""Launch nodes for this launch profile."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    rviz_config = "/robot/launch-profile/rviz-config.rviz"
    launch_description = [
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", [rviz_config]]
        ),
    ]
    return LaunchDescription(launch_description)
