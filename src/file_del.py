# 文件管理
# 删除文件名含有"获取更多资源.html"的文件
import os
import re

pattern = re.compile('获取更多资源.html')
# for root,dirs,files in os.walk('/Users/wangwei/Downloads/编程必备基础 大话HTTP协议'):
# for root, dirs, files in os.walk('/Volumes/TOSHIBA EXT'):
for root, dirs, files in os.walk('/Volumes/3tb'):
    for name in files:
        file_path = os.path.join(root,name)
        matching = pattern.search(file_path)
        if(matching):
            print(file_path)
            # 删除文件
            os.remove(file_path)