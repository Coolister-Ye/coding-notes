# 在MAC使用Crontab的可能遇到的问题

Crontab是一个定时任务的工具，可以在mac上安装和使用
https://www.runoob.com/linux/linux-comm-crontab.html

在mac中使用Crontab可能会遇到一下问题，这里做个记录

1. 使用crontab运行python定时任务

Crontab命令
```
* * * * * /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 /Users/me/Projects/57_auction_checker/web_service.py >> /Users/me/Projects/57_auction_checker/logs.log 2>&1
```
logs报错
```
/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/01379863/Desktop/Project/57_auction_checker/web_service.py': [Errno 1] Operation not permitted
```
解决方式
1. 主要是文件系统权限的问题，想MAC下的Desktop，Document等这些文件夹都有权限限制
2. 可以把整个项目放到用户文件夹下的一个新建文件夹
3. 网上还有另外一种方法，设置Security&Privacy下的Full Disk Access，将`/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python`加进去，但这里我进不去Application的包，所以是通过方式2解决的
