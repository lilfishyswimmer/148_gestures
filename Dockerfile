# Use the official ROS2 Humble image as the base
FROM ros:humble

# Install required system packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install --no-cache-dir opencv-python depthai

# Create and set the working directory
WORKDIR /root/148_gestures
COPY . /root/148_gestures

# Build the ROS2 package
RUN . /opt/ros/humble/setup.sh && colcon build --symlink-install

# Set the entrypoint to source ROS2 and the workspace, then launch the nodes
CMD ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash && source install/setup.bash && ros2 launch launch/gestures_launch.py"]

