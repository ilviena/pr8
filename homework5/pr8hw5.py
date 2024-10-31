def correct_input(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

sum = 0
while True:
    num = input('Введите число: ')
    if num == 'stop' or num == 'end':
        break
    if correct_input(num):
        sum += float(num)
    else:
        print('Введено не число!')
print(f"Сумма введенных чисел равна {sum}")
