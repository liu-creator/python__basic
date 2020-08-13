import time
import threading


# 1.打印限定次数
def timer(n):
    '''''
    每n秒执行一次
    '''
    # while True:
    for n_each in range(n):
        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        # yourTask()  # 此处为要执行的任务
        time.sleep(1)
        n_each += 1

def input_1():
    n = int(input("请输入打印的次数："))
    return (n)

# 运行
# timer(input_1())


# 2.间隔特定时间打印
def timer_2(n=1):
    '''''
    每n秒执行一次
    '''
    while True:
        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        # yourTask()  # 此处为要执行的任务
        # 间隔n秒再执行
        time.sleep(n)


def input_2():
    n = float(input("请输入间隔时间："))
    return (n)


# timer_2(input_2())


# 3.  利用线程中的延时方法实现5秒后执行函数
def printHello():
    print("start")

# 运行
# threading.Timer(5, printHello).start()
