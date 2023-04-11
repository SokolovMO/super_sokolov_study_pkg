#!/usr/bin/env python3
import rospy # импортируем основной модуль
from std_msgs.msg import String # импортируем используемый тип сообщений

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('listener') # регистрируем ноду в системе ROS с именем 'listener'
rospy.Subscriber('my_chat_topic', String, callback, queue_size=10) # регистрируем топик на чтение из  'my_chat_topic', тип сообщения и размер очереди
rospy.spin() # удерживаем программу до прерывания
