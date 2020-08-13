import os
import time

# dir_name: 处理文件的起始目录
def count_file(dir_name):
    # 用于存目录的名字
    dir_list = []
    # 将当前目录下的所有文件列出
    file_list = os.listdir(dir_name)
    # 遍历当前文件名列表
    for file_name in file_list:
        # 如果是目录
        if os.path.isdir(file_name):
            dir_list.append(dir_name + "/"+ file_name)
        else:
            with open(file_name) as f:
                text_list = f.readlines()
                print(file_name, ":", text_list)
    # 处理目录
    for dir_path in dir_list:
        os.chdir(dir_path)
        count_file(dir_path)


dir_name = input("请输入文件夹路径：")

start = time.time()
count_file(dir_name)
end = time.time()

print(str(end))

