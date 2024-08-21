class Player(object):
    numbers = 0  # 类属性
    all_age = []  # 类属性

    def __init__(self,name,age,city):  # 初始化函数
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1  # 类属性自增1
        Player.all_age.append(age)  # 将年龄添加到类属性中

    def show(self):  # 实例方法
        print('name:',self.name)
        print('age:',self.age)
        print('city:',self.city)
        print('numbers:',Player.numbers)

    @classmethod
    def get_player_numbers(cls):  # 类方法
        print('numbers is:',cls.numbers)

    @classmethod
    def get_max_age(cls):
        max_damage = 0
        for i in cls.all_age:
            if i > max_damage:
                max_damage = i
        return max_damage

    @staticmethod
    def isvalid(**kwargs):
        if kwargs['age'] < 18:
            return False
        return True

class FootballPlayer(Player):  # 继承Player类
    def __init__(self,name,age,city,team):  # 初始化函数
        super(FootballPlayer,self).__init__(name,age,city)  # 调用父类的初始化函数
        self.team = team  # 实例属性

    def show(self):  # 重写父类的show方法
        print('name:',self.name)
        print('age:',self.age)
        print('city:',self.city)
        print('team:',self.team)
        print('numbers:',Player.numbers)

    def get_team(self):  # 实例方法
        print('team:',self.team)

    @staticmethod
    def isvalid(**kwargs):
        if kwargs['age'] < 18:
            return False
        return True

Tom = FootballPlayer('Tom',20,'Shanghai','Shanghai Shenhua')  # 创建FootballPlayer类的实例

Tom.show()  # 调用show方法
Tom.get_team()  # 调用get_team方法
Tom.get_player_numbers()  # 调用get_player_numbers方法
print('max age:',Tom.get_max_age())  # 调用get_max_age方法
print('isvalid:',Tom.isvalid(age=20))  # 调用isvalid方法
Jerry = FootballPlayer('Jerry',18,'Beijing','Beijing Guoan')  # 创建FootballPlayer类的实例
Jerry.show()  # 调用show方法
Jerry.get_team()  # 调用get_team方法
Jerry.get_player_numbers()  # 调用get_player_numbers方法
print('max age:',Jerry.get_max_age())  # 调用get_max_age方法
