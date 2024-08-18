# 转换为整数 str --> int
s = "2024"
print(s)
n = int(s)
print(n)
print(type(s),type(n))
s1,s2 = True,False
print(int(s1),int(s2))
f = 3.14
print(int(f))
# 转换为浮点数
print(float(s))
n = 2024
print(float(n))
print(float(s1),float(s2))
# 转换为字符串
print(str(n))
print(str(f))
print(str(s1),str(s2))
# 转换为复数
print(complex(n))
print(complex(f))
print(complex(s1),complex(s2))
# 转换为元组
print(tuple(s))
print(tuple(str(n)))
print(tuple(str(f)))
print(tuple(str(s1)))
print(tuple(str(s2)))
# 转换为列表
print(list(s))
print(list(str(n)))
print(list(str(f)))
print(list(str(s1)))
print(list(str(s2)))
# 转换为集合
print(set(s))
print(set(str(n)))
print(set(str(f)))
print(set(str(s1)))
print(set(str(s2)))
# 转换为布尔值
print(bool(str))
print(bool(n))
print(bool(f))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(" "))
print(bool("False"))
print(bool("True"))
print(bool("0"))
print(bool("1"))
print(bool("3.14"))
# 进制转换
s = "10"
print(int(s,2))
print(int(s,8))
print(int(s,16))