# 按位与 & 两个都为1则1
print(5 & 7) # 5
'''
101
111
---
101
'''
# 按位或 | 有1则1
print(5 | 7) # 7
'''
101
111
---
111
'''
# 按位异或 ^ 相同为0，不同为1
print(5 ^ 7) # 2
'''
101
111
---
010
'''
# 按位取反 ~ 0变1，1变0，取反后的结果是对应的负数减1，即~x=-(x+1)
print(~5) # -6
'''
00000000000000000000000000000101
-----------------------------------
11111111111111111111111111111010 取反
10000000000000000000000000000101 加一
10000000000000000000000000000110 结果 -6
'''
# 左移 << 低位补0，高位丢弃，相当于乘2
print(5 << 1) # 10
'''
101
1010
'''
# 右移 >> 高位补0，低位丢弃，相当于除2
print(5 >> 1) # 2
'''
101
10
'''
