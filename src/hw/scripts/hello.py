#!/usr/bin/env python

##指定解释器

#1导入库
import rospy
#2编写主入口,可有可无
if __name__ == '__main__':
#3初始化ros节点
    rospy.init_node('hello_p')

#4输出日志
    rospy.loginfo('Hello world!')   