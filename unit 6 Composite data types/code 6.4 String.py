str1 = "hello"

# 序列的通用操作
print(str1[0])  # h

print(str1.upper())  # HELLO

print(str1 + " world")  # hello world

print(str1 * 3)  # hellohellohello

print("h" in str1)  # True

print("h" not in str1)  # False

print(len(str1))  # 5

print(max(str1))  # o

print(min(str1))  # e

print("abc" < "def")  # True

print("abc" < "abcd")  # True

# 字符串的特有操作

print(str1.find("l"))  # 2

print(str1.find("l", 3))  # 3

print(str1.find("l", 3, 4))  # -1

print(str1.rfind("l"))  # 3

print(str1.index("l"))  # 2

print(str1.index("l", 3))  # 3

# print(str1.index("l", 3, 4))  # ValueError: substring not found

print(str1.rindex("l"))  # 3

print(str1.count("l"))  # 2

print(str1.count("l", 3))  # 1

print(str1.count("l", 3, 4))  # 0

print(str1.replace("l", "L"))  # heLLo

print(str1.replace("l", "L", 1))  # heLlo

print(str1.split("l"))  # ['he', '', 'o']

print(str.isalnum("hello"))  # True

print("#".join(str1))  # h#e#l#l#o
# 字符串的格式化
print("hello %s" % "world")  # hello world

print("hello %d" % 100)  # hello 100

print("hello %f" % 100.0)  # hello 100.000000

print("hello %x" % 100)  # hello 64

print("hello %o" % 100)  # hello 144

print("hello %e" % 100)  # hello 1.000000e+02

print("hello %g" % 100)  # hello 100

# 遍历
for i in str1:
    print(i)

# 切片
print(str1[1:3])  # el

print(str1[1:3:1])  # el

print(str1[1:3:2])  # e

print(str1[1:])  # ello

print(str1[:3])  # hel

print(str1[::2])  # hlo

print(str1[::-1])  # olleh

# 字符串的转换
print(str(100))  # 100

print(repr(100))  # 100

print(chr(65))  # A

print(ord("A"))  # 65

print(hex(100))  # 0x64

print(oct(100))  # 0o144

print(bin(100))  # 0b1100100

print(int("100"))  # 100

print(float("100.0"))  # 100.0

print(str([1, 2, 3]))  # [1, 2, 3]

print(str((1, 2, 3)))  # (1, 2, 3)

print(str({1, 2, 3}))  # {1, 2, 3}

print(str({"a": 1, "b": 2}))  # {'a': 1, 'b': 2}

print(str(True))  # True

print(str(False))  # False

print(str(None))  # None

# 字符串的统计
s = input("请输入一段字符串：")
# 字母个数,数字个数,符号个数,其他字符个数
alpha = 0
digit = 0
space = 0
other = 0
for i in s:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print("字母个数：%d" % alpha)
print("数字个数：%d" % digit)
print("空格个数：%d" % space)
print("其他字符个数：%d" % other)
