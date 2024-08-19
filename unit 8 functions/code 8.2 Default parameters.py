# 位置参数
def power(x, n):
    return x ** n


print(power(2, 3))

# 缺省参数
def power(x, n=2):
    return x ** n


print(power(2))
print(power(2, 3))


# 缺省参数的位置
def power(x=2, n=2):
    return x ** n


print(power())
print(power(3))
print(power(3, 3))

def info(name, age = 18,gender="男"):
    print("姓名：%s" % name)
    print("年龄：%d" % age)
    print("性别：%s" % gender)


info("小明")
info("小红", 20)
info("小刚", 22, "女")
info("小李",gender="女")

