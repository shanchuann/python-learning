# 全局变量
num1 = 10
list = [1,2,3]
def f():
    # 局部变量
    global num1  # 声明num1为全局变量,声明不可变类型
    num2 = 20
    print(num2)
    num1 = 30
    print("函数内部：",num1)
    list.append(4)


print(num1)
f()
print("函数运行后：",num1)
# print(num2)  # NameError: name 'num2' is not defined
print(list)