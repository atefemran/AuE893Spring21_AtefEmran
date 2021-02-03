#!/usr/bin/env python3
import rospy
from geometry_msgs.msg  import Twist
from nav_msgs.msg import Odometry
from math import pow,atan2,sqrt
pi=22/7
corner=pi/2

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry, self.callback)
        self.pose = Odometry()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.pose.pose.position.x = round(self.pose.pose.pose.position.x, 4)
        self.pose.pose.pose.position.y = round(self.pose.pose.pose.position.y, 4)

    def move2goal(self):

#Variables definition ################################################################################################
        goal_pose = Odometry()
        vel_msg = Twist()

#YOUR INPUT ###########################################################################################################

        speed_linear=0.1
        speed_angular=0.1
        member_length=2

        angle_tolerance = 0.0001
        distance_tolerance = 0.1

        angle_diff=0.05  #intial value

        print("Let's draw a square")

#Going to the  first targets ################################################################################################

        for x in range(1, 4):
            if x==1:
                goal_pose.pose.pose.position.x = 2
                goal_pose.pose.pose.position.y = 0
                goal_angle = 0

            if x==2:
                print("ARRIVED the 1st Goooooal!")
                goal_pose.pose.pose.position.x = 2
                goal_pose.pose.pose.position.y = 2
                goal_angle = 0.71


            angle_diff = (goal_angle - self.pose.pose.pose.orientation.z)

            while (angle_diff > angle_tolerance):
                vel_msg.angular.z = (angle_diff/abs(angle_diff))*speed_angular   #Normalizing the differnce and getting the opposit angle
                #publish the velocity
                self.velocity_publisher.publish(vel_msg)
                #calculating the angle
                angle_diff = (goal_angle - self.pose.pose.pose.orientation.z)
                self.rate.sleep()


            #Stoping
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

            print("Finished orientation")

            #Setting the current time for distance calculations
            t0 = float(rospy.Time.now().to_sec())
            current_distance=0

            while sqrt(pow((goal_pose.pose.pose.position.x - self.pose.pose.pose.position.x), 2) + pow((goal_pose.pose.pose.position.y - self.pose.pose.pose.position.y), 2)) >= distance_tolerance:
                #linear velocity
                vel_msg.linear.x = speed_linear
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                #angular velocity in the z-axis:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = speed_angular * (((atan2(goal_pose.pose.pose.position.y - self.pose.pose.pose.position.y, goal_pose.pose.pose.position.x - self.pose.pose.pose.position.x))) - self.pose.pose.pose.orientation.z)

                print(vel_msg.angular.z)

                #Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)


            #Stoping
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()




if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move2goal()

    except rospy.ROSInterruptException: pass
