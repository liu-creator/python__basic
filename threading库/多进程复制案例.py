import os
import multiprocessing
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
    # print("当前进程父进程号为： " + str(os.getppid()))


if __name__ == '__main__' :
    start = time.time()

    source_dir= r"D:\电脑桌面\编程\img\cosplay美女性感大长腿写真图片"
    dest_dir= r"D:\电脑桌面\图片"

    try:
        os.mkdir(dest_dir)
    except :
        print("目标文件夹已经存在")

    file_list = os.listdir(source_dir)
    for file_name in file_list:
        sub_process = multiprocessing.Process(target=copy_file,
                                              args=(file_name,source_dir, dest_dir))
        # sub_process.daemon=True
        sub_process.start()
    time.sleep(0.5)
    print("\n"+"多进程复制程序执行完毕！！！")

    end = time.time()
    print(str('%.2f' % (end-start)))
    print("Running time: %.2f seconds" % (end - start))
    print("Running time: %s seconds" % (end - start))