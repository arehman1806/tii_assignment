import glob
import os
from setuptools import setup

package_name = 'ros_gazebo'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'maps'), ['ros_gazebo/maps/turtle_bot_waffle_pi_world.model']),
        (os.path.join('share', package_name, 'rviz'), ['ros_gazebo/rviz/nav2_gazebo.rviz']),
        (os.path.join('share', package_name, 'launch'), [
            'ros_gazebo/launch/digital_twin_slam.py',
            'ros_gazebo/launch/turtlebot3_world.launch.py',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Unity Robotics',
    maintainer_email='unity-robotics@unity3d.com',
    description='Unity Robotics Nav2 SLAM Example',
    license='Apache 2.0',
    tests_require=['pytest']
)
