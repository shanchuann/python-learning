# 10级台阶，一次可以走1级或2级，共有多少种走法
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n - 1) + f(n - 2)


print(f(10))
# 89

a = [0,1,2]
for i in range(3, 11):  # 从第3个元素开始，到第10个元素
    a.append(a[i-1] + a[i-2])
print(a[-1])