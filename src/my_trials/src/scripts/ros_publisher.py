#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("ros_publisher")
    publisher = rospy.Publisher("/my_topic", String, queue_size=10)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        msg= String()
        msg.data = "5od ama a2olak yaaa"
        publisher.publish(msg)
        rate.sleep()
        
    print('this is ended')
