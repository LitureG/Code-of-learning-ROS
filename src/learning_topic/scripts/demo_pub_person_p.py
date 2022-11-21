#! /usr/bin/env python

import rospy
from learning_topic.msg import person_custom
'''
发布人的消息
   导包
   初始化
   创建发布者
   组织发布逻辑并发布数据

'''

if __name__ == '__main__':
    rospy.init_node('dama')
    pub=rospy.Publisher('jiaoshetou',person_custom,queue_size=10)
    #创建person数据
    p = person_custom()
    p.name = '奥特曼'
    p.age = 8
    p.height = 1.8

    #创建Rate对象
    rate=rospy.Rate(1)

    
    #循环发布
    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("发布的消息:%s,%d,%.2f",p.name,p.age,p.height)
        rate.sleep() 