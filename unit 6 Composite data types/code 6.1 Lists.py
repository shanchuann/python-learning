list1 = []
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd', 'e']
list4 = [1, 'a', 2, 'b', 3, 'c']
list5 = [1, 2, 3, 4, 5, ['a', 'b', 'c', 'd', 'e']]
list6 = [1, 2, 3, 4, 5, ['a', 'b', 'c', 'd', 'e'], 'a', 'b', 'c', 'd', 'e']
list7 = list("123456")
print(list7)

print(type(list1))
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)

# 列表的索引
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])

# 列表的切片
print(list2[0:2])
print(list2[1:3])
print(list2[2:4])
print(list2[3:5])
print(list2[0:5])
print(list2[:3])
print(list2[2:])
print(list2[:])

# 列表的长度
print(len(list2))
print(len(list3))

# 列表的拼接
list8 = list2 + list3
print(list8)
list9 = list3 + list2
print(list9)

# 列表的重复
list10 = list2 * 2
print(list10)

# 列表的成员关系
print(1 in list2)
print(6 in list2)

# 列表的迭代
for i in list2:
    print(i)

# 列表的最大值和最小值
print(max(list2))
print(min(list2))

# 列表的方法
list2.append(6)
print(list2)
list2.insert(0, 0)
print(list2)
list2.remove(6)
print(list2)
list2.pop()
print(list2)
list2.pop(0)
print(list2)
list2.clear()
print(list2)

list2 = [1, 2, 3, 4, 5]
print(list2.count(1))
print(list2.index(1))
list2.reverse()
print(list2)
list2.sort()
print(list2)

# 列表的复制
list11 = list2
print(list11)
list12 = list2.copy()
print(list12)

# 列表的嵌套
list13 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list13)
print(list13[0])
print(list13[1])

print(list13[0][0])
print(list13[0][1])

# 列表的推导式
list14 = [i for i in range(10)]
print(list14)
list15 = [i for i in range(10) if i % 2 == 0]
print(list15)
list16 = [i * j for i in range(1, 10) for j in range(1, 10)]
print(list16)

# 列表的推导式嵌套
list17 = [[i * j for i in range(1, 10)] for j in range(1, 10)]
print(list17)

# 列表的遍历
for i in list17:
    for j in i:
        print("%2d" % j, end=' ')
    print()