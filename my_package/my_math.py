author = 'shanchuan'

def add(a, b):
    return a + b

def total(*args):
    '''
    参数a是一个列表，返回列表中所有元素的平方和
    '''
    result = 0
    for i in args:
        result += i**2
    return result