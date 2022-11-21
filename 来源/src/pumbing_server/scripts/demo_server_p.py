#! /usr/bin/env python
import rospy
from pumbing_server.srv import AddIntsRequest,AddInts,AddIntsResponse
# from pumbing_server import *
'''
服务端:解析客户端,产生响应
导包
初始化
创建服务端对象
处理逻辑(回调函数)
spin()


'''
#参数是封装的请求数据,返回值是响应的数据
def doNum(request):
    #解析提交的数据
    num1 = request.num1
    num2 = request.num2
    sum =num1 + num2
    #将结果封装进响应
    response=AddIntsResponse()
    response.sum=sum

    rospy.loginfo("服务器解析的数据num1=%d,num2=%d,响应的结果:sum=%d",num1,num2,sum)

    return response

if __name__ == '__main__':
    rospy.init_node('heisui')
    server = rospy.Service('addInts',AddInts,doNum)
    rospy.loginfo('服务器已启动')
    rospy.spin()
