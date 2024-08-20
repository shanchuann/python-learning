import csv,random
from my_package import my_tools
lista = []
def random_info(n = 100):
    subjects = ['Math', 'Science', 'History']
    for i in range(n):
        name = my_tools.random_string(random.randint(3,6))
        subject = random.choice(subjects)
        score = random.randint(50,100)
        lista.append([name, subject, score])

def average():
    with open('data.csv', mode = 'r',encoding = 'utf-8') as f:
        cf = csv.reader(f)
        head = next(cf)
        scores = []
        print(head)
        for row in cf:
            scores.append(int(row[2]))
        return sum(scores)/len(scores)

def make_datas():
    with open('data.csv', mode = 'a',encoding = 'utf-8') as f:
        cf = csv.writer(f)
        random_info()
        cf.writerows(lista)

make_datas()
result = average()
print('The average score is:', result)