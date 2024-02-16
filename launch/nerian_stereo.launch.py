from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    nerian_stereo_node = Node(
                package='nerian_stereo',
                executable='nerian_stereo_node',
                prefix='xterm -e gdb -ex run --args',
                parameters=[
                    {'remote_host':                  '192.168.131.10'},
                    {'remote_port':                  '7681'},
                    {'use_tcp':                       True},

                    {'top_level_frame':               'nerian_stereo'},
                    {'internal_frame':                'nerian_stereo'},
                    {'publish_internal_frame':        False},
                    {'ros_coordinate_system':         True},
                    {'ros_timestamps':                True},

                    {'max_depth':                     -1},
                    {'point_cloud_intensity_channel': 'rgb32f'},
                    {'color_code_disparity_map':      ''},

                    {'delay_execution':               0.0},
 
                ]
            )
    ld.add_action(nerian_stereo_node)
    return ld

