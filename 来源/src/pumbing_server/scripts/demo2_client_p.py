#! /usr/bin/env python

import rospy
from pumbing_server.srv import *
'''
客户端,组织并提交请求,处理服务端响应
导包
初始化
创建客户端
组织请求数据,并发送请求
处理响应

优化:
动态输入参数

问题:
客户端先启动会报错
实现客户端先启动时挂起等待服务端启动
ros中内置函数可以实现
wait_for_service()
rospy.wait_for_service('话题名')
'''
if __name__=='__main__':
    #判断参数长度
    if len(sys.argv)!=3:
        rospy.logerr('传参个数错误')
        sys.exit(1)

    rospy.init_node('erhei')
    client = rospy.ServiceProxy('addInts',AddInts)
    #解析传入的参数
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])

    #client.wait_for_service()
    rospy.wait_for_service('addInts')

    responce=client.call(num1,num2)
    rospy.loginfo('响应的数据:%d',responce.sum)