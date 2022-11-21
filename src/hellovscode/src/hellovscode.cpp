#include "ros/ros.h"
int main(int argc, char **argv)
{
    //解决乱码
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "hello_c");
    ROS_INFO("Hello,vscode,我试试");

    return 0;   
}