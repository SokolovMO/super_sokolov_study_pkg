#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, Int32MultiArray

def summing_callback(data):
    s = sum(data.data)
    pub.publish(Int32(s))

if __name__ == '__main__':
    rospy.init_node('summing_node')
    pub = rospy.Publisher('output_topic', Int32, queue_size=10)
    sub = rospy.Subscriber('input_topic', Int32MultiArray, summing_callback)
    rospy.spin()
