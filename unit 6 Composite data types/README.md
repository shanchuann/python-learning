# 组合数据类型

在Python中，有一些内置的数据类型，可以用来将多个数据组合在一起。这些数据类型被称为组合数据类型。Python中的组合数据类型有列表、元组、集合和字典。

## 序列

列表、元组和字符串都是序列类型，它们都支持一些共同的操作，如索引、切片、拼接、重复、成员检测等。

```python
# 索引
s = 'hello'
print(s[0])  # 输出: h

# 切片
print(s[1:4])  # 输出: ell

# 拼接
print(s + ' world')  # 输出: hello world

# 重复
print(s * 3)  # 输出: hellohellohello

# 成员检测
print('h' in s)  # 输出: True
```

序列类型还支持一些内置函数，如`len()`、`max()`、`min()`等。

```python
    
# 内置函数
s = 'hello'
print(len(s))  # 输出: 5
print(max(s))  # 输出: o
print(min(s))  # 输出: e
```

## 列表

列表是Python中最常用的数据类型之一。列表是一个有序的集合，可以存储任意数量的Python对象，包括数字、字符串、列表、元组、集合、字典等。列表用方括号`[]`来��示，列表中的元素之间用逗号`,`分隔。

```python
# 创建一个空列表
empty_list = []

# 创建一个包含整数的列表
int_list = [1, 2, 3, 4, 5]

# 创建一个包含字符串的列表
str_list = ['apple', 'banana', 'cherry']

# 创建一个包含列表的列表
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

列表是可变的，可以通过索引来访问和修改列表中的元素。列表的索引从0开始，可以使用负数索引来从列表末尾开始访问元素。

```python
# 访问列表中的元素
print(int_list[0])  # 输出: 1
print(str_list[1])  # 输出: banana
print(nested_list[1][2])  # 输出: 6

# 修改列表中的元素
int_list[0] = 10
print(int_list)  # 输出: [10, 2, 3, 4, 5]
```

列表还支持切片操作，可以通过切片来获取列表中的子列表。

```python
# 切片操作
print(int_list[1:4])  # 输出: [2, 3, 4]
print(str_list[:2])  # 输出: ['apple', 'banana']
print(nested_list[1][1:])  # 输出: [5, 6]
```

列表还支持一些常用的方法，如`append()`、`insert()`、`remove()`、`pop()`、`sort()`等。

```python
# 列表方法
int_list.append(6)  # 在列表末尾添加一个元素
print(int_list)  # 输出: [10, 2, 3, 4, 5, 6]

str_list.insert(1, 'orange')  # 在指定位置插入一个元素
print(str_list)  # 输出: ['apple', 'orange', 'banana', 'cherry']

int_list.remove(3)  # 移除列表中的指定元素
print(int_list)  # 输出: [10, 2, 4, 5, 6]
    
popped_element = int_list.pop()  # 移除并返回列表中的最后一个元素
print(popped_element)  # 输出: 6
print(int_list)  # 输出: [10, 2, 4, 5]

int_list.sort()  # 对列表进行排序
print(int_list)  # 输出: [2, 4, 5, 10]
```

## 元组

元组是Python中的另一个有序的集合数据类型。元组和列表类似，但是元组是不可变的，一旦创建后就不能修改。元组用圆括号`()`来表示，元组中的元素之间用逗号`,`分隔。

```python
# 创建一个空元组
empty_tuple = ()

# 创建一个包含整数的元组
int_tuple = (1, 2, 3, 4, 5)

# 创建一个包含字符串的元组
str_tuple = ('apple', 'banana', 'cherry')

# 创建一个包含元组的元组
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
```

元组的索引、切片和访问方式与列表相似。

```python
# 访问元组中的元素
print(int_tuple[0])  # 输出: 1
print(str_tuple[1])  # 输出: banana
print(nested_tuple[1][2])  # 输出: 6
```

元组是不可变的，不能修改元组中的元素。

```python
# 尝试修改元组中的元素会引发错误
int_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

## 集合

集合是Python中的一种无序的、不重复的数据类型。集合用大括号`{}`来表示，集合中的元素之间用逗号`,`分隔。

```python
# 创建一个空集合
empty_set = set()

# 创建一个包含整数的集合
int_set = {1, 2, 3, 4, 5}

# 创建一个包含字符串的集合
str_set = {'apple', 'banana', 'cherry'}
```

集合支持一些常用的集合操作，如并集、交集、差集等。

```python
# 集合操作
set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}

# 并集
union_set = set1 | set2
print(union_set)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# 交集
intersection_set = set1 & set2
print(intersection_set)  # 输出: {4, 5}

# 差集
difference_set = set1 - set2
print(difference_set)  # 输出: {1, 2, 3}
```

集合是可变的，可以通过`add()`、`remove()`等方法来修改集合。

```python
# 集合方法
str_set.add('orange')  # 向集合中添加一个元素
print(str_set)  # 输出: {'apple', 'banana', 'cherry', 'orange'}

str_set.remove('banana')  # 从集合中移除一个元素
print(str_set)  # 输出: {'apple', 'cherry', 'orange'}
```

## 字典

字典是Python中的一种无序的、可变的数据类型，用键-值对来存储数据。字典用大括号`{}`来表示，键和值之间用冒号`:`分隔，键-值对之间用逗号`,`分隔。

```python
# 创建一个空字典
empty_dict = {}

# 创建一个包含整数键的字典
int_dict = {1: 'one', 2: 'two', 3: 'three'}

# 创建一个包含字符串键的字典
str_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
```

字典可以通过键来访问和修改对应的值。

```python
# 访问字典中的元素
print(int_dict[1])  # 输出: one
print(str_dict['banana'])  # 输出: 2

# 修改字典中的元素
int_dict[1] = 'ONE'
print(int_dict)  # 输出: {1: 'ONE', 2: 'two', 3: 'three'}
```

字典还支持一些常用的方法，如`keys()`、`values()`、`items()`等。

```python
# 字典方法
print(str_dict.keys())  # 输出: dict_keys(['apple', 'banana', 'cherry'])
print(str_dict.values())  # 输出: dict_values([1, 2, 3])
print(str_dict.items())  # 输出: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])
```

## 总结

组合数据类型是Python中非常重要的数据类型，可以用来组织和存储复杂的数据结构。列表、元组、集合和字典分别提供了不同的功能和特性，可以根据具体的需求来选择合适的数据类型。在实际编程中，我们经常会使用这些组合数据类型来处理各种数据。