class Player(object):
    numbers = 0  # 类属性
    def __init__(self,name,age,city):  # 初始化函数
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1  # 类属性自增1

    def show(self):  # 实例方法
        print('name:',self.name)
        print('age:',self.age)
        print('city:',self.city)
        print('numbers:',Player.numbers)

Tom = Player('Tom', 20, 'Shanghai')
Tom.show()
Jerry = Player('Jerry', 22, 'Beijing')
Jerry.show()