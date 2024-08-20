# 文件及IO操作

## 文件的基本概念
文件是以计算机硬盘为载体储存在计算机上的信息集合。 
文件可以是文本，文档，图片，程序等等。 
计算机文件基本上分为2种:二进制文件(没有统一的字符编码)和(纯文本文件有统一的编码,可以被看作存储在硬盘上的长字符串)

纯文本文件编码格式常见的有:
ASCII,ISO-8859-1,GB2312,GBK,UTF-8,UTF-16等

二进制文件与文本文件的一个最主要的区别在于是否有统一的字符编码格式,
二进制文件顾名思义是直接由0与1组成，无统一的字符编码.如图片文件(jpg,png)和视频文件(avi)等。 

### 绝对路径和相对路径
绝对路径：从根目录开始的路径

相对路径：相对于当前文件的路径

### 读取文件的步骤

1. 打开文件
2. 读取文件
3. 关闭文件

## 文件的读取

### 文件的打开
    
```python
f = open('test.txt', 'r')
```

### 文件的读取

```python
content = f.read()
print(content)
```

### 文件的关闭

```python
f.close()
```

### 文件的读取方式

- read() 读取文件的全部内容
- read(n) 读取文件的前n个字符
- readline() 读取文件的一行
- readlines() 读取文件的所有行，返回一个列表
- for line in f: 逐行读取文件
- f.tell() 返回文件指针的位置
- f.seek(offset, whence) 移动文件指针
- f.write() 写入文件
- f.writelines() 写入多行
- f.flush() 刷新文件缓冲区
- f.close() 关闭文件

## 打开文件的模式

- r 只读,默认模式,文件必须存在,否则抛出异常
- w 只写,文件不存在则创建,存在则清空
- a 追加,文件不存在则创建,存在则追加
- r+ 读写,文件必须存在,否则抛出异常
- w+ 读写,文件不存在则创建,存在则清空
- a+ 读写,文件不存在则创建,存在则追加
- b 二进制模式,可与r,w,a,+组合使用,如rb,wb,ab,r+b,w+b,a+b,rb+,wb+,ab+,用于二进制文件操作

## 文件的迭代

```python
f = open('test.txt', 'r')
for line in f:
    print(line)
f.close()
```

## 文件的写入

```python
f = open('test.txt', 'w')
f.write('hello world')
f.close()
```

## 文件的追加

```python
f = open('test.txt', 'a')
f.write('hello world')
f.close()
```

## with语句

```python
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)
```
## csv文件

### csv文件的读取

```python
import csv

with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### csv文件的写入

```python
import csv

with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Tom', 20])
    writer.writerow(['Jerry', 22])
```