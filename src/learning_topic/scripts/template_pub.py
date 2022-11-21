#!/usr/bin/env python    
# 上边一行称为 shebang line, 指定运行该文件的程序。
# 此处是说用从 PATH 环境变量中找到的第一个 python 程序执行该文件。
# 如果要更加具体地指定执行文件，可以用 #!<path>/python 
# 指明用该路径下的 python 程序执行该文件。

import rospy   
# 调用 rospy module，这是所有 python node 需要加载的一个 module
from std_msgs.msg import String  
# 由于后边在构造 Publish message 时用到了 std_msgs/String 类型的 ROS 数据
# 所以要先调用相关的 module 中的 class，即 std_msgs.msgs.String 类。
# 在构造 msg 时，可以用 msg=String() 的方式初始化对象
# 注意：用 python 编写的 node 程序本质上依然是 python 程序文件
# 里面用到的 import 等调用命令还是要去 PYTHONPATH 指定的路径寻找相应的 module。
# 所以 ROS 的各种 module 必须在 PYTHONPATH 的路径中才行。
# 其实在 source ROS 的各种 .bash 文件或者 install 各种 ROS package 的时候
# 就已经将这些 module 放到 PYTHONPATH 中了。

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) 
    # 创建一个 pub 对象，pub 对象有个 method —— pub.publish() 可以被用来
    # 向 chatter 这个 topic 上发送类型为 String 的数据。
    # 这里就用到了 String class，所以需要在开头的时候调用相应的 module
    # 我感觉创建 pub 的这句命令放到后边更合适，将创建 node 的 init_node 命令做为最早的命令
    rospy.init_node('talker', anonymous=True)
    # 初始化 node，名字为 talker，有了名字，node 才开始与 master 以及其他 node 通信 
    # ROS graph 中可能存在多个重名的 node，例如多个 turtle node，当令 anonymous=True 时，
    # 重名 node 会自动在名字后边加上随机数以示区别。
    rate = rospy.Rate(10) 
    # 产生一个 rospy.Rate Class 的对象 rate，它有一个 method —— rate.sleep()
    # 可以控制 loop 的频率。
    # 比如每秒钟 loop 10次，如果一次 loop 小于 1/10 秒，则 sleep 等待，确保 1秒 完成10个 loop。
    # 很显然这里的前提是，每个 loop 不能超过 1/10 秒，否则单靠 sleep 是无法达到期望的 loop 频率的 
    while not rospy.is_shutdown():
        # 监控着是否程序是否被关闭，例如 ctrl + c 等
        hello_str = "hello world %s" % rospy.get_time()
        # 这里的字符串就是 std_msgs/String 类型的。rospy.get_time() 可以返回当前时间
        rospy.loginfo(hello_str)
        # 默认情况下 info 会被写到三个地方：1.屏幕，2.log 文件，3.rosout topic
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':  
# 当该程序作为主程序运行时，满足此条件。
# 如果该程序作为 module 被另一个程序调用，则 if 条件不成立，后边的都不会执行。
    try:
        talker()
    except rospy.ROSInterruptException:  
        pass
    # handle error, 看 talker() 程序是否能够正常运行，如果可以正常运行，则按照 talker() 中的命令运行； 
    # 如果运行 talker() 程序报错，则执行 except block 中的命令，即 pass， 
    # 实际上是什么都不做，结束程序，此时不会出现 error 提示信息。
    # 如果要求不这么严谨，也可以不用 try ... except 形式，直接调用 talker() 就行。