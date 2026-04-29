#### instructions
add "other_models" and "canadarm_description" to ${ROS2_WORKSPACE_NAME}/src

##### other_models package  
`colcon build`  
`source install/setup.bash`  
`ros2 launch other_models other_models.launch.py`  

change launch file as needed. current urdf models in folder:  
SSRMS_Canadarm [1] (default in launch file)  
SSRMS_Canadarm2 [1]  
ETSVII [1]  

sources  
[1] https://github.com/vyas-shubham/TraceableRobotModels/tree/master

##### canadarm_description package  
mirrored from space ros demos  

install urdf-launch  
`sudo apt install ros-jazzy-urdf-launch`  
`colcon build`
`source install/setup.bash`  
`ros2 launch canadarm_description robodescript_rviz_working.launch.py`  

source  
[1] https://github.com/space-ros/demos/tree/main/canadarm2  

#### SPACEROS!

##### installing earthly

`sudo /bin/sh -c 'wget https://github.com/earthly/earthly/releases/latest/download/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly && /usr/local/bin/earthly bootstrap --with-autocomplete'` 

[source: https://web.archive.org/web/20251116212638/https://earthly.dev/get-earthly]

##### test

`earthly github.com/earthly/hello-world+hello`  

##### setting up spaceros

`mkdir spaceros_ws`  
`cd spaceros_ws`  
`git clone https://github.com/space-ros/space-ros`  
`earthly +dev-image` [for me, ~10 min]  
`earthly +main-image` [5 min]

##### setting up moveit for spaceros

`docker pull osrf/space-ros-moveit2:latest`  
`cd spaceros_ws`  
`git clone https://github.com/space-ros/docker` [avoids building from binary ./build.sh -> crashed my Xorg 2 times bc I ran out of system memory before I gave up]  
`cd docker/moveit2`  
`./run.sh`  

##### canadarm demo 
build image:  
`cd ~/spaceros/docker/moveit2`  
`git clone https://github.com/space-ros/demos`  
`cd demos`  
`cd space_robots`  
`./build.sh`  

run image:  
`./run.sh`  

in demo container:  
`ros2 launch canadarm_demo canadarm.launch.py`  

##### ros-Trick demo
build image:  
`cd ~/spaceros/docker/moveit2/demos/ros_trick`  
`./build.sh`  

run image:  
`xhost +local:docker`  
`./run.sh`  

connecting to container from another terminal:  
`docker exec -it canadarm_ros_trick_demo bash`  
`source install/setup.bash && ros2 launch trick_canadarm_moveit_config moveit_rviz.launch.py`  

[source: https://github.com/space-ros/demos/blob/main/ros_trick/README.md]

##### other notes

###### connecting another terminal to an already running docker container

`docker container list`  
from output, get CONTAINER ID / CONTAINER NAME  
`docker exec -it CONTAINER ID OR CONTAINER NAME /bin/bash --init-file "install/setup.bash"`  
