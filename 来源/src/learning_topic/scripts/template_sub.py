#!/usr/bin/env python
# 第一句依然是 shebang line，指定运行该文件的程序
import rospy
from std_msgs.msg import String

def callback(data):
    # 尽管在 Subscriber 语句中没有给 callback 加参数
    # 但是在执行中默认将接受到的 msg 作为参数传递过来
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # std_msgs/String 类型的变量结构为 `string: data`，
   # 即 msg 的值是存储在 string 基本类型的 data field 中。 
def listener():
    rospy.init_node('listener', anonymous=True)
    # 初始化 node，名为 listener，如果有重名的就在后边加随机数，以示区分
    rospy.Subscriber("chatter", String, callback)
    # 监听 chatter topic 上的 std_msgs/String 类型的数据，一旦收到数据，就调用 callback 函数，
    # 其中函数的第一个 argument 总是接受到的数据。

    rospy.spin()
    # 在 C++ 中，spin() 的作用是不断的循环，每次循环结束就令 callback 函数处理数据。
    # 但在 python 中 spin() simply keeps python from exiting until this node is stopped。 
   # callback functions 不受 spin() 的影响，它们有自己的处理进程

if __name__ == '__main__':
    listener()