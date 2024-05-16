# Use the official ROS2 Foxy base image
FROM osrf/ros:galactic-desktop

# Set environment variables
ENV ROS_DISTRO=galactic
ENV TURTLEBOT3_MODEL=waffle_pi


# Install Nav2 packages
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-turtlebot3* \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-nav2-bringup \
    mesa-utils \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    python3-pip \
    && apt-get clean

# Set up the workspace
WORKDIR /ros2_unity_ws

# Copy the workspace source code
COPY colcon_ws/src src

# Install dependencies and build the workspace
RUN /bin/bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash && \
    apt-get update && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build"


# Add sourcing commands to .bashrc
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc && \
    echo "source /ros2_unity_ws/install/setup.bash" >> /root/.bashrc

# Start a bash session
CMD ["bash"]