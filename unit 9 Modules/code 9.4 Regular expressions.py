# ids = input("Enter your ID: ")
# 位数18位，前17位为数字，最后一位为数字或字母
# if len(ids) == 18 and ids[:17].isdigit() and ids[-1].isalnum():
#     print("Valid ID")
# else:
#     print("Invalid ID")
# import re
# if re.match(r"\d{17}[\dXx]", ids):
#     print("Valid ID")
# else:
#     print("Invalid ID")
import re
# 检测是否为纯数字
# if re.match(r"\d{17}$", ids):
#     print("Valid ID")
# else:
#     print("Invalid ID")

# . 匹配任意字符
result = re.match(r'.+', 'hello123')
print(result)

# [] 匹配中括号中的任意一个字符
result = re.match(r'[abc]', 'a')
print(result)

# [a-z] 匹配a-z中的任意一个字符
result = re.match(r'[a-z]', 'a')
print(result)

# [^] 匹配除中括号中的字符之外的任意一个字符
result = re.match(r'[^abc]', 'd')
print(result)

# ^ 匹配字符串的开头
result = re.match(r'^hello', 'hello123')
print(result)

# $ 匹配字符串的结尾
result = re.match(r'hello$', 'hello123')
print(result)

# * 匹配前一个字符0次或多次
result = re.match(r'\d*', '123')
print(result)

# + 匹配前一个字符1次或多次
result = re.match(r'\d+', '123')
print(result)

# ? 匹配前一个字符0次或1次
result = re.match(r'\d?', '123')
print(result)

# {n} 匹配前一个字符n次
result = re.match(r'\d{3}', '123')
print(result)

# {n,} 匹配前一个字符至少n次
result = re.match(r'\d{2,}', '123')
print(result)

# {n,m} 匹配前一个字符n到m次
result = re.match(r'\d{1,3}', '123')
print(result)

# | 匹配|左右任意一个表达式
result = re.match(r'hello|world', 'world')
print(result)

# () 分组匹配
result = re.match(r'(hello)(world)', 'helloworld')
print(result)

# \ 转义字符
result = re.match(r'\d\.', '1.')
print(result)

# \b 匹配单词的边界
result = re.match(r'\bhello\b', 'hello world')
print(result)

# \B 匹配非单词的边界
result = re.match(r'\Bhello\B', 'hello world')
print(result)

# \d 匹配数字
result = re.match(r'\d', '123')
print(result)

# \D 匹配非数字
result = re.match(r'\D', 'hello')
print(result)

# \s 匹配空白字符
result = re.match(r'\s', ' hello')
print(result)

# \S 匹配非空白字符
result = re.match(r'\S', 'hello')
print(result)

# \w 匹配字母、数字、下划线
result = re.match(r'\w', 'hello123')
print(result)

# \W 匹配非字母、数字、下划线
result = re.match(r'\W', 'hello123')
print(result)

# \A 匹配字符串的开头
result = re.match(r'\Ahello', 'hello world')
print(result)

# \Z 匹配字符串的结尾
result = re.match(r'world\Z', 'hello world')
print(result)

# \n 匹配换行符
result = re.match(r'.+\n', 'hello\nworld')
print(result)

# \t 匹配制表符
result = re.match(r'.+\t', 'hello\tworld')
print(result)

# \r 匹配回车符
result = re.match(r'.+\r', 'hello\rworld')
print(result)

# \f 匹配换页符
result = re.match(r'.+\f', 'hello\fworld')
print(result)

# \v 匹配垂直制表符
result = re.match(r'.+\v', 'hello\vworld')
print(result)

# \1 匹配第一个分组的内容
result = re.match(r'(\d)\1', '11')
print(result)

...

# re.I 忽略大小写
result = re.match(r'hello', 'Hello', re.I)
print(result)

# re.S 匹配任意字符
result = re.match(r'.+', 'hello\nworld', re.S)
print(result)

# re.M 匹配每一行
result = re.match(r'.+', 'hello\nworld', re.M)
print(result)

# re.X 忽略空白字符
result = re.match(r'hello world', 'hello world', re.X)
print(result)

# re.A 匹配字符串的开头
result = re.match(r'hello', 'hello world', re.A)
print(result)
...

from my_package import my_tools
print(my_tools.isphone_number('12345678901'))
print(my_tools.isphone_number('13000000000'))

print(my_tools.isemail('1111111111@qq.com'))
print(my_tools.isID_card('111111111111111111'))