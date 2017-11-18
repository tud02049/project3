

from __future__ import print_function

import rospy

from pycreate2 import Create2

import time



from std_msgs.msg import Int32

#define the sensor_state Publisher

def IR_sensor():

    rospy.init_node('IR_sensor')

    pub=rospy.Publisher('IR_sensors',Int32, queue_size=10)

    rate= rospy.Rate(2)

    #read sensor range at every 2 seconds

    port = '/dev/ttyUSB0'

    baud = {

        'default': 115200,

        'alt': 19200  # shouldn't need this unless you accident$

    }

    bot = Create2(port=port, baud=baud['default'])



    bot.start()



    bot.full()



    print('Starting ...')

    IR_sensor=[0,0,0,0,0,0];

    while not rospy.is_shutdown():



        # Packet 100 contains all sensor data.

        IR_sensor[0] = bot.get_sensors().light_bumper_left

       IR_sensor [1]= bot.get_sensors().light_bumper_front_left

       IR_sensor[2]= bot.get_sensors().light_bumper_center_left

        IR_sensor[3]= bot.get_sensors().light_bumper_center_right

       IR_sensor[4]= bot.get_sensors().light_bumper_front_right

       IR_sensor[5]= bot.get_sensors().light_bumper_right

        rospy.loginfo(IR_sensor)

        pub.publish(IR_sensor)

        rate.sleep()



if __name__=='__main__':

    try:

        IR_sensor_publisher()

    except rospy.ROSInterruptException:

        pass
