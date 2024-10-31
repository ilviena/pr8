def correct_input(x):
    if x.isdigit():
        return 1
    elif x[0] == '-' and x[1:].isdigit():
        return 1
    else:
        return 0

while True:
    a = input('Введите первое целое число или "q" для выхода: ')
    if a == 'q':
        break
    b = input('Введите второе целое число или "q" для выхода: ')
    if b == 'q':
        break
    if correct_input(a) and correct_input(b):
        print(f"Сумма {a} и {b} равна {int(a)+int(b)}")
    else:
        print('Неверный ввод!')
