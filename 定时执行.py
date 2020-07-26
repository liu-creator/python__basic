# 引入time, os
# 设置指定的时间，间隔多少后再次执行命令

import time, os


def re_exe(cmd, inc=0.5):
    run_times = 0
    while True:
        os.system(cmd)
        run_times += 1
        print("程序已执行{}次\n".format(run_times))
        time.sleep(inc)


re_exe("echo %time%", 0.5)
