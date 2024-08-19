# say_hello()
# NameError: name 'say_hello' is not defined
from unittest import removeResult


def say_hello():
    print('Hello, World!')
    print('Hello, Python!')


say_hello()
say_hello()

def sum_2_num(a, b):  # 形式参数
    result = a + b
    return result


sum_2_num(1, 2)  # 实际参数
result = sum_2_num(3, 4)
print(result)