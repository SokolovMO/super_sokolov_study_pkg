#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('even_numbers_overflow_publisher')

pub1 = rospy.Publisher('my_topic', Int32, queue_size=10)
pub2 = rospy.Publisher('overflow_topic', Int32, queue_size=10)

rate = rospy.Rate(10)

def start_even_numbers_overflow_publisher():

    count = 0

    while not rospy.is_shutdown():

        rospy.loginfo(count)
        if count < 100:
            pub1.publish(count)
        else:
            pub2.publish(count)
        
        if count == 100:
            count = 0
        
        count += 2
        
        rate.sleep()

try:
    start_even_numbers_overflow_publisher()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
