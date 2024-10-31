def correct_input(x):
    point_flag = 0
    if x[0] == '-':
        for i in x[1:]:
            if i == '.':
                point_flag += 1
                continue
            if not(i.isdigit()) or point_flag > 1:
                return 0
    else:
        for i in x:
            if i == '.':
                point_flag += 1
                continue
            if not(i.isdigit()) or point_flag > 1:
                return 0
    return 1
while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    if correct_input(a) and correct_input(b):
        break
    else:
        print('Неверный ввод!')
a = int(float(a))
b = int(float(b))
if a == b or a-b == 1 or b-a == 1:
    print('Между введенными числами нет целых')
elif a < b:
    print('Все целые числа, расположенные между введенными числами:')
    for i in range(a+1, b):
        print(i)
else:
    print('Все целые числа, расположенные между введенными числами:')
    for i in range(b+1, a):
        print(i)
    
