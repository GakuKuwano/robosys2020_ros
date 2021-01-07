#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from datetime import datetime


rospy.init_node('talker')
pub = rospy.Publisher('message', String, queue_size=1) 
rate = rospy.Rate(10)

name = input("あなたの名前を入力してください：")
print("-------------------------------------")
print("%sさんメッセージツールへようこそ！" %name)
print("終了するときは 'Ctrl＋C' -> 'Enter'")
print("--------------------------------------")

while not rospy.is_shutdown():
    data = String()
    timestamp = rospy.get_time()
    time = datetime.fromtimestamp(timestamp)
    x = input("文字を入力してね：")
    data.data = x + ' [%s'%name  + '(%s)]'%time
    pub.publish(data)
    rate.sleep()

