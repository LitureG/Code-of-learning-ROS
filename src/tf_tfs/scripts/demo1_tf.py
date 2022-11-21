#! /usr/bin/env python
import rospy,tf2_ros,tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
'''在静态的基础上修改三处即可
订阅方:订阅坐标变换消息,传入被转换的坐标点,调用算法
    导包
    初始化
    创建订阅对象
    组织被转换的坐标点
    转换逻辑实现,调用tf封装的算法
    输出结果
    (spin)


'''
if __name__ == '__main__':
    rospy.init_node('tf_vel_ctrl')
    #创建缓存对象,
    buffer = tf2_ros.Buffer()
    #创建订阅对象,传入缓存
    sub=tf2_ros.TransformListener(buffer)

    ps= tf2_geometry_msgs.PointStamped()
    ps.header.stamp = rospy.Time()

    ps.header.frame_id = 'son1'
    ps.point.x=1.0
    ps.point.y=2.0
    ps.point.z=3.0
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:   
            #计算son1相对于son2的坐标关系   
            ts=buffer.lookup_transform('son1', 'son2',rospy.Time(0))
            rospy.loginfo("父极坐标系:%s,子极坐标系:%s",
                    ts.header.frame_id,
                    ts.child.frame_id
                    )
            ps_out=buffer.transform(ps,'son2')
            rospy.loginfo("转换后的坐标:%.2f,%.2f,%.2f,参考的坐标系是:%s",
                        ps_out.point.x,
                        ps_out.point.y,
                        ps_out.point.z,
                        ps_out.header.frame_id
                        )
        except Exception as e:
            rospy.logwarn("Failed to %s",e)

        rate.sleep()
