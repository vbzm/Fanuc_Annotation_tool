# Fanuc_Annotation_tool
发那科工业机器人注释工具

# 文件介绍：
1、main2.py为主程序入口
2、其他文件为UI文件或多线程文件
3、img文件夹储存着程序所需的图片资源，img.qrc为Pyqt引用图片的方法

# 项目介绍：
本项目由==不知名网友==开发及维护，==微信公众号：不知名网友i==，与2023/8/7停止维护和更新，==请不要将此代码用于商业用途==。

# 发那科注释工具更新履历：

V1.0：
软件初版，没有UI，是使用windos黑窗口做交互使用，支持写入，删除，读出。
更新日期：未知

V2.0：
正式版本，更新UI，基于V1.0更新UI，以及添加机器人信息窗口。
更新日期：2023-1-7
文章：https://mp.weixin.qq.com/s/LR7rxOSHYU_RZYYlkS4mGw

v3.0：
基于V2.0版本添加，写入/删除，支持可选择功能。
更新时间：2023-3-18
文章：https://mp.weixin.qq.com/s/kpWK-UUJx1LEaEwCLpW38A

V3.1：
基于3.0版本添加功能，新增功能：
   1、支持自动寻址，即自动搜寻网段下可用IP进行设备添加。
     2、设备列表自动PING，若设备在线提示功能。
     3、发那科机器人变量遍历功能，模糊搜索功能添加。
更新时间：2023-3-27

V3.2
基于3.1版本优化功能
本次更新主为优化用户体验
1、关闭软件时较缓慢，已完成优化，原因为软件子线程阻塞了主线程关闭。
2、变量工具各种错误，已修复，原因为编码格式错误。
3、模糊搜索无法使用，已修复，原因为接口引用错误。
此版本为最后一个版本，不再更新。
