#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def callback(message):
    rospy.loginfo("get message! ->  %s", message.data) # ターミナルへの表示

rospy.init_node('listener')
sub = rospy.Subscriber('message', String, callback)
rospy.spin()
