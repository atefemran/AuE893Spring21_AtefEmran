#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import struct
import numpy as np

# the logic is dviding the wander condition to three modes based ont he surroundings
# this is being established by dividing the lidar into 3 regions and selecting the
# mode based on the front readings:
# 1) The wander mode - the min lidar reading from the fron region is above the threshold, the TB will try to center its position
# 2) Slow Down - When the min front measurment is less than the threshold, the linear speed is decreased
# 3) Critical - when its very close to obstcal, stops and rotates away from obstcale

class avoidance:

    def __init__(self):
        # unique node (using anonymous=True).
        rospy.init_node('avoidance', anonymous=True)

        # Publisher which will publish to the topic '/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.scan_subscriber = rospy.Subscriber('/scan', LaserScan, self.new_measurment)
        self.rate = rospy.Rate(10)
        self.max= 3.5

    def new_measurment(self,lidar_readings):
        self.rate.sleep()

        self.left = np.minimum(np.min(lidar_readings.ranges[20:75]),self.max)
        self.left_mean = np.minimum(np.mean(lidar_readings.ranges[20:75]),self.max)
        self.front = np.minimum(np.minimum(np.min(lidar_readings.ranges[0:22]),np.min(lidar_readings.ranges[338:360])),self.max)
        self.right = np.minimum(np.min(lidar_readings.ranges[285:340]), self.max)
        self.right_mean = np.minimum(np.mean(lidar_readings.ranges[285:340]), self.max)

    def move(self):
        rospy.sleep(3)              #Needed while running from launch file
        vel_msg = Twist()

        #Tuning Parameters
        # (1) threshhold, (2) critical, (3) speeds (linear and angular), (4) difference min and mean
        speed_lin = 0.15
        speed_ang = 0.3

        threshold = 0.5             #in real world make it 0.5 | Gazebo 0.5
        critical = 0.2              #in real world make it 0.3 | Gazebo 0.2

        #let's move it
        vel_msg.linear.x = speed_lin
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        self.rate.sleep()

        # The indefinite loop
        while True:
            # Let's descover what is surrounding us! (kp value)
            diff = self.left-self.right                 #used when critical
            diff_mean = self.left_mean-self.right_mean  #used in regular conditions

            #what if we will hit something ahead --> reduce the linear speed and rotate .. take it easy :)
            if self.front<threshold and self.front>critical :
                # Reduce linear speed and rotate
                vel_msg.linear.x = self.front*speed_lin/threshold
                vel_msg.angular.z = speed_ang*diff_mean/(abs(diff_mean)+0.000000001)
                # print('threshhold')
            elif self.front<critical:
                vel_msg.linear.x = 0
                vel_msg.angular.z = speed_ang*diff/(abs(diff)+0.000000001)
                # print('critical')
            else:
                vel_msg.linear.x = speed_lin
                vel_msg.angular.z = speed_ang*diff_mean/(abs(diff_mean)+0.000001)
                # print('else')

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        # ctrl + C, the node will stop.
        rospy.spin()

try:
    x = avoidance()
    x.move()

except rospy.ROSInterruptException:
    pass

#Atef Emran @Apr,2021
