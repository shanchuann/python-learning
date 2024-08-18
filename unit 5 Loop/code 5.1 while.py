# 初始条件
n = 0
while n <= 5:
    print(n)
    # 更新条件
    n = n + 1

print('循环结束')

# 高斯求和
sum = 0
counter = 1
while counter <= 100:
    sum += counter
    counter += 1
print('1 到 %d 之和为: %d' % (counter - 1, sum))

# 死循环
# var = 1
# while var == 1:
#     num = int(input('输入一个数字: '))
#     print('你输入的数字是: ', num)
# print('Good bye!')

# 1! + 2! + 3! + ... + n!
n = 3
result2 = 0
result = 1
i = 1
while i <= n:
    result *= i
    print(result)
    result2 += result
    i += 1
print(result2)

# 与else连用
count = 0
while count < 5:
    print(count, '小于5')
    count += 1
else:
    print(count, '大于或等于5')
