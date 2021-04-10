#!/usr/bin/env python3
import rospy
import roslaunch


uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
launch = roslaunch.parent.ROSLaunchParent(uuid,["/home/atefemran/AuE8935_Course/ros_local_ws/src/darknet_ros/darknet_ros/launch/darknet_ros.launch"])
launch.start()
rospy.sleep(300)
