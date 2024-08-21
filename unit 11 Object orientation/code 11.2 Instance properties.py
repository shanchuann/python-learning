class Player(object):
    pass

shanchuan = Player()
# 实例的属性
shanchuan.name = 'shanchuan'
shanchuan.age = 19
shanchuan.city = 'xi\'an'
print(shanchuan.name, shanchuan.age, shanchuan.city)

class Player(object):
    def __init__(self,name,age,city):  # 初始化函数
        self.name = name
        self.age = age
        self.city = city

shanchuan = Player('shanchuan',19,'xi\'an')
print(shanchuan.name, shanchuan.age, shanchuan.city)
shanchuan.city = 'beijing'
print(shanchuan.name, shanchuan.age, shanchuan.city)
tom = Player('tom',20,'beijing')
print(tom.name, tom.age, tom.city)
tom.height = 180
print(tom.__dict__)  # 查看实例的属性