class Player(object):
    numbers = 0  # 类属性
    def __init__(self,name,age,city):  # 初始化函数
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1  # 类属性自增1

Tom = Player('Tom', 20, 'Shanghai')
print(Tom.__dict__)    # {'name': 'Tom', 'age': 20, 'city': 'Shanghai'}
print(Player.numbers)  # 1
Jerry = Player('Jerry', 22, 'Beijing')
print(Jerry.__dict__)  # {'name': 'Jerry', 'age': 22, 'city': 'Beijing'}
print(Player.numbers)  # 2

