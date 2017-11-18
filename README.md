# project3

in project we communcate with roomba using Ros in raspberrypi; after installing ros kinetic follow the instructions below

we first create a worksopace and package by using the link below 

https://www.intorobotics.com/ros-kinetic-publisher-and-subscriber-in-python/

we go to the workspace directory and type the following code

$rosdep update

$rosdep install --from-paths src -i -y

$catkin_make

$source ./devel/setup.bash

$pip install pycreate2

initiate the roscore

$cd /your_work_space

$source ./devel/setup.bash

$export ROS_MASTER_URI=http://[pi_ip_address]:11311

$export ROS_IP=[pi_ip_address]

$roscore

run publisher

$cd /your_work_space/src/your_pakage_name/src/

$chmod u+x 'file_names.py'

$sudo usermod -a -G dialout $USER  #give permission to the USB port to serial

$rosrun 'your_pakage_name' 'file_name.py'
