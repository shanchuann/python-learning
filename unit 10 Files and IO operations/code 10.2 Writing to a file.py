# 打开文件
f = open('test.txt', 'w')
# 写入文件
f.write('Hello, World!')
# 关闭文件
f.close()

f = open('test1.txt', 'w')
f.write('Hello, World!\n')
f.write('Hello, World!\n')

context = ['Hello, World!\n', 'Hello, World!\n']
for line in context:
    f.write(line)
# 关闭文件
f.close()