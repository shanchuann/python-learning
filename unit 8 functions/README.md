# 函数

## 形参和实参

函数定义时的参数叫做形参，调用函数时传递的参数叫做实参。

```python
def add(x, y): # x 和 y 是形参
    return x + y

print(add(1, 2)) # 实参 1 和 2 传递给了形参 x 和 y
```

## 函数的返回值

函数可以返回一个值，也可以不返回值。

```python
def add(x, y):
    return x + y

print(add(1, 2)) # 3
```

## 函数的参数类型
### 位置参数
要求实参的顺序和形参的顺序一致,由形参的顺序来决定实参的位置
```python
def add(x, y):
    return x + y

print(add(1, 2)) # 3
```

### 缺省参数
定义函数时，可以给参数设置默认值，这样在调用函数时，如果不传递参数，就会使用默认值。
```python
def add(x, y=2):
    return x + y

print(add(1)) # 3

print(add(1, 3)) # 4
```

### 可变参数
定义函数时，可以使用可变参数，这样在调用函数时，可以传递任意数量的参数。
```python
def add(*args):
    return sum(args)

print(add(1, 2, 3)) # 6
```

## 变量的作用域
变量的作用域分为局部变量和全局变量。

### 局部变量
在函数内部定义的变量，只能在函数内部使用，称为局部变量。
```python
def add(x, y):
    z = x + y
    return z

print(add(1, 2)) # 3
# print(z) # NameError: name 'z' is not defined
```

### 全局变量
在函数外部定义的变量，可以在函数内部使用，称为全局变量。
```python
z = 0

def add(x, y):
    global z
    z = x + y
    return z

print(add(1, 2)) # 3
print(z) # 3
```
global 关键字可以在函数内部修改全局变量的值。声明的为不可变类型

## 匿名函数
使用 lambda 关键字定义匿名函数。
```python
add = lambda x, y: x + y

print(add(1, 2)) # 3
```

### 累加,过滤,映射
```python
from functools import reduce

# 累加
print(reduce(lambda x, y: x + y, [1, 2, 3, 4])) # 10

# 过滤
print(list(filter(lambda x: x > 2, [1, 2, 3, 4]))) # [3, 4]

# 映射
print(list(map(lambda x: x * 2, [1, 2, 3, 4]))) # [2, 4, 6, 8]
```

## 内置函数
Python 内置了很多函数，可以直接使用。

### 数学函数
```python
print(abs(-1)) # 1  绝对值
print(max(1, 2, 3)) # 3  最大值
print(min(1, 2, 3)) # 1  最小值
print(pow(2, 3)) # 8  幂
print(round(1.5)) # 2  四舍五入
```

### 类型转换函数
```python
print(int(1.5)) # 1  转换为整数
print(float(1)) # 1.0  转换为浮点数
print(str(1)) # '1'  转换为字符串
```

### 序列函数
```python
print(all([True, False])) # False  所有元素都为 True 返回 True
print(any([True, False])) # True  任意一个元素为 True 返回 True
print(len([1, 2, 3])) # 3  返回序列的长度
print(sorted([3, 2, 1])) # [1, 2, 3]  返回排序后的序列
```

### 其他函数
```python
print(dir([])) # 列出对象的所有属性和方法  
print(help([])) # 查看对象的帮助信息
print(isinstance([], list)) # True  判断对象是否是指定类型
print(range(1, 10)) # range(1, 10)  生成一个序列
print(sum([1, 2, 3])) # 6  求和
```

## 递归函数
函数调用自身的函数称为递归函数。

1. 写出临界条件
2. 找出这一次和上一次的关系
3. 假设当前函数已经能调用,调用自身计算上一次的结果,在求出本次的结果当满足一个条件时,函数不再调用自身,返回结果
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 120
```


