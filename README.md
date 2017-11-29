
# project3

in project we communcate with roomba using Ros in raspberrypi; after installing ros kinetic follow the instructions below

we first create a worksopace and package by using the link below 

https://www.intorobotics.com/ros-kinetic-publisher-and-subscriber-in-python/

# we go to the workspace directory and type the following code

$rosdep update

$rosdep install --from-paths src -i -y

$catkin_make

$source ./devel/setup.bash

$pip install pycreate2

# initiate the roscore

$cd /your_work_space

$source ./devel/setup.bash

$export ROS_MASTER_URI=http://[pi_ip_address]:11311

$export ROS_IP=[pi_ip_address]

$roscore

# run publisher
# open another terminal
cd ~/robot
source devel/setup.bash
rosrun fanny_package irsensors.py

# run suscriber 
# open a third terminal
cd ~/robot
source devel/setup.bash
rosrun fanny_suscriber wheels.py

# wheels

in this piece of code

when an object call publisher enter 

call back will activate 

after call back is activate 

the wheel will run

# sensor 

sensor read and avoid obstacles

