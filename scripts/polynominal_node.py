#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

def polynomial_callback(data):
    powers = range(1, len(data.data) + 1)
    powered_data = []
    for i in range(len(data.data)):
        powered_data.append(data.data[i] ** powers[i])
    pub.publish(Int32MultiArray(data=powered_data))

if __name__ == '__main__':
    rospy.init_node('polynomial_node')
    pub = rospy.Publisher('output_topic', Int32MultiArray, queue_size=10)
    sub = rospy.Subscriber('input_topic', Int32MultiArray, polynomial_callback)
    rospy.spin()
