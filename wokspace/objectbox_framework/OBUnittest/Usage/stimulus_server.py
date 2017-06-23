#coding=utf-8
"""
server:
模拟TAE执行，后台线程一直运行，里面存取了一些数据对象
pythonrunner对象可以运行python文件，python文件中可以操作server中的对象
池子里的对象有一个listener的列表吧
另一个（或者同一个）线程接收命令，对池子中的对象操作，如果池子中的对象发生了状态变化，通知监听者
命令可以用一个list来存储，增加时，自动触发处理命令
client:
向命令池中填入命令
对象的获取是通过id，或者引用方式

框架真正搭建好以后，如果需要操作底层对象，有两种方式：
1.通过代理对象操作
  * 客户使用这种情况时，应该对代理机制比较了解
  * 还需要有一个注册表，用来查看所有的对象信息
2.直接运行python脚本（这里模拟这种情况）
  * 需要保证底层对象就封装了listeners
  * 魔法：脚本里面也可以操作代理对象:)
"""
import OBBase.ob_global
import OBBase.ob_base
import OBBase.server_state

#等待命令，根据输入执行不同的脚本，查看对象状态
#执行python时，应该是多线程调用的
#对有些属性操作，应该是线程安全的

#对于GUIAST应该也是多线程调用的，这样可以组建多个GUIAST对象，并发执行
notOver = True
while notOver:
    command = raw_input("Enter your input: ")
    #init
    #组建一个对象池（实际可能是反序列化得到的），并添加一些观察者（模拟gui，或者对象池中其他的对象）
    if command == '1':
        execfile('Scripts//script1.py')
    #change some thing(open)
    #改变对象池中状态变化
    elif command == '2':
        execfile('Scripts//script2.py')
    #change other thing(exec)
    #改变对象池中状态变化
    elif command == '3':
        execfile('Scripts//script3.py')
    #close matlab
    elif command == '4':
        execfile('Scripts//script4.py')
    #terminate
    elif command == '5':
        notOver = False

