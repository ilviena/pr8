def correct_input(x):
    try:
        int(x)
        return True  
    except ValueError:
        return False 

while True:
    a = input('Введите первое целое число или "q" для выхода: ')
    if a == 'q':
        break
    b = input('Введите второе целое число или "q" для выхода: ')
    if b == 'q':
        break
    if correct_input(a) and correct_input(b):
        print(f"Сумма {a} и {b} равна {int(a) + int(b)}")
    else:
        print('Неверный ввод!')
