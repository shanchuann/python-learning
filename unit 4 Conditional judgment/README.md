# 条件判断
## 基本语法
在Python中，条件判断的基本语法如下：
```python
if condition:
    # 当condition为True时，执行这段代码
    pass
elif another_condition:
    # 当condition为False且another_condition为True时，执行这段代码
    pass
else:
    # 当上述所有条件都为False时，执行这段代码
    pass
```
    
### if 语句
if语句用来测试一个条件。如果条件为True，则执行相应的代码块；否则，跳过该代码块。例如：
```python
age = 18
if age >= 18:
    print("You are an adult.")
```
在这个例子中，如果变量age的值大于或等于18，则会输出"You are an adult."。

### elif 语句
elif是else if的缩写，用于测试另外一个条件。elif只能在if语句之后使用，可以有多个elif条件。例如：
```
age = 15
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```
在这个例子中，程序会先检查age >= 18是否为True，如果是则输出"You are an adult."，如果不是则检查age >= 13是否为True，如果是则输出"You are a teenager."，否则输出"You are a child."。

### else 语句
else语句在所有条件都不满足时执行相应的代码块。一个if语句块中最多只能有一个else语句，并且它必须放在所有if和elif语句的最后。例如：
```
age = 10
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```
在这个例子中，由于age小于13，所有条件都不满足，所以程序会执行else语句，输出"You are a child."。

## 嵌套条件判断
有时我们需要在一个条件判断中再进行一个条件判断，这种情况称为嵌套条件判断。例如：
```
age = 20
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior.")
    else:
        print("You are not a senior yet.")
else:
    print("You are not an adult.")
```
在这个例子中，如果age大于或等于18，程序会进一步检查是否大于或等于65。如果是，则输出"You are a senior."，否则输出"You are not a senior yet."。如果age小于18，程序直接输出"You are not an adult."。

## 使用布尔操作符
在条件判断中，我们可以使用布尔操作符来组合多个条件。常用的布尔操作符有and、or和not。

### and 操作符
and操作符用于连接两个条件，只有当两个条件都为True时，整个条件才为True。例如：
```
age = 20
has_id = True
 
if age >= 18 and has_id:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")
```
在这个例子中，只有当age大于或等于18且has_id为True时，程序才会输出"You can enter the club."。

### or 操作符
or操作符用于连接两个条件，只要其中一个条件为True，整个条件就为True。例如：
```
age = 20
has_id = False
 
if age >= 18 or has_id:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")
```
在这个例子中，只要age大于或等于18，或者has_id为True，程序就会输出"You can enter the club."。

### not 操作符
not操作符用于取反，即将True变为False，将False变为True。例如：
```
is_raining = False
 
if not is_raining:
    print("You don't need an umbrella.")
else:
    print("You need an umbrella.")
```
在这个例子中，由于is_raining为False，not is_raining为True，所以程序会输出"You don't need an umbrella."。

## 多重条件判断
在实际应用中，我们常常需要检查多个条件。这可以通过多个elif语句来实现。例如：
```
score = 85
 
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```
在这个例子中，程序会依次检查每个条件，直到找到一个满足的条件，然后执行相应的代码块。如果score大于或等于90，输出"Grade: A"；如果大于或等于80但小于90，输出"Grade: B"，以此类推。

## 条件表达式
Python还提供了一种简洁的条件表达式（也称为三元运算符），它允许在一行代码中实现简单的条件判断。其语法如下：

value_if_true if condition else value_if_false
例如：
```
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```
在这个例子中，如果age大于或等于18，status的值为"adult"；否则，status的值为"minor"。

## 实战案例
下面通过几个实际案例来展示如何在编程中使用条件判断。

### 案例一：判断用户输入的数字是奇数还是偶数
```
number = int(input("Enter a number: "))
 
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```
在这个例子中，程序首先读取用户输入的数字，并将其转换为整数。然后通过取模运算number % 2来判断该数字是奇数还是偶数。如果结果为0，说明是偶数，否则是奇数。

### 案例二：根据用户输入的分数判断成绩等级
```
score = int(input("Enter your score: "))
 
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
 
print("Your grade is:", grade)
```
在这个例子中，程序根据用户输入的分数，判断并输出对应的成绩等级。

### 案例三：根据用户输入的年份判断是否为闰年
```
year = int(input("Enter a year: "))
 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
```
在这个例子中，程序根据闰年的判断规则，判断并输出用户输入的年份是否为闰年。

总的来说，条件判断是编程中的基本构建块，它使程序能够根据不同的条件执行不同的代码。掌握if、elif和else语句，以及布尔操作符的使用，对于编写复杂的程序至关重要。
