# 面向对象程序设计

## 1. 面向对象程序设计的基本概念
    
面向对象程序设计是一种程序设计范式,它以对象作为基本单元,将数据和操作封装在对象中,以提高程序的可维护性和可重用性.
    
面向对象程序设计的基本概念: 
- 类和实例
- 对象的属性和方法
- 类属性和方法
- 面向对象的三大特性

### 类
类是一种抽象的数据类型,它定义了一类对象的共同属性和方法.类是对象的模板,对象是类的实例.

- 类的定义
```python
class 类名:
    # 类的属性
    属性1 = 值1
    属性2 = 值2
    ...
    
    # 类的方法
    def 方法1(self, 参数1, 参数2, ...):
        pass
    def 方法2(self, 参数1, 参数2, ...):
        pass
    ...

    # class 表明定义一个类,类名通常使用大写字母开头,类的属性和方法缩进,方法的第一个参数通常是 self,表示对象本身.
    # ClassName() 类的名字
    # () 父类集合的开始和结束
    # object 父类的名字，定义类继承自父类，默认是object，object是所有类的直接或间接父类
```
- 类的实例化
```python
# 类的实例化
# 对象名 = 类名()

class Person(object):  # 定义一个类
    name = 'Tom'
    age = 18
    def say_hello(self):
        print('Hello, I am', self.name)

p = Person()  # 实例化一个对象
p.say_hello()  # 调用对象的方法

```

### 实例（对象）
实例是类的具体实现,它具有类定义的属性和方法.

- 实例的属性和方法
```python
# 实例的属性和方法
# 对象名.属性名
# 对象名.方法名()

class Person(object):  # 定义一个类
    name = 'Tom'
    age = 18
    def say_hello(self):
        print('Hello, I am', self.name)
        
p = Person()  # 实例化一个对象
print(p.name)  # 访问对象的属性
p.say_hello()  # 调用对象的方法

```

## 2. 类和实例

### 类属性和方法
类属性和方法是类的属性和方法,它们属于类本身,而不是类的实例.

- 类属性和方法
```python
# 类属性和方法
# 类名.属性名
# 类名.方法名()

class Person(object):  # 定义一个类
    name = 'Tom'  # 类属性
    age = 18  # 类属性
    def say_hello(self):  # 类方法
        print('Hello, I am', self.name)
        
print(Person.name)  # 访问类的属性
Person.say_hello()  # 调用类的方法

```
## 3. 静态方法

静态方法是类的方法,它不需要访问类的属性和方法,也不需要访问实例的属性和方法.

- 静态方法
```python
# 静态方法
# @staticmethod
# 类名.方法名()

class Person(object):  # 定义一个类
    @staticmethod
    def say_hello():  # 静态方法
        print('Hello, I am Tom')
        
Person.say_hello()  # 调用静态方法
    
   ```

## 3. 面向对象的三大特性

面向对象的三大特性是封装、继承和多态.

### 类的继承

继承是一种类与类之间的关系,它允许一个类继承另一个类的属性和方法.

- 类的继承
```python
# 类的继承
# class 子类名(父类名):
#     pass

class Person(object):  # 定义一个类
    def say_hello(self):  # 类方法
        print('Hello, I am Tom')

class Student(Person):  # 定义一个子类
    def study(self):  # 类方法
        print('I am studying')

s = Student()  # 实例化一个对象
s.say_hello()  # 调用父类的方法
s.study()  # 调用子类的方法

```

### 多态

多态是一种对象的多种形态,它允许不同的对象对同一个方法做出不同的响应.

- 多态
```python
# 多态
# class 子类名(父类名):
#     pass

class Person(object):  # 定义一个类
    def say_hello(self):  # 类方法
        print('Hello, I am Tom')

class Student(Person):  # 定义一个子类
    def say_hello(self):  # 类方法
        print('Hello, I am Jack')

def say_hello(p):  # 多态
    p.say_hello()

p = Person()  # 实例化一个对象
s = Student()  # 实例化一个对象
say_hello(p)  # 调用父类的方法
say_hello(s)  # 调用子类的方法

```

### 封装

封装是一种将数据和操作封装在对象中的机制,它允许对象隐藏内部实现细节,只暴露必要的接口.

- 封装
```python
# 封装
# class 类名:
#     def __init__(self, 参数1, 参数2, ...):
#         self.属性1 = 参数1
#         self.属性2 = 参数2
#         ...

class Person(object):  # 定义一个类
    def __init__(self, name, age):  # 初始化方法
        self.name = name  # 实例属性
        self.age = age  # 实例属性
    def say_hello(self):  # 类方法
        print('Hello, I am', self.name)

p = Person('Tom', 18)  # 实例化一个对象
p.say_hello()  # 调用对象的方法

```
## 魔法方法

魔法方法是一种特殊的方法,它以双下划线开头和结尾,用于实现类的特殊功能.

- 魔法方法
```python
# 魔法方法
# class 类名:
#     def __init__(self, 参数1, 参数2, ...):
#         self.属性1 = 参数1
#         self.属性2 = 参数2

class Person(object):  # 定义一个类
    def __init__(self, name, age):  # 初始化方法
        self.name = name  # 实例属性
        self.age = age  # 实例属性
    def __str__(self):  # 魔法方法
        return 'Person(name=%s, age=%d)' % (self.name, self.age)

p = Person('Tom', 18)  # 实例化一个对象
print(p)  # 调用魔法方法

```

| 魔法方法 | 说明 | 魔法方法 | 说明 |
| :--- | :--- | :--- | :--- |
| `__str__` | 字符串表示方法 | `__init__` | 初始化方法 |
| `__repr__` | 表示方法 | `__len__` | 长度方法 |
| `__getitem__` | 获取元素方法 | `__setitem__` | 设置元素方法 |
| `__delitem__` | 删除元素方法 | `__iter__` | 迭代方法 |
| `__next__` | 下一个方法 | `__contains__` | 包含方法 |
| `__add__` | 加法方法 | `__sub__` | 减法方法 |
| `__mul__` | 乘法方法 | `__truediv__` | 除法方法 |
| `__floordiv__` | 地板除法方法 | `__mod__` | 取模方法 |
| `__pow__` | 幂方法 | `__eq__` | 等于方法 |

如果类中定义了这些魔法方法,则可以使用相应的运算符对对象进行操作.

```python
# 魔法方法
# class 类名:
#     def __init__(self, 参数1, 参数2, ...):
#         self.属性1 = 参数1
#         self.属性2 = 参数2
#     def __add__(self, other):
#         pass

class Person(object):  # 定义一个类
    def __init__(self, name, age):  # 初始化方法
        self.name = name  # 实例属性
        self.age = age  # 实例属性
    def __add__(self, other):  # 魔法方法
        return self.age + other.age

p1 = Person('Tom', 18)  # 实例化一个对象
p2 = Person('Jack', 20)  # 实例化一个对象
print(p1 + p2)  # 调用魔法方法

```
如果类中没有定义这些魔法方法,则会调用默认的魔法方法,通常会抛出异常.

```python
# 魔法方法
# class 类名:
#     def __init__(self, 参数1, 参数2, ...):
#         self.属性1 = 参数1
#         self.属性2 = 参数2

class Person(object):  # 定义一个类
    def __init__(self, name, age):  # 初始化方法
        self.name = name  # 实例属性
        self.age = age  # 实例属性

p1 = Person('Tom', 18)  # 实例化一个对象
p2 = Person('Jack', 20)  # 实例化一个对象
print(p1 + p2)  # 调用魔法方法

```



