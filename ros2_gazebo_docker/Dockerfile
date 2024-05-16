# Galactic full
FROM osrf/ros:galactic-desktop

# Set environment variables
ENV ROS_DISTRO=galactic
ENV TURTLEBOT3_MODEL=waffle_pi
ENV ROS_DOMAIN_ID=11

# Nav2 packages
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-nav2-bringup \
    ros-${ROS_DISTRO}-gazebo-ros-pkgs \
    gazebo11 \
    mesa-utils \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    python3-pip \
    && apt-get clean


# required for building turtlebot3_gazebo package
RUN pip3 install catkin_pkg


# Set up the workspace
WORKDIR /ros2_gazebo_ws

# Copy the workspace source code
COPY calcon_ws/src src

# Build the workspace
RUN /bin/bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash && \
    apt-get update && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build"

# Add sourcing commands to .bashrc
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc && \
    echo "source /ros2_gazebo_ws/install/setup.bash" >> /root/.bashrc && \
    echo "export ROS_DOMAIN_ID=${ROS_DOMAIN_ID}" >> /root/.bashrc

# Start a bash session
CMD ["bash"]
