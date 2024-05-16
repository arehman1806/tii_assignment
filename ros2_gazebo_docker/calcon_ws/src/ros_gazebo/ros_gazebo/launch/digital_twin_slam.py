import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'ros_gazebo'
    package_dir = get_package_share_directory(package_name)
    rviz_config_file = os.path.join(package_dir, 'rviz', 'nav2_gazebo.rviz')

    return LaunchDescription([
        # Environment variable settings

        # Launch Navigation2 with namespace
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'navigation_launch.py')
            ),
            launch_arguments={
                'use_sim_time': 'true',
            }.items()
        ),

        # Launch SLAM Toolbox with namespace
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('slam_toolbox'), 'launch', 'online_async_launch.py')
            ),
            launch_arguments={
                'use_sim_time': 'true',
            }.items()
        ),

        # Launch Gazebo world without namespace
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('ros_gazebo'), 'launch', 'turtlebot3_world.launch.py')
            ),
        ),

        # Launch RViz
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file],
            parameters=[{'use_sim_time': True}]
        ),
    ])
