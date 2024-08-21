# 封装
class User(object):
    def __init__(self,name,age):
        self._name = name  # 受保护的属性
        self.__age = age  # 私有属性

    @property  # 获取一个变量
    def age(self):
        return self.__age
    @age.setter  # 修改一个变量
    def age(self,age):
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age

    def show_infos(self):
        print('name:',self._name)
        print('age:',self.__age)

shanchuan = User('shanchuan',19)
# print(shanchuan._name)
# # print(shanchuan.__age)  受保护
# print(shanchuan._User__age)  # 私有属性
#
# shanchuan.show_infos()

# shage = shanchuan.get_age()
# print(shage)
# shanchuan.set_age(20)
# shanchuan.show_infos()
# shanchuan.set_age(-1)

print(shanchuan.age)
shanchuan.age = 20
print(shanchuan.age)



