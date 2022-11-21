#! /usr/bin/env python

from unicodedata import name
import rospy
'''
演示参数查询
    get_param(键,默认值)
        当键存在时返回对应的值,不存在返回默认值
    get_param_cached
    get_param_names
    has_param
    search_param

'''

if __name__ == '__main__':
    rospy.init_node('get_param_p')
    #get_param
    radius=rospy.get_param('radius',0.52)
    radius2=rospy.get_param('radius_pxxx',0.3)
    rospy.loginfo('radius: %.2f,radius2: %.2f',radius,radius2)
    
    #get_param_cached(效率比上一个更高)
    radius3=rospy.get_param_cached('radius',0.52)
    radius4=rospy.get_param_cached('radius_pxxx',0.3)
    rospy.loginfo('radius3: %.2f,radius4: %.2f',radius3,radius4)

    #get_param_names()获取键名
    names = rospy.get_param_names()
    for name in names:
        rospy.loginfo('name= %s',name)
    
    #has_param判断是否含有某个键
    flag1=rospy.has_param('radius')
    if flag1:
        rospy.loginfo('radius exists')
    else:
        rospy.loginfo('radius does not exist')

    
    flag2=rospy.has_param('radiusxx')
    if flag2:
        rospy.loginfo('radiusxx exists')
    else:
        rospy.loginfo('radiusxx does not exist')

    #查找某个键是否存在,存在就返回键名
    key=rospy.search_param('radius')
    rospy.loginfo('key=%s',key)