import os
path = r'D:\电脑桌面\编程\img'
path_read = []    # path_read saves all executable files


def check_if_dir(file_path):
    temp_list = os.listdir(file_path)    # put file name from file_path in temp_list
    for temp_list_each in temp_list:
        if os.path.isfile(file_path + '/' + temp_list_each):
            temp_path = file_path + '/' + temp_list_each
            if os.path.splitext(temp_path)[-1] == '.jpg':    # 自己需要处理的是.jpg文件,所以在此加一个判断
                path_read.append(temp_path)
            else:
                continue
        else:
            check_if_dir(file_path + '/' + temp_list_each)    # loop traversal
    print(path_read)
    print("提取的文件总数为：{}个".format(len(path_read)))


check_if_dir(path)