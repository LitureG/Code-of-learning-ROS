#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
'''
    发布方:发布速度消息
        话题:/turtle/cmd_vel
        消息:geometry_msgs/Twist

        导包
        初始化
        创建发布者对象
        组织数据并发布


'''
if __name__ == '__main__':
    
    rospy.init_node('my_control')
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate=rospy.Rate(10)
    twist=Twist()
    twist.linear.x=0.5
    twist.linear.y=0.0
    twist.linear.z=0.0

    twist.angular.x=0.0
    twist.angular.y=0.0
    twist.angular.z=0.5

    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()
        rate.sleep()

        