#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from apriltag_ros.msg import AprilTagDetectionArray
from move_robot import MoveTurtlebot3

x_diff = 0
depth_diff = 0

class Apriltag_follower(object):

    def __init__(self):
        self.bridge = CvBridge()
        #to use the CvBridge, you will need to transfer the message from compressed to raw (follow the instructions)

        self.publish = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.image_sub = rospy.Subscriber('/tag_detections_image', Image, self.camera_callback)
        self.sub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, self.callback)

    def camera_callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
        cv2.imshow("Scan", cv_image)
        cv2.waitKey(1)

    def callback(self, data):
        global x_diff, depth_diff
        try:
            x_diff = data.detections[0].pose.pose.pose.position.x - 0.06        #compensate the width to determine the right x difference
            depth_diff = data.detections[0].pose.pose.pose.position.z           #the z position represents the depth from the camera cooridnates
            vel_msg = Twist()

            #the proportianal variables values
            Kp_depth_diff = 0.3                                                 #the proportional value
            Kp_x_diff = 1.5                                                     #the proportional value

            #the velocity message
            if depth_diff < 0.1:                                                #the robot will maintain distance of 10 cm
                vel_msg.linear.x = 0
            else:
                vel_msg.linear.x = depth_diff * Kp_depth_diff
                vel_msg.angular.z = -1* x_diff * Kp_x_diff * abs(x_diff) * abs(x_diff)
            self.publish.publish(vel_msg)

        except IndexError:
            rospy.loginfo('Can not detect the tags paper')


def main():
    rospy.init_node('april_tag_node', anonymous=True)
    Apriltag_follower()
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    main()
