#!/usr/bin/env python3
import rospy # импортируем основной модуль
from std_msgs.msg import String # импортируем используемый тип сообщений

rospy.init_node('talker') # регистрируем узел в системе ROS с именем 'talker'
pub = rospy.Publisher('my_chat_topic', String, queue_size=10) # регистрируем топик на публицакию  в 'my_chat_topic', тип сообщения и размер очереди
rate = rospy.Rate(1) # частота выполнения кода

def start_talker():
    
    # создаем объект сообщения
    msg = String()

    # Бесконечный цикл, пока ROS система работает
    while not rospy.is_shutdown():
        # сформируем сообщение, которое включает в себя время
        hello_str = "hi =) %s" % rospy.get_time()
        # вывод в терминал информации (содержание сообщения)
        rospy.loginfo(hello_str)

        # Заполнение сообщения и публикация сообщения в топик
        msg.data = hello_str
        pub.publish(msg)

        # Сон в соответствии с выдерживаемой частотой
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
