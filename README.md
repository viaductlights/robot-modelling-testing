### instructions
add "other_models" to ${ROS2_WORKSPACE_NAME}/src

`colcon build`  
`source install/setup.bash`  
`ros2 launch other_models other_models.launch.py`  

change launch file as needed. current urdf models in folder:  
SSRMS_Canadarm [1] (default in launch file)  
SSRMS_Canadarm2 [1]  
ETSVII [1]  

sources  
[1] https://github.com/vyas-shubham/TraceableRobotModels/tree/master

### SPACEROS!

#### installing earthly

`sudo /bin/sh -c 'wget https://github.com/earthly/earthly/releases/latest/download/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly && /usr/local/bin/earthly bootstrap --with-autocomplete'` 

[source: https://web.archive.org/web/20251116212638/https://earthly.dev/get-earthly]

#### testing earthly

`earthly github.com/earthly/hello-world+hello`  

#### setting up spaceros

`mkdir spaceros_ws`  
`cd spaceros_ws`  
`git clone https://github.com/space-ros/space-ros`  
`earthly +dev-image` [for me, ~10 min]  
`earthly +main-image` [5 min]

#### setting up moveit for spaceros:

`docker pull osrf/space-ros-moveit2:latest`  
`cd spaceros_ws`  
`git clone https://github.com/space-ros/docker` [avoids building from binary ./build.sh -> crashed my Xorg 2 times bc I ran out of system memory before I gave up]  
`cd docker/moveit2`  
`./run.sh`  

#### other notes
next:  
- test canadarm + canadarm2/Trick demos

##### connecting another terminal to an already running docker container

`docker container list`  
from output, get CONTAINER ID / CONTAINER NAME  
`docker exec -it CONTAINER ID OR CONTAINER NAME /bin/bash --init-file "install/setup.bash"`  
