#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import struct

class emergency:

    def __init__(self):
        # unique node (using anonymous=True).
        rospy.init_node('emergency_brake', anonymous=True)

        # Publisher which will publish to the topic '/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.scan_subscriber = rospy.Subscriber('/scan', LaserScan, self.new_measurment)
        self.rate = rospy.Rate(10)
        self.current_distance=1e3

    def new_measurment(self,lidar_readings):
        self.current_distance = lidar_readings.ranges[1]


    def move(self):

        # the input paramters
        speed = 0.3
        emergency_distance = 0.7
        vel_msg = Twist()

        # Emergencu condition
        while self.current_distance > emergency_distance:
            vel_msg.linear.x = speed
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            # Publishing vel_msg
            self.velocity_publisher.publish(vel_msg)
         	 # Publish at the desired rate.
            self.rate.sleep()


        # Stop
        vel_msg.linear.x = 0
        self.velocity_publisher.publish(vel_msg)

        # ctrl + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        x = emergency()
        x.move()

    except rospy.ROSInterruptException:
        pass
