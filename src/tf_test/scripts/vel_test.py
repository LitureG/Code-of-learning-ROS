#! /usr/bin/env python
import math
import rospy,tf2_ros,tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped,Twist


if __name__ == '__main__':
    rospy.init_node('tf_vel_ctrl')
    #创建缓存对象,
    buffer = tf2_ros.Buffer()
    #创建订阅对象,传入缓存
    sub=tf2_ros.TransformListener(buffer)
    #创建速度消息发布对象
    pub=rospy.Publisher('/turtle2/cmd_vel',Twist,queue_size=100)

    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:   
            #计算son1相对于son2的坐标关系   
            ts=buffer.lookup_transform('turtle2', 'turtle1',rospy.Time(0))
            rospy.loginfo("父极坐标系:%s,子极坐标系:%s,偏移量:(%.2f,%.2f,%.2f)",
                    ts.header.frame_id,
                    ts.child_frame_id,#子和父的结构不一样
                    ts.transform.translation.x,
                    ts.transform.translation.y,
                    ts.transform.translation.z
                    )
            #组织 Twist 消息
            twist = Twist()
            #线速度计算=系数*两点之间的距离
            #角速度=系数*夹角(atan2(y,x))
            twist.linear.x =2*math.pow(ts.transform.translation.x,2) + math.pow(ts.transform.translation.y,2)
            twist.angular.z =4*math.atan2(ts.transform.translation.y,ts.transform.translation.x)

            pub.publish(twist)

        except Exception as e:
            rospy.logwarn("错误提醒: %s",e)

        rate.sleep()
