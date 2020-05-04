# 文件管理
# 修改文件名----文件名含有_[itjc8.com]，重命名为去掉_[itjc8.com]的名称
import os
import re

pattern = re.compile('\[IT教程吧-www.itjc8.com\]_')
# for root,dirs,files in os.walk('/Users/wangwei/Downloads/编程必备基础 大话HTTP协议'):
# for root, dirs, files in os.walk('/Volumes/TOSHIBA EXT'):
for root, dirs, files in os.walk('/Volumes/3tb'):
    for name in files:
        file_path = os.path.join(root,name)
        matching = pattern.search(file_path)
        if(matching):
            start_index = matching.span()[0]
            end_index = matching.span()[1]
            last_path = file_path[end_index:-1] + file_path[-1];
            # print(last_path)
            try:
                if(last_path[0]=="/"):
                    rename = file_path[0:start_index]
                    num = int(start_index + len("[IT教程吧-www.itjc8.com]_"))
                    print(file_path[0:num], rename)
                    os.rename(file_path[0:num], rename)
                else:
                    rename = file_path[0:start_index]+last_path
                    print(file_path, rename)
                    os.rename(file_path, rename)
            except FileNotFoundError:
                print("==")
            # 重命名文件名
            # os.rename(file_path[0:num],rename);