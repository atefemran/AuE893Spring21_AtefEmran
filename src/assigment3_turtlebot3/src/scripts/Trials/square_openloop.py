#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI=3.1415926535
corner_angle=PI/2

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    pose_subscriber = rospy.Subscriber('/odom', Odometry, queue_size=10))        #New line
    pose = Odometry()                                                           #New Line
    vel_msg = Twist()
    r = rospy.Rate(5);

    #Square defining parameters
    print("Let's draw a square")
    speed = 0.3
    distance = 2
    angular_speed = 0.3

    i=1     #required for the while loop
    #each loop represents a memeber and a rotation
    #make sure that the condition value is the multiplication of 4
    while(i<=4):
        i=i+1

        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        r.sleep()
        print("test")

        if i==1:
            goal_x=2
            goal_y=0
        if i==2:
            goal_x=2
            goal_y=2
        if i==3:
            goal_x=0
            goal_y=2
        if i==4:
            goal_x=0
            goal_y=0

        #Setting the current time for distance calculations
        t0 = float(rospy.Time.now().to_sec())
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            vel_msg.linear.x = speed
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            r.sleep()
            #Takes actual time to velocity calculus
            t1=float(rospy.Time.now().to_sec())
            current_distance= speed*(t1-t0)
            #Calculates distancePoseStamped

        #Stop
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = angular_speed
        velocity_publisher.publish(vel_msg)
        r.sleep()


        # Setting the current time for angle calculations
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        #we should start with 0 angle
        angle_diff = (goal_angle - self.pose.pose.pose.orientation.z)
###########################################################################################HHhhhhHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHhhhhh###############
        angle_diff = (atan2(goal_y - pose.pose.pose.position.y, goal_x - pose.pose.pose.position.x) - self.pose.theta)

        while(abs(angle_diff) > angle_tolerance):
            vel_msg.angular.z = (angle_diff/abs(angle_diff))*speed_angular   #Normalizing the differnce and getting the opposit angle
            #publish the velocity
            self.velocity_publisher.publish(vel_msg)
            #calculating the angle
            angle_diff = (goal_angle - self.pose.pose.pose.orientation.z)
            self.rate.sleep()

        #Stop
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        r.sleep()

    #After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
	try:
		#Testing our function
		move()
	except rospy.ROSInterruptException: pass
