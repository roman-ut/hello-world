desk = [['-']*3 for i in range(3)] # создание начального игрового стола

def print_desk(): # функция вывода игрового стола на экран
    print('-------------')
    print("Игровой стол:")
    print('-------------')
    print('   ', '0','1','2')
    for i in range(3):
        print(f" {str(i)}  {' '.join(desk[i])}")
    print('-------------')

def inter_menu(n): # функция, реализующая интерактивное меню ввода значений и их контроль
    while True:
        while True:
            x = input('Номер строки = ')
            if not x.isdigit():
                print('Введите целое число!')
                continue
            x = int(x)
            if 0 <= x <= 2:
                break
            else:
                print('Введённое значение не существует. Размер игрового стола 3 на 3. '
                      'Введите значение от 0-ля до 2-х.')
        while True:
            y = input('Номер столбца = ')
            if not y.isdigit():
                print('Введите целое число!')
                continue
            y = int(y)
            if 0 <= y <= 2:
                break
            else:
                print('Введённое значение не существует. Размер игрового стола 3 на 3. '
                      'Введите значение от 0-ля до 2-х.')
        if desk[x][y] != '-':
            print('Введённая позиция занята. Введите другие значения.')
        else:
            desk[x][y] = n
            break
    return desk[x][y]

def proverka(n): # функциия проверки победителя
    if (desk[0][0] == n and desk[1][1] == n and desk[2][2] == n) or \
            (desk[0][2] == n and desk[1][1] == n and desk[2][0] == n):
        return True
    else:
        for i in range(0,3):
            k = []
            for y in range(0,3):
                k.append(desk[y][i])
            if k == [n,n,n]:
                return True
            if desk[i] == [n,n,n]:
                return True
    return False

# основной код программы, реализующий игру в крестики нолики
print('Добро пожаловать в игру "Крестики-нолики"!')
count = 0 # счетчик хода
while True:    
    print_desk()
    if count == 9:
        print('Ничья!')
        break
    print('Укажите в какую позицию ввести "Х":')
    inter_menu('x')
    if proverka('x'):
        print_desk()
        print('Ура! Победил "X" - игрок')
        break
    count += 1
    print_desk()
    if count == 9:
        print('Ничья!')
        break
    print('Укажите в какую позицию ввести "0":')
    inter_menu('0')
    if proverka('0'):
        print_desk()
        print('Ура! Победил "0" - игрок')
        break
    count += 1
print('Игра окончена!')
