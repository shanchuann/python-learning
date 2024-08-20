import time
print(time.time())  # 时间戳
print(time.localtime())  # 结构化时间
t = time.localtime()
print(t.tm_year,type(t.tm_year))
s = time.strftime('%Y-%m-%d %H:%M:%S',t)
print(s)

from my_package import my_tools
print(my_tools.get_time())

