tuple1 = (1,2,"3",True)
print(tuple1)
print(type(tuple1))
tuple2 = (1,)
print(tuple2)
print(type(tuple2))
tuple3 = (1)
print(tuple3)
print(type(tuple3))
tuple4 = ()
print(tuple4)
print(type(tuple4))
tuple5 = tuple()
print(tuple5)
print(type(tuple5))
tuple6 = tuple([1,2,3])
print(tuple6)
print(type(tuple6))
tuple7 = tuple("Hello")
print(tuple7)
print(type(tuple7))
tuple8 = tuple("Hello",)
print(tuple8)
print(type(tuple8))
list1 = list(tuple1)
print(list1)
str = str(tuple1)
print(str)
print(str[1])

# 序列的通用操作
tuple1 = (1,2,3,4,5)
# 1.索引
print(tuple1[0])
# 2.切片
print(tuple1[1:3])
# 3.相加
tuple2 = (6,7,8,9,10)
print(tuple1 + tuple2)
# 4.相乘
print(tuple1 * 2)
# 5.成员资格
print(3 in tuple1)
# 6.长度
print(len(tuple1))
# 7.最大值
print(max(tuple1))
# 8.最小值
print(min(tuple1))
# 9.转换
list1 = list(tuple1)
print(list1)
tuple3 = tuple(list1)
print(tuple3)
# 10.元素个数
print(tuple1.count(3))
# 11.元素索引
print(tuple1.index(3))
# 12.in
print(3 in tuple1)
print(6 in tuple1)

# 元组的不可变性
tuple1 = (1,2,3,4,5)
# tuple1[0] = 2
# del tuple1[0]
# tuple1.append(6)
# tuple1.insert(0,0)
# del tuple1
# tuple1.clear()
# tuple1.pop()
# tuple1.remove(1)
# tuple1.reverse()
# tuple1.sort()
# tuple1.extend([6,7,8])
# tuple1 += (6,7,8)
# tuple1 *= 2
# tuple1[1:3] = (7,8,9)
# tuple1[1:3] = [7,8,9]
# tuple1[1:3] = (7,8)
# tuple1[1:3] = [7,8]

# 元组的应用
# 1.元组的解包
tuple1 = (1,2,3)
a,b,c = tuple1
print(a,b,c)
a,b,c = 1,2,3
print(a,b,c)
a = 1
b = 2
a,b = b,a
print(a,b)
# 2.元组的交换
a = 1
b = 2
a,b = b,a
print(a,b)
# 3.元组的拆包
tuple1 = (1,2,3,4,5)
a,*b,c = tuple1
print(a,b,c)
a,*b = tuple1
print(a,b)
*a,b = tuple1
print(a,b)

# 遍历
tuple1 = (1,2,3,4,5)
for index,i in enumerate(tuple1):
    print(index,i)
for i in range(len(tuple1)):
    print(i,tuple1[i])