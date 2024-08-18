# print 2024
print(2024)
# print : I am admin
print("I am admin")
#creat a variable named "Year" and assign it the value 2024
Year = 2024
print(Year)
# print 2024year,I will be 19 years old
print(2024, "year,I will be 19 years old")  # 逗号分隔符打印时转化为空格

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(2024, "year,I will be 19 years old", sep="")  # sep参数指定分隔符
print(end="*")  # end参数指定结束符
print(2024, "year,I will be 19 years old", sep="", end="\n")
# print :今天是 2024 年 1 月 1 日，星期 一，天气 晴，温度 20.4 度
year = 2024
month = 1
day = 1
week = "一"
weather = "晴"
temperature = 20.4
print("今天是 ", year, " 年 ", month, " 月 0", day, " 日，星期 ", week, "，天气 ", weather, "，温度 ", temperature, " 度", sep="")
# 格式化输出
print("今天是 %d 年 %d 月 %02d 日，星期 %s，天气 %s，温度 %.1f 度" % (year, month, day, week, weather, temperature))