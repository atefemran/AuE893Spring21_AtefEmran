#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def rotate():

    #Starts a new node
    rospy.init_node('turtlesim_movement', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    r = rospy.Rate(10)

    # The message to the user
    print("Let' draw a circle")

    linear_speed = 0.3
    angular_speed = 0.3

    #The circle path correponds to circular and liear components (x and angular)
    vel_msg.linear.x=linear_speed
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angular_speed

    # Setting the current time for distance calculations
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    #Change the 6*Pi to the angle you want the turtle to stop at
    while(current_angle < 16*PI):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
        r.sleep()


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    vel_msg.linear.x=0
    velocity_publisher.publish(vel_msg)
    rospy.spin()


if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException: pass
