#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import struct
import numpy as np
# from wander import avoidance
#
# from follow_line_gazebo import LineFollower
# import cv2
# from cv_bridge import CvBridge, CvBridgeError
# from sensor_msgs.msg import Image

from std_msgs.msg import Int16

rospy.init_node('main_script', anonymous=True)
rate = rospy.Rate(20)
line_detection=''
def camera_callback(message):
    global line_detection
    line_detection = message.data

while True:
    detect_line_sub = rospy.Subscriber("/detect_line",Int16,camera_callback)
    if (line_detection == 1):
        print("got ittttt")
        rate.sleep()


# try:
#     wander = avoidance()
#     first_move=1
#     while True:
#         wander.move()
#         first_move=first_move+1
#
#         line_follower = LineFollower()
#
# except rospy.ROSInterruptException:
#     pass
