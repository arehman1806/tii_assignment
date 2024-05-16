#!/bin/bash

# Function to display the help message
display_help() {
    echo "Usage: $0 POSITION_X POSITION_Y ORIENTATION_Z"
    echo
    echo "Publish a goal pose to Unity and Gazebo simulations."
    echo
    echo "Arguments:"
    echo "  POSITION_X       X coordinate of the goal position"
    echo "  POSITION_Y       Y coordinate of the goal position"
    echo "  ORIENTATION_Z    Z orientation (in degrees) of the goal position. The script automatically converts 00Y->Quaternion"
    echo
    exit 0
}

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    display_help
fi

if [ "$#" -ne 3 ]; then
    echo "Error: Incorrect number of arguments."
    echo "Use -h or --help for usage information."
    exit 1
fi

POSITION_X=$1
POSITION_Y=$2
ORIENTATION_Z=$3

# Convert the Z orientation to radians
ORIENTATION_Z_RAD=$(echo "$ORIENTATION_Z * 0.01745329252" | bc -l)

# Calculate the quaternion from the Z orientation
ORIENTATION_W=$(echo "c($ORIENTATION_Z_RAD / 2)" | bc -l)
ORIENTATION_Z_QUAT=$(echo "s($ORIENTATION_Z_RAD / 2)" | bc -l)

# Get the current time for the message header in seconds and nanoseconds
CURRENT_TIME=$(date +%s)
CURRENT_NANOSEC=$(date +%N)

UNITY_CONTAINER_NAME="unity_simulation"
GAZEBO_CONTAINER_NAME="gazebo_digital_twin_simulation"

ROS2_SETUP_CMD="source /opt/ros/galactic/setup.bash"
BASH_CMD="source ~/.bashrc && $ROS2_SETUP_CMD && ros2 topic pub /goal_pose geometry_msgs/PoseStamped \"{header: {stamp: {sec: $CURRENT_TIME, nanosec: ${CURRENT_NANOSEC:0:9}}, frame_id: 'map'}, pose: {position: {x: $POSITION_X, y: $POSITION_Y, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: $ORIENTATION_Z_QUAT, w: $ORIENTATION_W}}}\" -1"

# Publish to Unity simulation container
docker exec $UNITY_CONTAINER_NAME bash -c "$BASH_CMD" &
UNITY_PID=$!

# Publish to Gazebo container
docker exec $GAZEBO_CONTAINER_NAME bash -c "$BASH_CMD" &
GAZEBO_PID=$!

# Wait for both background processes to finish
wait $UNITY_PID
wait $GAZEBO_PID