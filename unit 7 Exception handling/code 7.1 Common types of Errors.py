# Nameerroe
# prlnt("hello world")
print("hello world")
# NameError: name 'prlnt' is not defined

a = '111'
# print(aa)
print(a)
# NameError: name 'aa' is not defined

# print(b)
# NameError: name 'b' is not defined

# SyntaxError
# if 'he' == 'hi'
#    print('hello')
# SyntaxError: invalid syntax

# IndentationError
# if 'he' == 'hi':
# print('hello')
# IndentationError: expected an indented block

# TypeError
# print(1 + '1')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

tp = (1, 2, 3)
# tp[2] = 4
print(tp)
# TypeError: 'tuple' object does not support item assignment
# tp.append(4)
print(tp)
# AttributeError: 'tuple' object has no attribute 'append'

# ZeroDivisionError
# print(1/0)
# ZeroDivisionError: division by zero

# IndexError
tp = (1, 2, 3)
# print(tp[3])
print(tp[2])
# IndexError: tuple index out of range

# KeyError
d = {1: 'one', 2: 'two'}
# print(d[3])
print(d.get(3))
# KeyError: 3