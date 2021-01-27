#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI=3.1415926535
corner_angle=PI/2

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Square defining parameters
    print("Let's draw a square")
    speed = 0.2
    distance = 2
    angular_speed = 0.2

    i=1     #required for the while loop
    #each loop represents a memeber and a rotation
    #make sure that the condition value is the multiplication of 4
    while(i<=4):
        i=i+1
        #Drawing the  square member
        vel_msg.linear.x = speed
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        #Setting the current time for distance calculations
        t0 = float(rospy.Time.now().to_sec())
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)

        #Rotating
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = angular_speed

        # Setting the current time for angle calculations
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while(current_angle < corner_angle):
            #publish the velocity
            velocity_publisher.publish(vel_msg)
            #calculating the time
            t1 = rospy.Time.now().to_sec()
            #calculating the angle
            current_angle = angular_speed*(t1-t0)



    #After the loop, stops the robot
    vel_msg.linear.x = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
	try:
		#Testing our function
		move()
	except rospy.ROSInterruptException: pass
