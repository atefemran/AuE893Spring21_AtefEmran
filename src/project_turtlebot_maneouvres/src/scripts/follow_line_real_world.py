#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
#from cv_bridge import CvBridge, CvBridgeError          #CV bridge does not work with CompressedImage
from geometry_msgs.msg import Twist
#from sensor_msgs.msg import Image                      #it is different message
from sensor_msgs.msg import CompressedImage as Image             #importing the compressed messsage

class LineFollower(object):

    def __init__(self):
        #self.bridge_object = CvBridge()
        self.velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        #self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed",Image,self.camera_callback)             #queue_size was not added

    def camera_callback(self, data):
        #cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        np_arr = np.frombuffer(data.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)                                                                           #wrong syntax for this openCV version

        # We get image dimensions and crop the parts of the image we dont need
        height, width, channels = cv_image.shape
        crop_start=(height/2)+150
        crop_end=(height/2)+250
        crop_img = cv_image[int(crop_start):int(crop_end)][1:int(width)]
        #crop_img = cv_image[340:360][1:640]

        # photo center
        centerx, centery = width/2, ((crop_start+crop_end)/2-crop_start)

        # Convert from RGB to HSV
        hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

        # Define the Yellow Colour in HSV

        """
        To know which color to track in HSV use ColorZilla to get the color registered by the camera in BGR and convert to HSV.
        """

        # Threshold the HSV image to get only yellow colors
        lower_yellow = np.array([20,100,100])
        upper_yellow = np.array([50,255,255])
        #lower_yellow = np.array([45,67,81])
        # upper_yellow = np.array([45,29,88])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Calculate centroid of the blob of binary image using ImageMoments
        m = cv2.moments(mask, False)

        try:
            cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
        except ZeroDivisionError:
            cx, cy = 10000, 10000

        # Draw the centroid in the resultut image
        # cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
        cv2.circle(mask,(int(cx), int(cy)), 10,(0,0,255),-1)
        cv2.imshow("Original", cv_image)
        cv2.imshow("MASK", mask)
        cv2.waitKey(1)

        vel_msg = Twist()

        #calculating the difference between the center of the image and the centroid
        diff_y= centery-cy
        diff_x= centerx-cx

        #Proportional controller value calculation for linear speed
        if diff_y < -8000 :
            vel_msg.linear.x = 0.3
        elif abs(diff_y) <2:
            vel_msg.linear.x = 0.3
        else:
            vel_msg.linear.x = 0.3*diff_y/15

        # Proportional controller value calculation for angulat speed
        if diff_x < -8000 :
            vel_msg.angular.z = 0
        else:
            vel_msg.angular.z = 0.3*diff_x/100

        # vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        self.velocity_publisher.publish(vel_msg)

        print("centerioid (x,y): ", cx,cy)
        print("center (x,y): ", centerx,centery)
        print("linear speed: ", vel_msg.linear.x)

    def clean_up(self):
        cv2.destroyAllWindows()


def main():
    rospy.init_node('line_following_node', anonymous=True)
    line_follower_object = LineFollower()
    rate = rospy.Rate(10)
    ctrl_c = False
    def shutdownhook():
        # Works better than rospy.is_shutdown()
        line_follower_object.clean_up()
        rospy.loginfo("Shutdown time!")
        ctrl_c = True
    rospy.on_shutdown(shutdownhook)
    while not ctrl_c:
        rate.sleep()

if __name__ == '__main__':
        main()
