#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32
//define the display text
def callback(data):
    rospy.loginfo("I receive %s", data.data)
    port = '/dev/ttyUSB0'

    baud = {

        'default': 115200,

        'alt': 19200  # shouldn't need this unless you accident$

    }

    bot = Create2(port=port, baud=baud['default'])



    bot.start()



    bot.full()
    bot.drive_straight(100)




    


//define the subscriber
def random_subscriber():
    rospy.init_node('subscriber')
    rospy.Subscriber('publisher',Int32, callback)
    rospy.spin()

if __name__=='__main__':
    random_subscriber()
