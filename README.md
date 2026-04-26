##### instructions
add "other_models" to ros2_ws/src

`colcon build`  
`source install/setup.bash`  
`ros2 launch other_models other_models.launch.py`  

change launch file as needed. current urdf models in folder:  
SSRMS_Canadarm [1] (default in launch file)  
SSRMS_Canadarm2 [1]  
ETSVII [1]  

sources  
[1] https://github.com/vyas-shubham/TraceableRobotModels/tree/master
