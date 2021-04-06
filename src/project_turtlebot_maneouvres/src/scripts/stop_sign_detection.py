#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import String
from darknet_ros_msgs.msg import BoundingBoxes

class stopsign:
    def __init__(self):
        rospy.init_node('stopsignprobability', anonymous=True)
        self.class_pub = rospy.Publisher('class', String, queue_size=10)
        self.yolo_sub = rospy.Subscriber('/darknet_ros/bounding_boxes',BoundingBoxes,self.newprediction)
        self.rate = rospy.Rate(10)

    def newprediction(self,bounding_box):
        self.rate.sleep()
        prediction = bounding_box.bounding_boxes
        for box in prediction:
            # print(box.probability, box.xmin, box.xmax, box.ymin, box.ymax, box.Class)
            identified_class=box.Class
            area = (box.xmax-box.xmin)*(box.ymax-box.ymin)
            if ((identified_class == "bench") & (box.probability > 0.3) & (area > 0.1)):        #change based on the calibration
                self.class_pub.publish(identified_class)
                self.rate.sleep()
            # elif identified_class != "bench":
            #     self.class_pub.publish("non")

def main():
    while not rospy.is_shutdown():
        stopsignmain=stopsign()

if __name__ == '__main__':
    main()
