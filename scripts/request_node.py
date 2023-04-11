#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, Int32MultiArray

def callback(data):
    print("Sum:", data.data)

def request_node():
    rospy.init_node('request_node')
    pub = rospy.Publisher('output_topic', Int32MultiArray, queue_size=10)
    sub = rospy.Subscriber('input_topic', Int32, callback)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        try:
            numbers = input("")
            numbers = list(map(int, numbers.split()))
            msg = Int32MultiArray(data=numbers)
            pub.publish(msg)

            rate.sleep()

        except (rospy.ROSInterruptException, KeyboardInterrupt):
            rospy.logerr('Exception catched')

    rospy.loginfo("Shutting down request_node")

if __name__ == '__main__':
    try:
        request_node()
    except (rospy.ROSInterruptException, KeyboardInterrupt):
        rospy.logerr('Exception catched')
