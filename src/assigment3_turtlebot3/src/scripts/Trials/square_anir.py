#!/usr/bin/env python3
import rospy
from math import pi
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    #print("Let's move your robot")
    #speed = input("Input your speed:")
    #distance = input("Type your distance:")
    #isForward = input("Foward?: ")#True or False
    speed = 0.3
    side = 2
    #pi = 3.15
    distance = 4*(side + (pi/2))
    
    #Checking if the movement is forward or backwards
    #if(isForward):
    #    vel_msg.linear.x = abs(speed)
    #else:
    #    vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    i = 0

    while i == 0:

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
	
        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
        
        	if(current_distance < side):
        		vel_msg.linear.x = 0.3
        		vel_msg.angular.z = 0
        	
        	if(current_distance >= side and current_distance < (side+(pi/2))):
        		vel_msg.linear.x = 0
        		vel_msg.angular.z = 0.3
        	
        	if(current_distance < (side*2 + (pi/2))  and current_distance >= (side+(pi/2)) ):
        		vel_msg.linear.x= 0.3
        		vel_msg.angular.z = 0
        	
        	if(current_distance >= (side*2 + (pi/2))  and current_distance < 2*(side + (pi/2)) ):
        		vel_msg.linear.x = 0
        		vel_msg.angular.z = 0.3
        	
        	if(current_distance < (side*3 + 2*(pi/2))  and current_distance >= 2*(side + (pi/2)) ):
        		vel_msg.linear.x= 0.3
        		vel_msg.angular.z = 0
        	
        	if(current_distance >= (side*3 + 2*(pi/2))  and current_distance < 3*(side + (pi/2)) ):
        		vel_msg.linear.x = 0
        		vel_msg.angular.z = 0.3
        	
        	if(current_distance < (side*4 + 3*(pi/2)) and current_distance >= 3*(side + (pi/2)) ):
        		vel_msg.linear.x= 0.3
        		vel_msg.angular.z = 0
        	
        	if(current_distance >= (side*4 + 3*(pi/2))  and current_distance <= 4*(side + (pi/2)) ):
        		vel_msg.linear.x = 0
        		vel_msg.angular.z =0.3
        	
        	#Publish the velocity
        	velocity_publisher.publish(vel_msg)
		#Takes actual time to velocity calculus
		
        	t1=rospy.Time.now().to_sec()
		#Calculates distancePoseStamped
		
        	current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        i = 1
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
