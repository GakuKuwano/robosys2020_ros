#!/usr/bin/env python3

import rospy
#from std_msgs.msg import Int32
from std_msgs.msg import String
from datetime import datetime


rospy.init_node('talker')
pub = rospy.Publisher('chat', String, queue_size=1) 
data = String()
timestamp = rospy.get_time()
time = datetime.fromtimestamp(timestamp)
data.data = "hell world(%s)" %time
rate = rospy.Rate(1)

#while not rospy.is_shutdown():
#    pub.publish(n)
#    rate.sleep()

rospy.sleep(10)
pub.publish(data)
rospy.spin()

