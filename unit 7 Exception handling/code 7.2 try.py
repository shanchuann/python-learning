try:
    print("May be an error")
except:
    print("An error occurred")
else:
    print("No error occurred")
finally:
    print("Finally block")
print('*'*20)
try:
    print("May be an error")
    n = int(input("please enter a number: "))
    n = 5/n
    print(n)
except ZeroDivisionError as e:
    print("Division by zero")
    print(e)
except:
    print("Please enter a number")
else:
    print("No error occurred")
finally:
    print("Finally block")
    # 数据清除, 关闭文件, 关闭数据库连接






