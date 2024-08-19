while True:
    try:
        op = input('请输入四则运算表达式(e.g:1+2): ')
        if '+' in op:
            a = op.split('+')
            result = int(a[0]) + int(a[1])
            print('结果是: ', result)
        elif '-' in op:
            a = op.split('-')
            result = int(a[0]) - int(a[1])
            print('结果是: ', result)
        elif '*' in op:
            a = op.split('*')
            result = int(a[0]) * int(a[1])
            print('结果是: ', result)
        elif '/' in op:
            a = op.split('/')
            result = int(a[0]) / int(a[1])
            print('结果是: ', result)
        elif op =='C':
            print('感谢使用')
            break
        else:
            raise Exception('请输入正确的四则运算表达式')
    except ZeroDivisionError:
        print('错误: 除数不能为0')
    except Exception as e:
        print('错误:', e)