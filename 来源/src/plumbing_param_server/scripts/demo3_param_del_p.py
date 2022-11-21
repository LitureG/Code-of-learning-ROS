#! /usr/bin/env python

import rospy
'''
演示示例里的删除
delete_param()

'''
if __name__ == '__main__':
    rospy.init_node('del_param')
    try:

        rospy.delete_param("radius")
    except Exception as e:
        rospy.loginfo("parameter does not exist")

    
