# 打开文件
from fileinput import filename

f = open('test.txt')
# 读取文件
context = f.read()
# 打印文件内容
print(context)
# 关闭文件
f.close()

f = open('../unit 10 Files and IO operations/test.txt')  # 相对路径
context = f.read()
print(context)
f.close()

f = open('D:/Python/Python_code/python-learning/unit 10 Files and IO operations/test.txt')  # 绝对路径
context = f.read()
print(context)
f.close()

# 路径获取
import os
path = os.getcwd()
print(path)
filename = path + '/test.txt'
print(filename)
f = open(filename,mode = 'r',encoding = 'GBK')
context = f.read()
print(context)

context = f.read(5)
print(context)
context = f.readline()
print(context)
context = f.readlines()
print(context)
f.close()