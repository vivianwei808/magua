import os
import xlwt

# 把某个目录下的文件名列到excel中
file_dir="/Volumes/3tb";
os.listdir(file_dir)
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet("文件名");
n=0
for i in os.listdir(file_dir):
    worksheet.write(n,0,i)
    n+=1
new_workbook.save('目录.xls');