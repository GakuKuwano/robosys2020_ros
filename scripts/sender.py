#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from datetime import datetime

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import getpass

fromAddress = input('あなたのメールアドレスを入力してください：') #送信元のメールアドレス
password = getpass.getpass() #パスワード
toAddress = '送信先のメールアドレス'

rospy.init_node('talker')
pub = rospy.Publisher('message', String, queue_size=1) 
rate = rospy.Rate(10)

def send_message(fromAddress, password, subject, bodyText, toaddress):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(fromAddress, password)

    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()
    smtpobj.send_message(msg)
    rospy.loginfo("Send Messege")
    smtpobj.close()

while not rospy.is_shutdown():
    data = String()
    timestamp = rospy.get_time()
    time = datetime.fromtimestamp(timestamp)

    subject = input('件名：')
    bodyText = input('本文：')
    checker = False
    while not checker:
        check = input('送信しますか[y/n]?')
        if check == 'y':
            checker = True
            send_message(fromAddress, password, subject, bodyText, toAddress)
            data.data = ' [%s'%fromAddress  + '(%s)]'%time
            pub.publish(data)
            rate.sleep()
        elif check == 'n':
            checker = True
    input("続ける場合は 'Enter' / 終了するときは 'Ctrl＋C' -> 'Enter' ：")
            
