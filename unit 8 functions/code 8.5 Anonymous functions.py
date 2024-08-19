a = lambda x, y: x + y
print(a(5, 6))  # Output: 11

a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(i ** 2)
print(b)  # Output: [1, 4, 9, 16, 25]

a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    a[i] = a[i] ** 2
print(a)  # Output: [1, 4, 9, 16, 25]

a = [1, 2, 3, 4, 5]
def f(x):
    return x**2
result = map(f,a)  # map() 映射
print(list(result))  # Output: [1, 4, 9, 16, 25]

a = [1, 2, 3, 4, 5]
result = map(lambda x: x**2, a)
print(list(result))  # Output: [1, 4, 9, 16, 25]


a = [1, 2, 3, 4, 5]
# reduce() 累加,累积
from functools import reduce
result = reduce(lambda x, y: x + y, a)
print(result)  # Output: 15

a = [1, 2, 3, 4, 5]
# filter() 过滤
result = filter(lambda x: x % 2 == 0, a)
print(list(result))  # Output: [2, 4]

a = [1,2,3,40,5,6,0,6,0,5]  # 12340560605
result = 0
mul = 1
for i in a[::-1]:
    result = result + i*mul
    mul = mul * 10**len(str(i))
print(result)  # Output: 12340560605

a = [1,2,3,40,5,6,0,6,0,5]  # 12340560605
result = reduce(lambda x, y: x*10**len(str(y)) + y, a)