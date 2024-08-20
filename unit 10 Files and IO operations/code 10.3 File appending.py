# 文件追加
f = open('test1.txt', 'a')
f.write('This is a test\n')
f.close()
f = open('test1.txt', 'r')
print(f.read())
f.close()
