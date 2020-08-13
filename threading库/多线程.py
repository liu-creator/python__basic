import threading


# 守护主线程
# work_thread = threading.Thread(target=work,damon=True)
# work_thread.setDaemon(True)

# 获取当前线程的 线程对象
# current_thread = threading.current_thread()
# print(current_thread)
# 多线程之间执行是无序的，是由CPU调度的，并发执行，只能占用一个核，不能多核。进程可以并行，多核，但是资源消耗大

import os
import threading
import time


def copy_file (file_name, source_dir, dest_dir):
    source_path = source_dir + "/" +file_name
    dest_path = dest_dir + "/" + file_name

    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break
    print("\n" + "正在复制：" + file_name)
    print("当前进程号为： " + str(os.getpid()))
    print("当前进程父进程号为： " + str(os.getppid()))
    time.sleep(0.3)


if __name__ == '__main__' :
    source_dir= r"D:\电脑桌面\编程\img\cosplay美女性感大长腿写真图片"
    dest_dir= r"D:\电脑桌面\图片"

    try:
        os.mkdir(dest_dir)
    except :
        print("目标文件夹已经存在")

    file_list = os.listdir(source_dir)
    for file_name in file_list:
        sub_process = threading.Thread(target=copy_file,
                                       args=(file_name,source_dir, dest_dir))
        # sub_process.daemon=True
        sub_process.start()
    print("当前进程号为：", os.getpid())
    print("\n"+"多进程复制程序执行完毕！！！")