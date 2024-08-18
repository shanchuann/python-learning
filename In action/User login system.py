# 用户名,密码,黑名单
users = {
    'admin':{'username': 'admin', 'password': '111','status': True},
    'root':{'username': 'root', 'password': '222','status': True},
    'test':{'username': 'test', 'password': '333','status': False},
}

for i in range(3):
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    if user in users and pwd == users[user]['password'] and users[user]['status']:
        print('登录成功')
        flag = True
        break
    elif user in users and pwd == users[user]['password'] and not users[user]['status']:
        print('用户已被锁定')
    elif user in users and pwd != users[user]['password']:
        print('密码错误')
    else:
        print('用户不存在')
else:
    print('尝试次数过多')