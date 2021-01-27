This file explains the file in assigment2 "Turtlesim"

##########################################################################################
### THE STRUCTURE ####

The deliverables for the assigment are 3 types of files for 3 tasks:

	Types of files:
	1- Scripts (python3 files): you can find them on the following path:
	   AuE893Spring21_AtefEmran/src/assigment2_turtlesim/src/scripts/
	2- Launch files: you can fin them on the following path:
	   AuE893Spring21_AtefEmran/src/assigment2_turtlesim/src/launch/
	3- Videos and screenshots: you can find them on this path:
	   AuE893Spring21_AtefEmran/src/assigment2_turtlesim/videos and screenshots/

	Tasks files:
	The below names will be used to name the files for each task
	1- Drawing a circle --> circle.<file_extension>
	2- Turtle move in a square with specified dimensions --> square_openloop.<file_extension>
	3- Turtle move in a square using target points --> square_closedloop.<file_extension>

##########################################################################################
# [1] ### Drawing Circle ####
The script makes the turtle move in a circle with a constant predefined speed.

The code logic consists of the setting up the importing files and defining the variables. Then, the  next part considers the needed angular speed and linear speed to draw a circle (please note that you need to change these values to change the circle shape and speed. 

If you want to change the angular speed, go to line 18, and put the  angular speed instead of the 90. If you want to change the linear speed, go to line 21, and put the linear speed instead of the 2. 

![Circle Screenshot](/videos and screenshots/circle.png)

##########################################################################################
# [2] ### Drawing Square with specified dimensions ####

square_openloop uses the a predefined angular and linear speeds to draw a square, and required square member length "the distance variable". The script is a for loop, in which every loop draw a square member and turn the turtle to draw the next member. Number of loops shall equal = x*4, where x is the number of squares needed. The script uses the defined linear speed, and the time to achieve the required length of the square meembers; then, uses the angular speed to rotate the turtle till reaching the "turning angle" which is 90 degrees.

Changing the linear speed --> line 15 --> "speed" variable
Changing the length of each member --> line 16 --> "distance" variable
Changing the angular speed --> line 17 --> "angular speed" variable
Changing the number of squares -- line 19 --> "i" variable


##########################################################################################
# [3] ### Drawing Square with specified goals/targets ####

square_closedloop uses a predefined square corners goals to draw a square. The script cosnsists of four identical section, each one of them draw a memeber. Before these four a section, the importing section and making the turtle move to the defined starting point. 

Each section consists of two main sub-sections, the first one uses the next goal and the current goal locations to calculate the difference in angle as an input to a proportiional controller adjust the turtle to its new destination. The next sub-section uses a proportional controller alss using the difference in pose as the input to the controller. Both of these sections consist of loops with a target of achieving a specified tolerance. 

Changing the goals --> the first two line after the "Going to ....." line --> "Goal_pose" variables
Changing the tolerance --> lines 33 and 34 --> "distance_tolerance" and "angle_tolerance" variables
Changing the speed of the turtle --> the propertional controler value inside each loop


##########################################################################################

