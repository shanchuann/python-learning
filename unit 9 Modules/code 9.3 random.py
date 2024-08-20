import random
# 随机小数
print(random.random())
# 随机整数
print(random.randint(1, 10))

list1 = [1, 2, 3, 4, 5]
# 随机选择一个元素
print(list1[random.randint(0, len(list1) - 1)])
print(random.choice(list1))

# 生成随机字母组成的列表
a = []
n = 5
for i in range(20):
    s = ''
    for j in range(n):
        t = random.randint(65, 90)
        s += chr(t)
    a.append(s)
print(a)

from my_package import my_tools, my_games
print(my_tools.random_string(5))

# 随机打乱列表
random.shuffle(list1)
print(list1)

my_games.gess_number()


