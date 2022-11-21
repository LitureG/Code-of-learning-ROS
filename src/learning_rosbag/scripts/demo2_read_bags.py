#! /usr/bin/env python

from std_msgs.msg import String
import rospy,rosbag ,std_msgs

'''
需求:duqu磁盘上的bag文件
流程:
导包
初始化
创建rosbag对象并打开文件
du数据
关闭流
'''

if __name__ == '__main__':
    rospy.init_node('write_bag')
    bag = rosbag.Bag('hello.bag','r')
    msgs=bag.read_messages('/liaotian')
    for topic,msg,time in msgs:
        rospy.loginfo('huati:%s,xiaoxi:%s,shijian:%s',topic,msg.data,time)
    bag.close()