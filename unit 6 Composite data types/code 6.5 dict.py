# 字典创建
dict = {'Name': 'Zara',
        'Age': 7,
        'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
# 修改字典
dict['Age'] = 8
dict['School'] = "DPS School"
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
# 删除字典元素
del dict['Name']
dict.clear()
del dict
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])
# print("dict['Class']: ", dict['Class'])

# 字典键的特性
dict = {'Name': 'Zara', 'Age': 7}
print("Age: %s" % dict.get('Age'))

print('Age' in dict)

# 遍历
dict = {'Name': 'Zara', 'Age': 7}
for key in dict:
    print(key, dict[key])
print("-"*20)
for key, value in dict.items():
    print(key, value)

# 字典的常用方法
dict = {'Name': 'Zara', 'Age': 7}
print("Value : %s" % dict.items())
print("Value : %s" % dict.keys())
print("Value : %s" % dict.values())
print("Value : %s" % dict.pop('Age'))
print("Value : %s" % dict)
dict = {'Name': 'Zara', 'Age': 7}
dict2 = dict.copy()
print("Value : %s" % dict2)
dict2 = dict.fromkeys(dict)
print("Value : %s" % dict2)
dict.clear()
print("Value : %s" % dict)
print("Value : %s" % dict2)
dict.update({'Age': 7})
print("Value : %s" % dict)
dict.update({'Age': 8})
print("Value : %s" % dict)
