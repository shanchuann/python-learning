# 运算符
| 运算符 | 描述 | 例子 |
| --- | --- | --- |
| 算术运算符 | +, -, *, /, %, //, ** | `a + b`, `a - b`, `a * b`, `a / b`, `a % b`, `a // b`, `a ** b` |
| 比较运算符 | ==, !=, >, <, >=, <= | `a == b`, `a != b`, `a > b`, `a < b`, `a >= b`, `a <= b` |
| 逻辑运算符 | and, or, not | `a and b`, `a or b`, `not a` |
| 位运算符 | &, \|, ^, ~, <<, >> | `a & b`, `a \| b`, `a ^ b`, `~a`, `a << b`, `a >> b` |
| 赋值运算符 | =, +=, -=, *=, /=, %=, //=, **=, &=, \|=, ^=, <<=, >>= | `a = b`, `a += b`, `a -= b`, `a *= b`, `a /= b`, `a %= b`, `a //= b`, `a **= b`, `a &= b`, `a \|= b`, `a ^= b`, `a <<= b`, `a >>= b` |
| 成员运算符 | in, not in | `a in b`, `a not in b` |
| 身份运算符 | is, is not | `a is b`, `a is not b` |

# 表达式
表达式是由变量、常量和运算符组成的。Python 表达式可以包含多个运算符。Python 解释器会根据运算符的优先级和结合性来计算表达式的值。

```python
a = 10
b = 20
c = 30
d = 40
    
# 算术运算符
print(a + b) # 30
print(a - b) # -10
print(a * b) # 200
print(a / b) # 0.5
print(a % b) # 10
print(a // b) # 0
print(a ** b) # 100000000000000000000

# 比较运算符
print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True
    
# 逻辑运算符
print(a and b) # 20
print(a or b) # 10
print(not a) # False

# 位运算符
print(a & b) # 0
print(a | b) # 30
print(a ^ b) # 30
print(~a) # -11
print(a << b) # 10485760
print(a >> b) # 0

# 赋值运算符
a += b
print(a) # 30
a -= b
print(a) # 10
a *= b
print(a) # 200
a /= b
print(a) # 10.0
a %= b
print(a) # 10.0
a //= b
print(a) # 0.0
a **= b
print(a) # 0.0
a &= b
print(a) # 0
a |= b
print(a) # 20
a ^= b
print(a) # 0
a <<= b
print(a) # 0
a >>= b
print(a) # 0

# 成员运算符
print(a in [10, 20, 30]) # True
print(a not in [10, 20, 30]) # False

# 身份运算符
print(a is b) # False
print(a is not b) # True
```

# 运算符优先级
| 运算符 | 描述 |
| --- | --- |
| ** | 指数 (最高优先级) |
| ~ | 按位翻转 |
| +, - | 正号，负号 |
| *, /, %, // | 乘，除，取模和取整除 |
| +, - | 加法，减法 |
| <<, >> | 移位运算符 |
| & | 位与 |
| ^, \| | 位运算符 |
| <=, <, >, >= | 比较运算符 |
| ==, != | 等于运算符 |
| =, +=, -=, *=, /=, %=, //=, **=, &=, \|=, ^=, <<=, >>= | 赋值运算符 |
| is, is not | 身份运算符 |
| in, not in | 成员运算符 |
| not, or, and | 逻辑运算符 (最低优先级) |
```

# 阅读
- [Python 运算符](https://www.runoob.com/python/python-operators.html)
- [Python 表达式](https://www.runoob.com/python/python-expressions.html)
- [Python 运算符优先级](https://www.runoob.com/python/python-operators.html)