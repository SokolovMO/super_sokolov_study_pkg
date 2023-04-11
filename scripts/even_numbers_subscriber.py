#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def even_numbers_subscriber_callback(data):
    rospy.loginfo("Received number from /my_topic: %d", data.data)

rospy.init_node('even_numbers_subscriber')

sub = rospy.Subscriber('my_topic', Int32, even_numbers_subscriber_callback)

rospy.spin()
