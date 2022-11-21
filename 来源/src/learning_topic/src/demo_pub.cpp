#include "ros/ros.h"
#include "std_msgs/String.h"//ros中文本类型包含在该头文件中
#include "sstream"//
/*
        发布方实现:
        1.头文件

        2.初始化ros节点
        3.创建节点句柄
        4.创建发布者对象
        5.编写发布逻辑并发布数据

*/
int main(int argc, char* argv[]){
    setlocale(LC_ALL, "");  //解决乱码问题  
    ros::init(argc, argv, "ergouzi");
    ros::NodeHandle nh;
    ros::Publisher pub=nh.advertise<std_msgs::String>("che",10);
    //创建被循环发布的消息
    std_msgs::String msg;
    ros::Rate rate(1);
    int count=0;
    while (ros::ok()) {//ok(表示只要节点还运行就一直循环)
        count++;
        //msg.data = "hello"; 
        //实现字符串拼接
        std::stringstream ss;
        ss << "hello --->"<< count;
        msg.data = ss.str();
        pub.publish(msg);
        //添加日志
        ROS_INFO("发布的内容是:%s", ss.str().c_str());
        rate.sleep();
        }   
}