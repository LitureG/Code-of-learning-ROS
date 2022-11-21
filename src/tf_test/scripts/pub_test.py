#! /usr/bin/env python
import rospy

'''
发布方:
订阅乌龟位置信息,转换成坐标系的相对关系,在发布
    准备;
    话题:/turtle1/pose
    类型:/turtlesim/Pose

    liucheng
    导包
    初始化
    创建订阅者对象
    回调函数处理订阅的信息(核心)
    spin()


'''
from turtlesim.msg import Pose
import tf2_ros,tf
from geometry_msgs.msg import TransformStamped
import sys

#接受乌龟名变量
turtle_name =''

def doPose(pose):
    #创建发布坐标系相对关系的对象
    pub = tf2_ros.TransformBroadcaster()
    #将pose转换成坐标系相对关系信息
    ts = TransformStamped()
    ts.header.frame_id = 'world'
    ts.header.stamp = rospy.Time.now()
    ts.child_frame_id = turtle_name
    #子坐标系相对父坐标系的偏移量
    ts.transform.translation.x =pose.x
    ts.transform.translation.y =pose.y
    ts.transform.translation.z =0
    #四元数(欧拉角->四元数)
    '''
        乌龟是二维的,不存在翻滚和俯仰,只有偏航
        0 0 pose.theta

    '''
    qtn = tf.transformations.quaternion_from_euler(0,0,pose.theta)
    ts.transform.rotation.x = qtn[0]
    ts.transform.rotation.y = qtn[1]
    ts.transform.rotation.z = qtn[2]
    ts.transform.rotation.w = qtn[3]
    #发布
    pub.sendTransform(ts)

if __name__ == '__main__':
    rospy.init_node('dynamic_pub')
    #解析传入的参数,传入几个参数? 文件全路径+传入参数+节点名+日志文件路径
    if len(sys.argv) != 4:
        rospy.loginfo("Please provide encough parameters")
        sys.exit(1)
    else:
        turtle_name = sys.argv[1]

    sub = rospy.Subscriber(turtle_name+'/pose',Pose,doPose,queue_size=10)
    rospy.spin()