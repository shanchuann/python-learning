# 单引号字符串
str1 = 'I told'
# 空串
str2 = ''
str3 = str()
# 双引号字符串
str4 = "I am admin"
# 三引号字符串
str5 = '''
I 
am
admin'''

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

# 字符串运算
# 字符串连接
str6 = "Hello," + "Python!"
print(str6)
# 字符串重复
str7 = "Hello, Python!" * 3
print(str6)
# 字符串索引
str8 = "Hello, Python!"
print(str8[0],end=" ")
print(str8[1],end=" ")
print(str8[2],end=" ")
print(str8[3],end=" ")
print(str8[4],end=" ")
print(str8[5],end=" ")
print(str8[6],end=" ")
print(str8[7],end=" ")
print(str8[8],end=" ")
print(str8[9],end=" ")
print(str8[10],end=" ")
print(str8[11],end=" ")
print(str8[12],end=" ")
print(str8[13])
print(str8[-1])  # 字符串倒数第一个字符
# 字符串切片 变量名[起始位置:结束位置:步长]，起始位置包含，结束位置不包含，步长默认为1
str9 = "Hello, Python!"
print(str9[0:5])
print(str9[7:13])
print(str9[:5])
print(str9[7:])
str13 = "123456789"
print(str13[::2])
# 字符串反转
print(str13[::-1])
print(str13[-1:-10:-1])
# 字符串长度
str10 = "Hello, Python!"
print(len(str10))
# 字符串格式化
str11 = "Hello, %s" % "Python!"
print(str11)
str12 = "Hello, %s, I am %d years old" % ("Python", 19)
print(str12)
# 字符串转义
str14 = "Hello, \"Python!\""
print(str14)
str15 = "Hello, \'Python!\'"
print(str15)
str16 = "Hello, \\Python!"
print(str16)
str17 = "Hello, \nPython!"
print(str17)
str18 = "Hello, \tPython!"
print(str18)

# 字符串方法
# 字符串查找
str19 = "Hello, Python!"
print(str19.find("Python"))
print(str19.find("Java"))
# 字符串替换
str20 = "Hello, Python!"
print(str20.replace("Python", "Java"))
# 字符串分割
str21 = "Hello, Python!"
print(str21.split(","))
# 字符串大小写转换
str22 = "Hello, Python!"
print(str22.upper())
print(str22.lower())
# 字符串去空格
str23 = " Hello, Python! "
print(str23.strip())
# 字符串格式化
print("Hello, {0}".format("Python!"))
str25 = "Hello, {0}, I am {1} years old".format("Python", 19)
print(str25)