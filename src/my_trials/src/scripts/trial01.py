#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node('first_node')
    print('ready')
    while not rospy.is_shutdown():
        print('hello')
        rospy.Rate(1).sleep()
    rospy.sleep(1)

    print('not ready')
