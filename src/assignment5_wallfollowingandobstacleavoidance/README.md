# TEAM 4

##  ASSIGNMENT 5  


### Navigating through assignment 5:

![Navigation Image](https://raw.githubusercontent.com/atefemran/AuE893Spring21_AtefEmran/master/src/assignment5_wallfollowingandobstacleavoidance/videos/navigation.png)

### The tasks

In Assignment 5 we have 3 tasks:-

In all the tasks the same concept is being used where we divid the LiDAR readings into different ranges, and using the mean distance measurment of these ranges, we could estimate the location of the robot to the different obstcales, and make the turtlbot react accordingly. 

A) Make the turtlebot follow walls
		Using script wall_follow.py script and launch files. 
![Wall follow](https://github.com/atefemran/AuE893Spring21_AtefEmran/blob/master/src/assignment5_wallfollowingandobstacleavoidance/videos/gifs/wall_follow.gif?raw=true)
	
B) Make the turtlebot wander in a room and avoid obstcales on Gazebo
		Using script wander.py script and launch files. 
![Wander in Gazebo](https://github.com/atefemran/AuE893Spring21_AtefEmran/blob/master/src/assignment5_wallfollowingandobstacleavoidance/videos/gifs/wander_gazebo.gif?raw=true)
			
C) Make the turtlebot wander in a room and avoid obstcales in th real world
		Using script wander.py script and launch files. 
![Wander in Real World](https://github.com/atefemran/AuE893Spring21_AtefEmran/blob/master/src/assignment5_wallfollowingandobstacleavoidance/videos/gifs/wander_real_world.gif)
		
### How to run each part?

	A) '$ roslaunch assignment5_wallfollowingandobstacleavoidance wall_follower.launch'  
	B) '$ roslaunch assignment5_wallfollowingandobstacleavoidance wander.launch '  
