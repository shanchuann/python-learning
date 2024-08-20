# 模块

## 模块的导入和使用

模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用python编程的一个重要的方式。
想要使用一个模块，你可以用`import`语句，语法如下：

```python
import module1[, module2[,... moduleN]
```

在模块中定义全局变量,函数,类等，然后在其他程序中导入模块，就可以使用模块中定义的全局变量,函数,类等。

```python
# 定义一个模块
# 文件名: module.py
def print_func( par ):
    print ("Hello : ", par)
    return
```

```python
# 导入模块
import module

# 现在可以调用模块里包含的函数了
module.print_func("Runoob")
```

### from...import 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

```python
from modname import name1[, name2[, ... nameN]]
```

例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：

```python
from fib import fibonacci
```

### from...import* 语句

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

```python
from modname import *
```

这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。

### 模块函数重命名

你可以使用`as`关键字来重命名模块函数名，语法如下：

```python
from modname import name as name1
```

例如：

```python
from fib import fibonacci as fb
```

## 包的使用
包是Python模块的一种组织形式，它将模块包含在文件夹中，形成一个大的Python工具库。文件夹中还有一个`__init__.py`文件的目录,他定义了包的属性和方法。

例如，我们有一个包`mypackage`，它有如下目录结构：

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

如果我们想要导入`module1`，我们可以使用如下语句：

```python
import mypackage.module1
```

或者：

```python
from mypackage import module1
```

## 模块搜索路径

当解释器遇到import语句，如果模块在当前的搜索路径就会被导入。

搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块，解释器首先搜索当前目录，然后是shell变量PYTHONPATH包含的目录，如果都找不到，Python会寻找默认路径。

模块搜索路径存储在`sys`模块的`path`变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

## PYTHONPATH变量

PYTHONPATH是Python编译器所使用的环境变量，它会在解释器寻找模块的路径中起作用。当一个模块被导入，Python会搜索模块的搜索路径，如果模块没有找到，会抛出一个`ModuleNotFoundError`异常。

PYTHONPATH是一个包含目录名的列表，Python解释器会从列表中的第一个目录开始搜索，直到找到所需的模块。

### 新建 ./my_module.py 文件来进行测试及演示

### random模块

Python的random模块用于生成随机数。下面是random模块的一些常用函数：

| 函数 | 描述 |
| --- | --- |
| random() | 生成一个0到1之间的随机浮点数 |
| uniform(a, b) | 生成一个a到b之间的随机浮点数 |
| randint(a, b) | 生成一个a到b之间的随机整数 |
| randrange(start, stop, step) | 从指定范围内，按指定基数递增的集合中获取一个随机数 |
| choice(seq) | 从序列中获取一个随机元素 |
| shuffle(seq) | 将序列的所有元素随机排序 |
| sample(seq, n) | 从指定序列中随机获取n个元素 |

#### random小游戏
1. 石头剪刀布
2. 猜数字

## 正则表达式

正则表达式是一个特殊的字符序列，帮助你检查一个字符串是否与某种模式匹配。

可以用于文本搜索,替换,分割等操作。

Python自带re模块，它提供了对正则表达式的支持。

### re模块的函数

| 函数 | 描述 |
| --- | --- |
| re.match() | 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none |
| re.search() | 扫描整个字符串并返回第一个成功的匹配 |
| re.sub() | 替换字符串中的匹配项 |
| re.compile() | 编译正则表达式，生成一个正则表达式对象，供match()和search()使用 |

### 正则表达式语法

| 字符 | 描述 |
| --- | --- |
| ^ | 匹配字符串的开头 |
| $ | 匹配字符串的末尾 |
| . | 匹配任意字符，除了换行符 |
| [...] | 匹配括号中的任意一个字符 |
| [^...] | 匹配不在括号中的任意一个字符 |
| * | 匹配前面的子表达式零次或多次 |
| + | 匹配前面的子表达式一次或多次 |
| ? | 匹配前面的子表达式零次或一次 |
| {n} | 匹配前面的子表达式n次 |
| {n,} | 匹配前面的子表达式至少n次 |
| {n, m} | 匹配前面的子表达式n到m次 |
| a\|b | 匹配a或b |
| () | 匹配括号中的表达式，也表示一个组 |
| \w | 匹配字母数字下划线 |
| \W | 匹配非字母数字下划线 |
| \s | 匹配任意空白字符 |
| \S | 匹配任意非空白字符 |
| \d | 匹配任意数字 |
| \D | 匹配任意非数字 |
| \b | 匹配一个单词边界 |
| \B | 匹配非单词边界 |
| \A | 匹配字符串的开始 |
| \Z | 匹配字符串的结束 |
| \z | 匹配字符串的结束，如果是存在换行，只匹配到换行前的结束字符串 |
| \G | 匹配最后匹配完成的位置 |
| \t | 匹配制表符 |
| \n | 匹配换行符 |

### re模块的使用

```python
import re

# re.match()
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
    
# re.search()
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)    
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

# re.sub()
phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)
```

### 正则表达式实例

1. 验证手机号码
2. 验证邮箱
3. 验证身份证号码
4. ...

## 时间和日期

Python提供了一个time和calendar模块用于格式化日期和时间。

### time模块

time模块包含了以下内置函数：

| 函数 | 描述 |
| --- | --- |
| time() | 返回当前时间的时间戳 |
| localtime() | 将一个时间戳转换为当前时区的struct_time |
| gmtime() | 将一个时间戳转换为UTC时区的struct_time |
| mktime() | 将一个struct_time转换为时间戳 |
| asctime() | 将一个struct_time转换为格式化时间字符串 |
| ctime() | 将一个时间戳转换为格式化时间字符串 |
| strftime() | 格式化时间字符串 |

### calendar模块

calendar模块包含了以下内置函数：

| 函数 | 描述 |
| --- | --- |
| calendar(year, w=2, l=1, c=6) | 返回一个多行字符串格式的year年年历 |
| month() | 返回一个多行字符串格式的month月日历 |
| monthcalendar(year, month) | 返回一个整数的单层嵌套列表，每个子列表是一个星期 |
| prcal(year, w=2, l=1, c=6) | 直接打印year年的日历 |
| prmonth(year, month, w=2, l=1) | 直接打印month月的日历 |

### time和calendar模块的使用

```python
import time
import calendar

# time模块
ticks = time.time()
print("当前时间戳为：", ticks)
    
localtime = time.localtime(time.time())
print("本地时间为：", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为：", localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# calendar模块
cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历：")
print(cal)
```

## turtle库

turtle是Python的一个图形库，它使得非常容易的绘制图形。

### turtle库的使用

```python
import turtle

turtle.speed(1)  # 设置画笔移动速度
turtle.pensize(2)  # 设置画笔宽度
turtle.pencolor("blue")  # 设置画笔颜色

turtle.forward(100)  # 向前移动100像素
turtle.right(90)  # 向右旋转90度

turtle.done()  # 保持窗口打开
```

## socket库(./code 9.7 socket)

Python的socket库提供了对网络通信的支持。

### socket库的使用

```python
    
import socket

# 创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 12345

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于1024字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))
```

## 安装第三方库

### pip工具

pip是Python的包管理工具，它可以安装、卸载、升级Python包。

### 安装第三方库

```bash
pip install package_name
```

### 卸载第三方库

```bash
pip uninstall package_name
```

### 升级第三方库

```bash
pip install --upgrade package_name
```

### 查看已安装的第三方库

```bash
pip list
```

### 查看第三方库的信息

```bash
pip show package_name
```

### 导出已安装的第三方库

```bash
pip freeze > requirements.txt
```

### 从requirements.txt文件安装第三方库

```bash
pip install -r requirements.txt
```