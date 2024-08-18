# if-elif-else语句
if 1 < 0:
    print("1小于0")
elif 1 == 0:
    print("1等于0")
else:
    print("1大于0")
# if-else if
sorce = 90
if sorce >= 90:
    print("优秀")
else:
    if sorce >= 80:
        print("良好")
    else:
        if sorce >= 60:
            print("及格")
        else:
            print("不及格")

# BMI指数
height = 1.75
weight = 70
bmi = weight / height ** 2
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")

# 日期判断
num = int(input("请输入一个数字："))
if num == 1:
    print("星期一")
if num == 2:
    print("星期二")
if num == 3:
    print("星期三")
if num == 4:
    print("星期四")
if num == 5:
    print("星期五")
if num == 6:
    print("星期六")
if num == 7:
    print("星期日")
if num < 1 or num > 7:
    print("输入错误")

# 三元表达式
x = 1
y = 2
z = x if x > y else y
print(z)