# 引入time, os, sched，这三个是必备的
import time, os, sched


# 1.周期性一直执行
# time.time 参数返回从某个特定的时间到现在经历的秒数
# time.sleep 参数衡量的时间
schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    # enter 计划多少秒后，再次启动自己并进行运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)


def timming_exe(cmd, inc=1):
    # enter从现在起第n秒开始运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    # 运行结束
    schedule.run()


print(" 这里写你的调试信息 ")
timming_exe("echo %time%", 1)


# 2.执行有限次
# time.time 参数返回从某个特定的时间到现在经历的秒数
# time.sleep 参数衡量的时间
schedule = sched.scheduler(time.time, time.sleep)

# 打印时间的函数
def perform_command(cmd, inc):
    # enter 计划多少秒后，再次启动自己并进行运行
    # 重复调用自己，打印时间的函数一直进行下去
    # schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)


# 根据主函数提供的次数调用i次perform_command循环函数
def timing_exe(cmd, inc= 1):
    # enter从现在起第n秒开始运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    # 运行结束
    schedule.run()

# 主函数 增加输入框，确定执行次数
def times_count():
    max_count = int(input("请输入打印的次数： "))
    for i in range(max_count):
        timing_exe("echo %time%", 1)
        i += 1


print(" 这里写你的调试信息 ")
times_count()