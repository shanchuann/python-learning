import csv, random
from my_package import my_tools
lista = []
def random_info(n = 100):
    subjects = ['python', 'java', 'c++', 'c#', 'javascript']
    for i in range(n):
        name = my_tools.random_string(random.randint(3, 6))
        subject = random.choice(subjects)
        score = random.randint(50, 100)
        lista.append([name, subject, score])
def average():
    with open('data.csv', mode = 'r', encoding = 'utf-8') as f:
        cf = csv.reader(f)
        head = next(cf)  # 获取表头
        score = []
        for i in cf:
            score.append(int(i[2]))
    return sum(score)/len(score)
def make_datas():
    with open('data.csv', mode = 'a', encoding = 'utf-8',newline = "") as f:
        cf = csv.writer(f)
        random_info()
        cf.writerows(lista)

make_datas()
print('average is',round(average(), 2))
