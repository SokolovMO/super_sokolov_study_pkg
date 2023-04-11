#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def even_numbers_overflow_subscriber_callback(data):
    rospy.loginfo("Received number from /overflow_topic: %d", data.data)

rospy.init_node('even_numbers_overflow_subscriber')

sub = rospy.Subscriber('overflow_topic', Int32, even_numbers_overflow_subscriber_callback)

rospy.spin()
