# 年龄判断
age_str = input("请输入一个人的年龄：")
if age_str.isdigit():
    age = int(age_str)
    if age >= 1 and age <= 120:
        print("年龄在1-120之间")
    else:
        print("年龄不在1-120之间")
else:
    print("输入有误")
