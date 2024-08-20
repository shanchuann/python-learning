from fileinput import filename


def write_txt():
    data = input('Enter the date: ')
    text = input('Enter your journal: ')
    filename  = 'journal.txt'
    f = open(filename, 'a')
    f.write(data + '\n')
    f.write(text + '\n')
    f.close()
    return True
def read_txt(day = '-1'):
    filename = 'journal.txt'
    with open(filename, 'r') as f:
        if day != '-1':
            for line in f:
                if line.startswith(day):
                    print(line)
                    print(f.readline())
                    break
        else:
            for line in f:
                print(line)
                print(f.readline())
    return True

def menu():
    print('1. Write to journal')
    print('2. Read journal')
    print('3. Exit')

menu()
while True:
    op = input('Enter your choice: ')
    if op == '1':
        if write_txt():
            print('Journal written successfully')

    elif op == '2':
        day = input('Enter the date you want to read(read all please enter -1): ')
        if read_txt(day):
            print('Journal read successfully')
    elif op == '3':
        print('Goodbye!')
        quit()
    else:
        print('Try again')