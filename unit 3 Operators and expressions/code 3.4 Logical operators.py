# and 与
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print("hello" and "hi")  # hi 短路运算
print("hello" and "")  # ""
print("" and "hi")  # ""
# or 或
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print(1 or 0)  # 1
print(0 or 1)  # 1
print(0 or 0)  # 0
print(1 or 1)  # 1
# not 非
print(not True)  # False
print(not False)  # True
# 优先级 not > and > or
print(True and False or True)  # True
print(True and (False or True))  # True
print((True and False) or True)  # True
print(not True and False)  # False
print(not (True and False))  # True
print(not True and not False)  # False
print(not (True and not False))  # False
print(not True and not False)  # False
print(not (True and not False))  # False


