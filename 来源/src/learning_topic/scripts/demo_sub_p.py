#! /usr/bin/env python
import rospy
from std_msgs.msg import String #倒入消息格式
'''
    订阅实现流程
        1.导包
        2.初始化ros节点
        3.创建订阅者对象
        4.回调函数处理数据
        5.spin()


'''
def doMsg(msg):
    rospy.loginfo("我订阅的消息:%s",msg.data)

if __name__ == '__main__':
    rospy.init_node('huahua')
    sub=rospy.Subscriber('che',String,doMsg,queue_size=10)
    rospy.spin()#循环订阅