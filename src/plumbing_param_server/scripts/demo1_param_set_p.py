#! /usr/bin/env python

import rospy
'''
演示示例里的增删
在参数服务器里设置机器人的属性,型号,半径
rospy.set_param()

'''
if __name__ == '__main__':
    rospy.init_node('param_set_p')
    rospy.set_param('type', 'yellowcar')
    rospy.set_param('radius', 0.2)
    #修改参数,后面的参数会覆盖前面的.更改后要再次运行此程序才能更改
    rospy.set_param('radius', 0.1)

    
