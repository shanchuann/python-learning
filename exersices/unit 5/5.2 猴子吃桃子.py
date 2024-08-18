# 猴子吃桃子
# 穷举(天数为3)
peach = 1
while True:
    d1 = peach//2 - 1
    d2 = d1//2 - 1
    d3 = d2//2 - 1
    if d3 == 1:
        print(peach)
        break
    peach += 1

# 倒推(天数为10)
peach = 1
for i in range(9):
    peach = (peach + 1) * 2
print(peach)

