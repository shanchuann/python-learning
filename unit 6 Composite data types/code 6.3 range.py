# range(start,stop,step)
print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(10,0,-1)))
print(list(range(10,1,-2)))

# 遍历
for i in range(5):
    print(i)
for i in range(1,5):
    print(i)
for i in range(1,5,2):
    print(i)
for i in range(5,1,-1):
    print(i)

# 生成列表
print([i for i in range(5)])

# 生成元组
print(tuple(i for i in range(5)))

# 生成集合
print({i for i in range(5)})
print({i:i for i in range(5)})
print({i:i for i in range(5) if i%2 == 0})

# 生成字典
print({i:i for i in range(5)})
print({i:i for i in range(5) if i%2 == 0})

# 水仙花数(三位数),每个位数的立方和等于这个数本身
for i in range(100,1000):
    if i == (i//100)**3 + (i//10%10)**3 + (i%10)**3:
        print(i)