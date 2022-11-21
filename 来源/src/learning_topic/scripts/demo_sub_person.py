#! /usr/bin/env python
import rospy
from learning_topic.msg import person_custom
'''
订阅人的消息
    导包
    初始化
    创建订阅者
    处理订阅数据
    spin()



'''

def doperson(p):#回调函数
    rospy.loginfo("小伙子的数据:%s,%d,%.2f",p.name,p.age,p.height)

rospy.init_node('daye')
sub=rospy.Subscriber('jiaoshetou',person_custom,doperson)
rospy.spin()