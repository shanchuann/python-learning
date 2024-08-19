# 可变参数
def total(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


print(total(1, 2, 3))

def f(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


d = {"name": "张三", "age": 18}
f(**d)

