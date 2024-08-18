# - 输入年月日,计算这一天是这一年的第几天
# - 输入2024-12-31,输出2024年的第366天

date = input('请输入年月日,格式为YYYY-MM-DD:')
year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])

# 闰年判断
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    leap = 1
else:
    leap = 0

# 月份天数
month_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# 计算天数
days = 0
for i in range(1,month):
    days += month_day[i]
days += day

# 闰年2月加1
if leap == 1 and month > 2:
    days += 1

print('这是这一年的第%d天' % days)