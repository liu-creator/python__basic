import sched
import threading
import time

# 一、延迟运行事件
# 生成调度器
scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name):
    print ('EVENT:', time.time(), name)


# print ('START:', time.time())

# 分别设置在执行后2秒、3秒之后执行调用函数
# scheduler.enter(2, 1, print_event, ('first',))
# scheduler.enter(延迟时间，优先级，函数名，（函数参数，）)
scheduler.enter(2, 1, print_event, ('first',))
scheduler.enter(3, 1, print_event, ('second',))


# 运行调度器
# scheduler.run()


# # 二、重叠事件
# # 　　调用run()块执行所有的事件。每个事件都在同一线程中运行，所以如果一个事件需要更长的时间，延迟事件将会有重叠。
# # 为了不丢失事件，延迟事件将会在之前事件运行完再被执行，但一些延迟事件可能会晚于原本计划的事件。
#
#
# scheduler = sched.scheduler(time.time, time.sleep)
#
# def long_event(name):
#     print('BEGIN EVENT :', time.time(), name)
#     time.sleep(2)
#     print('FINISH EVENT:', time.time(), name)
#
# print('START:', time.time())
# scheduler.enter(2, 1, long_event, ('first',))
#
# # 事件无法在设想的3秒后执行，将会顺延执行
# scheduler.enter(3, 1, long_event, ('second',))
#
# scheduler.run()


# 四、取消事件
# 利用enter()和enterabs()返回一个引用事件用来取消它。
scheduler = sched.scheduler(time.time, time.sleep)

# 建立一个全局 线程计数器
counter = 0


def increment_counter(name):
    global counter
    print('EVENT:', time.time(), name)
    counter += 1
    print('NOW:', counter)


print('START:', time.time())
e1 = scheduler.enter(2, 1, increment_counter, ('E1',))
e2 = scheduler.enter(3, 1, increment_counter, ('E2',))

# 开始一个线程执行事件
t = threading.Thread(target=scheduler.run)
t.start()

# 在主线程,取消第一个预定事件
scheduler.cancel(e1)

# 等待线程调度程序完成运行
t.join()