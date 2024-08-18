while True:
    print(111)
    break
    print(222)
print("end")

for i in range(1,10):
    if i%3 == 0:
        print(i)
        break
print("end")

# 判断一个数是否为质数
num = 17
for i in range(2,num):
    if num%i == 0:
        print("不是质数")
        break
else:
    print("是质数")
print("end")
