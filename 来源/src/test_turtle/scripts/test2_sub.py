#! /usr/bin/env python
import rospy
from turtlesim.msg import Pose

def doPose(pose):
    rospy.loginfo("P->乌龟位置信息:坐标(%.2f,%.2f),朝向:%.2f,线速度:%.2f,角速度:%.2f",\
        pose.x, pose.y, pose.theta,pose.linear_velocity, pose.angular_velocity)

if __name__ == '__main__':
    rospy.init_node('subpose')
    sub=rospy.Subscriber('/turtle1/pose',Pose,doPose,queue_size=100)

    rospy.spin()