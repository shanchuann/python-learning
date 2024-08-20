import random

def stone_paper_scissors():  # 石头剪刀布
    for i in range(3):
        player = input(" please input stone-paper-scissors: ")
        computer = random.choice(['stone', 'scissors', 'paper'])
        print('player：', player)
        print('computer：', computer)
        if player == computer:
            print('Draw')
        elif player == 'stone' and computer == 'scissors' or player == 'scissors' and computer == 'paper' or player == 'paper' and computer == 'stone':
            print('you win')
        else:
            print('you lose')

def gess_number():  # 猜数字
    answer = random.randint(1, 100)
    while True:
        number = int(input('please input a number: '))
        if number < answer:
            print('Guess too small')
        elif number > answer:
            print('Guess too big')
        else:
            print('bingo')
            break

