try:
    pwd = input('Enter password: ')
    if len(pwd) < 6:
        raise Exception('Password is too short')
except Exception as e:
    print(e)