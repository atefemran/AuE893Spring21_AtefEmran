#!/usr/bin/env python3
import rospy
import roslaunch
import numpy as np
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from darknet_ros_msgs.msg import BoundingBoxes

class stopsign:
    def __init__(self):
        rospy.init_node('stopsignprobability', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.stop_sign_detect_pub = rospy.Publisher('/detect_stop', Int16, queue_size=10)
        self.yolo_sub = rospy.Subscriber('/darknet_ros/bounding_boxes',BoundingBoxes,self.newprediction)
        self.detect_line_sub = rospy.Subscriber("/detect_line",Int16,self.line_detection)
        self.rate = rospy.Rate(10)

    def line_detection(self,msg):
        global line_detection
        line_detection = msg.data

    def newprediction(self,bounding_box):
        self.rate.sleep()
        prediction = bounding_box.bounding_boxes
        for box in prediction:
            global stop_sign_detect
            identified_class=box.Class
            probability = float(box.probability)
            area = (box.xmax-box.xmin)*(box.ymax-box.ymin)
            if ((identified_class == "stop sign") & (probability > 0.5) & (area > 1)):        #change based on the calibration
                stop_sign_detect = 1
            self.stop_sign_detect_pub.publish(stop_sign_detect)
            rospy.sleep(0.1)



vel_msg = Twist()
line_detection = 0
stop_sign_detect = 0
while True:
    stopsign()
    if line_detection ==1:
        stopsign()
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        launch = roslaunch.parent.ROSLaunchParent(uuid,["/home/atefemran/AuE8935_Course/ros_local_ws/src/darknet_ros/darknet_ros/launch/darknet_ros.launch"])
        launch.start()
        while stop_sign_detect==0:
            rospy.sleep(0.1)
            stopsign()
    if stop_sign_detect==1:
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.sleep(3)



# import rospy
# import numpy as np
# from darknet_ros_msgs.msg import BoundingBoxes
#
# class stopsign:
#     def __init__(self):
#         rospy.init_node('stopsignprobability', anonymous=True)
#         self.yolo_sub = rospy.Subscriber('/darknet_ros/bounding_boxes',BoundingBoxes,self.newprediction)
#         self.rate = rospy.Rate(10)
#
#     def newprediction(self,bounding_box):
#         self.rate.sleep()
#         prediction = bounding_box.bounding_boxes
#         for box in prediction:
#             identified_class=box.Class
#             area = (box.xmax-box.xmin)*(box.ymax-box.ymin)
#             if ((identified_class == "stop sign") & (box.probability > 0.6) & (area > 1000):        #change based on the calibration
#                 self.stop_sign.publish(identified_class)
#                 self.rate.sleep()
#             # elif identified_class != "bench":
#             #     self.stop_sign.publish("non")
#
# def main():
#     while not rospy.is_shutdown():
#         stopsignmain=stopsign()
#
# if __name__ == '__main__':
#     main()
