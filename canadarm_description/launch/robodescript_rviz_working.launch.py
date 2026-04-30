from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Get package paths
    urdf_launch_pkg = FindPackageShare('urdf_launch')
    canadarm_description_share = FindPackageShare('canadarm_description')
    
    # Paths
    default_model_path = PathJoinSubstitution([
        canadarm_description_share, 
        'models', 'urdf', 
        'SSRMS_Canadarm2.urdf.xacro'
    ])
    default_rviz_config_path = PathJoinSubstitution([
        canadarm_description_share, 
        'rviz', 
        'rviz_basic_settings_2.rviz'
    ])
    
    # Launch arguments
    gui_arg = DeclareLaunchArgument(
        name='gui', 
        default_value='true',
        choices=['true', 'false'],
        description='Flag to enable joint_state_publisher_gui'
    )
    
    model_arg = DeclareLaunchArgument(
        name='model', 
        default_value=default_model_path,
        description='Path to robot urdf/xacro file'
    )
    
    rviz_arg = DeclareLaunchArgument(
        name='rvizconfig', 
        default_value=default_rviz_config_path,
        description='Absolute path to rviz config file'
    )
    
    # Include the standard display launch file
    display_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([urdf_launch_pkg, 'launch', 'display.launch.py'])
        ),
        launch_arguments={
            'urdf_package': 'canadarm_description',
            'urdf_package_path': LaunchConfiguration('model'),
            'rviz_config': LaunchConfiguration('rvizconfig'),
            'jsp_gui': LaunchConfiguration('gui')
        }.items()
    )
    
    ld = LaunchDescription()
    ld.add_action(gui_arg)
    ld.add_action(model_arg)
    ld.add_action(rviz_arg)
    ld.add_action(display_launch)
    
    return ld
