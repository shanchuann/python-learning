# 集合的创建
s = set()
print(s)
s = {1, 2, 3,2, 3, 4}
print(s)
s = set([1, 2, 3, 2, 3, 4])
print(s)
s = set((1, 2, 3, 2, 3, 4))
print(s)
s = set('hello')
print(s)
s = set({'a': 1, 'b': 2, 'c': 3})
print(s)
s = set({'a', 'b', 'c'})
print(s)
s = set(range(10))
print(s)
# in
print(1 in s)
# not in
print(1 not in s)
# len
print(len(s))
# add
s.add(10)
print(s)
# remove
s.remove(0)
print(s)
# pop
print(s.pop())
print(s)
# clear
s.clear()
print(s)
# copy
s = {1, 2, 3, 4}
t = s.copy()
print(t)
# update
s.update({4, 5, 6})
print(s)
#  | 交集
print(s | t)
# & 并集
print(s & t)
# - 差集
print(s - t)
# ^ 对称差集
print(s ^ t)
# <= 子集
print(s <= t)
# >= 超集
print(s >= t)
# < 真子集
print(s < t)
# > 真超集
print(s > t)
# == 相等
print(s == t)
# != 不等
print(s != t)
# is 子集
print(s is t)
# is not 超集
print(s is not t)
# 集合推导式
s = {x for x in range(10)}
print(s)
s = {x for x in range(10) if x % 2 == 0}
print(s)
s = {x: x**2 for x in range(10)}
print(s)
s = {x: x**2 for x in range(10) if x % 2 == 0}
print(s)
# 列表去重
l = [1, 2, 3, 2, 3, 4]
print(list(set(l)))
# 字符串去重
s = 'hello'
print(''.join(set(s)))
# 字典去重
d = {'a': 1, 'b': 2, 'c': 1}
print({v: k for k, v in d.items()})
# 集合去重
s = {1, 2, 3, 2, 3, 4}
print(set(s))
