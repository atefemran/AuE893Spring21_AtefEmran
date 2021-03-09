# TEAM 4

##  ASSIGNMENT 6


### Navigating through assignment 6:

![Navigation Image](https://github.com/atefemran/AuE893Spring21_AtefEmran/blob/master/src/assignment6_trackingandfollowing/videos/Navigation.png)

### The tasks

In Assignment 6 we have 2 main tasks:-

A) Make the turtlebot follow a line in Gazebo and in the real world
![Wall follow](https://github.com/atefemran/AuE893Spring21_AtefEmran/blob/master/src/assignment6_trackingandfollowing/videos/line_following_gazebo.gif)
![Wall follow](https://github.com/atefemran/AuE893Spring21_AtefEmran/blob/master/src/assignment6_trackingandfollowing/videos/line_follower_real_world.gif)
	
B) Make the turtlebot follow april tags in real world
![Wander in Gazebo](https://github.com/atefemran/AuE893Spring21_AtefEmran/blob/master/src/assignment6_trackingandfollowing/videos/apriltag_follower_real_world.gif)
			

### How to run each part?

	A) Gazebo: 	'$ roslaunch assignment6_trackingandfollowing turtlebot3_follow_line.launch'  
	   Real World: after having running roscore, running the turtlebot, and running bringup for the robot and the camera, run the below rosrun command
	   		'$ rosrun assignment6_trackingandfollowing follow_line_real_world.py'  
	B) After having a running roscore and running the bringup of the robot and camera, the robot is now connected. 
	   Run this line in new terminal to transform the image message from compressed to raw to be able to use the CvBridge '$ rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw'  
	   Finally run this rosrun line in new terminal '$ oslaunch assignment6_trackingandfollowing apriltag_follower.launch'  
