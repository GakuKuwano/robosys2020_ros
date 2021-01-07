#!/usr/bin/env python3
import rospy
#from std_msgs.msg import Int32
from std_msgs.msg import String


def callback(message):
    a = message
    print(a)
    rospy.loginfo("get message! [%s]", message.data) # ターミナルへの表示

rospy.init_node('listener')
sub = rospy.Subscriber('chat', String, callback)
rospy.spin()
