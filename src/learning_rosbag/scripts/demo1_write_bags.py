#! /usr/bin/env python

from std_msgs.msg import String
import rospy,rosbag

'''
需求:写出消息数据到磁盘上的bag文件
流程:
导包
初始化
创建rosbag对象并打开文件
写数据
关闭流
'''

if __name__ == '__main__':
    rospy.init_node('write_bag')
    bag = rosbag.Bag('hello.bag','w')
    msg=String()
    bag.write('/liaotian',msg)
    bag.write('/liaotian',msg)
    bag.write('/liaotian',msg)
    bag.write('/liaotian',msg)
    bag.write('/liaotian',msg)
    bag.write('/liaotian',msg)
    bag.close()