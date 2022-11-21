#! usr/bin/env python

import rospy
from std_msgs.msg import String

'''
    使用python实现消息发布
    1.导库
    2.初始化ros节点
    python无需节点句柄
    3.创建发布者对象
    4.编写发布逻辑并发布数据
'''

if __name__ == '__main__':  
    rospy.init_node('sandai')
    pub = rospy.Publisher('che',String,queue_size=10)
    #创建数据
    msg=String()
    #指定发布频率
    rate=rospy.Rate(1)
    #设置计数器
    count=0
    #休眠等待注册完毕
    rospy.sleep(3)
    while not rospy.is_shutdown():
        count+=1

        msg.data='hello'+str(count)

        pub.publish(msg)

        rospy.loginfo('发布的数据：%s',msg.data)
        rate.sleep()