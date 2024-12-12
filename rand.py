import random

welcome = 'Добро пожаловать в числовую угадайку'
print(welcome)

while True:
    while True:
        num_right = input("Ввдетие целое число больше 0, это число будет правой границей при генерации рандомного числа: ")

        if num_right.isdigit() and int(num_right) >= 1:
            num_right = int(num_right)
            break
        print('Вы ввели некоректное число')

    rand_num = random.randint(1, num_right)


    def is_valid(num):
        try:
            return num.isdigit() and int(num) >= 1 and int(num) <= num_right
        except Exception:
            return False



    while True:
        count = input("Введите количество попыток (от 1 до 100): ")

        if count.isdigit() and int(count) >= 1 and int(count) <= 100:
            count = int(count)
            break
        print("Что-то не так с введеным числом, введите еще раз")


    for i in range(count):
        user_num = input(f"Введите загаданное число от 1 до {num_right}: ")

        if not is_valid(user_num):
            print(f'Вы ввели не верное число или не число, осталось попыток: {count - (i-1)}')
        else:
            user_num = int(user_num)
        if user_num == rand_num and i == 0:
            print(f"Поздравляю, вы угадали с первого раза!")
            break
        elif user_num == rand_num:
            print(f"Поздравляю вы угадали, сделано попыток: {i+1}")
            break
        elif user_num > rand_num:
            print(f"Веденое число больше чем загаданное, осталось попыток: {count - (i+1)}")
        elif user_num < rand_num:
            print(f"Веденое число меньше чем загаданное, осталось попыток: {count - (i+1)}")
    else:
        print(f"К сожалению вы не смогли угадать число от 1 до {num_right}, всего попыток было: {count}")

    again = input("Хотите сыграть еще раз? (введите 'да' если хотите, остальное считается как отказ): ")

    if again.lower() != 'да':
        break

print("Спасибо вы играли в угадайку, увидимся еще")