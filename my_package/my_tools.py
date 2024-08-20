import random, re
a = []
n = 5

def random_char(upper = True):
    if upper:
        t = random.randint(65, 90)
        return chr(t)
    else:
        t = random.randint(97, 122)
        return chr(t)

def random_string(length):
    s = ''
    for j in range(length):
        s += random_char(random.choice([True, False]))
    return s

def Verification_code(length):
    return random_string(length)

def main():
    print(Verification_code(5))

def isphone_number(phone):
    result = re.match(r'^1[3-9]\d{9}$', phone)
    if result:
        return result
    else:
        return "请输入正确的手机号码"

def isemail(email):
    result = re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email)
    if result:
        return result
    else:
        return "请输入正确的邮箱"

def isID_card(ID_card):
    result = re.match(r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dxX]$', ID_card)
    if result:
        return result
    else:
        return "请输入正确的身份证号码"

import time
def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

