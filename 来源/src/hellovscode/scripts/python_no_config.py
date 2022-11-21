#!/usr/bin/env python
#上面一行是在声明python的解释器,也可以是python3
#当不配置的时候可能出错

import rospy
if __name__ == '__main__':
    rospy.init_node('hello_p2')
    rospy.loginfo('Hello,vscode,号厉害22222222222222')
    