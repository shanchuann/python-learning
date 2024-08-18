for i in range(5):
    print(i)

# Output: 0 1 2 3 4
# range(5)生成一个从0到4的整数序列，for循环依次将序列中的元素赋值给i，然后执行循环体

# 高斯求和
sum = 0
for i in range(101):
    sum += i
print(sum)

# 1! + 2! + 3! + ... + n!
n = 3
result2 = 0
result = 1
for i in range(1,n+1):  # 1到n
    result *= i
    print(result)
    result2 += result
print(result2)

