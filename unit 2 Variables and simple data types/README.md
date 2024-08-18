# 变量与基础数据类型
## 变量
变量是程序中用于保存数据的占位符。Python 中的变量可以是任何数据类型，包括数字、字符串、列表、元组、字典等。变量在使用前必须先赋值，赋值操作使用等号（=）。
```python
message = "Hello Python world!"
print(message)
```
在上面的代码中，变量 `message` 被赋值为字符串 "Hello Python world!"，然后使用 `print()` 函数输出变量的值。

### 变量命名规则
- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线开头，但不能以数字开头。
- 变量名不能包含空格，但可以使用下划线来分隔单词。
- 例如，变量名 `my_name` 比 `myname` 更容易理解。
- 不要使用 Python 关键字和函数名作为变量名。
- 变量名应该简短且具有描述性，例如 `name` 比 `n` 更好。
- 慎用小写字母 `l` 和大写字母 `O`，因为它们可能被误认为数字 `1` 和 `0`。
- 变量名应该简短且具有描述性，例如 `name` 比 `n` 更好。

## 字符串
字符串是由字符组成的序列，可以使用单引号、双引号或三引号来创建字符串。
```python
name = 'ada lovelace'
print(name.title())
```
在上面的代码中，变量 `name` 被赋值为字符串 `'ada lovelace'`，然后使用字符串方法 `title()` 将字符串首字母大写。

### 字符串方法
- `title()`：将字符串中每个单词的首字母大写。
- `upper()`：将字符串中所有字母大写。
- `lower()`：将字符串中所有字母小写。
- `strip()`：删除字符串开头和末尾的空白字符。
- `lstrip()`：删除字符串开头的空白字符。
- `rstrip()`：删除字符串末尾的空白字符。
- `replace(old, new)`：将字符串中的 `old` 替换为 `new`。
- `split()`：将字符串分割为列表。
- `join(list)`：将列表中的字符串连接为一个字符串。
- `startswith(prefix)`：检查字符串是否以 `prefix` 开头。
- `endswith(suffix)`：检查字符串是否以 `suffix` 结尾。
- `find(sub)`：查找子字符串 `sub` 在字符串中的位置，如果不存在则返回 `-1`。
- `index(sub)`：查找子字符串 `sub` 在字符串中的位置，如果不存在则抛出异常。
- `isalnum()`：检查字符串是否只包含字母和数字。
- `isalpha()`：检查字符串是否只包含字母。
- `isdigit()`：检查字符串是否只包含数字。
- `islower()`：检查字符串是否只包含小写字母。
- `isupper()`：检查字符串是否只包含大写字母。
- `isspace()`：检查字符串是否只包含空白字符。

## 数字
Python 中的数字包括整数和浮点数。整数是没有小数部分的数字，浮点数是有小数部分的数字。
```python
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3 ** 2)  # 3 的 2 次幂
print(3 ** 0.5)
```
在上面的代码中，使用加减乘除运算符计算两个数字的和、差、积、商和幂。
    
### 数字方法
- `abs(x)`：返回 `x` 的绝对值。
- `round(x, n)`：返回 `x` 四舍五入到 `n` 位小数的值。
- `max(iterable)`：返回可迭代对象中的最大值。
- `min(iterable)`：返回可迭代对象中的最小值。
- `sum(iterable)`：返回可迭代对象中所有元素的和。
- `pow(x, y)`：返回 `x` 的 `y` 次幂。
- `divmod(x, y)`：返回 `x` 除以 `y` 的商和余数。
- `int(x)`：将 `x` 转换为整数。
- `float(x)`：将 `x` 转换为浮点数。
- `complex(x)`：将 `x` 转换为复数。
- `bin(x)`：将 `x` 转换为二进制字符串。
- `oct(x)`：将 `x` 转换为八进制字符串。
- `hex(x)`：将 `x` 转换为十六进制字符串。
- `chr(x)`：返回 Unicode 码位 `x` 对应的字符。
- `ord(x)`：返回字符 `x` 对应的 Unicode 码位。
- `isinstance(x, type)`：检查 `x` 是否是 `type` 类型的实例。
- `type(x)`：返回 `x` 的类型。
- `id(x)`：返回 `x` 的内存地址。
- `hash(x)`：返回 `x` 的哈希值。
- `bool(x)`：将 `x` 转换为布尔值。
- `str(x)`：将 `x` 转换为字符串。
- `list(x)`：将 `x` 转换为列表。
- `tuple(x)`：将 `x` 转换为元组。
- `set(x)`：将 `x` 转换为集合。
- `dict(x)`：将 `x` 转换为字典。
- `len(x)`：返回 `x` 的长度。
- `range(start, stop, step)`：返回从 `start` 到 `stop` 的等差数列。
- `enumerate(iterable)`：返回可迭代对象的索引和值。
- `zip(*iterables)`：将多个可迭代对象打包成元组。
- `sorted(iterable)`：返回可迭代对象的排序副本。
- `reversed(iterable)`：返回可迭代对象的反向迭代器。
- `filter(function, iterable)`：返回可迭代对象中满足条件的元素。
- `map(function, iterable)`：返回可迭代对象中每个元素应用函数后的结果。
- `reduce(function, iterable)`：返回可迭代对象中连续两个元素应用函数后的结果。
- `sum(iterable)`：返回可迭代对象中所有元素的和。
- `any(iterable)`：检查可迭代对象中是否有元素为真。
- `all(iterable)`：检查可迭代对象中所有元素是否为真。
- `abs(x)`：返回 `x` 的绝对值。
- `round(x, n)`：返回 `x` 四舍五入到 `n` 位小数的值。
- `max(iterable)`：返回可迭代对象中的最大值。
- `min(iterable)`：返回可迭代对象中的最小值。
- `sum(iterable)`：返回可迭代对象中所有元素的和。

## 注释
注释是程序中用于解释代码的文本，Python 解释器会忽略注释。单行注释以 `#` 开头，多行注释使用三个单引号或双引号。
```python
# This is a single-line comment.
'''
This is a multi-line comment.
'''
```
在上面的代码中，使用单行注释和多行注释来解释代码。

## 小结
- 变量是程序中用于保存数据的占位符，变量在使用前必须先赋值。
- 字符串是由字符组成的序列，可以使用单引号、双引号或三引号来创建字符串。
- 数字包括整数和浮点数，可以使用加减乘除运算符计算两个数字的和、差、积、商和幂。
- 注释是程序中用于解释代码的文本，Python 解释器会忽略注释。