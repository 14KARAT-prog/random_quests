import random

# constants
digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'

# variable
chars = ''

print('Привет, тебя приветствует генератор паролей!')

# def valid number
def input_num_valid(st_input = 'Введите целое число', instruction=1):
    '''
    Описание функции
    Функция запрашивает целое положительное число у пользователя
    Входные параметры:
    st_input - Строка которая будет отображаться для пользователя (default: Введите целое число)
    instruction - Число обозначающая инструкцию для функции (default: 1)
    где 1 - Означает что пользователь должен ввести от 1 до n целое число
    2 - Означает что пользователь вводит булев флаг 0 или 1(Нет или Да соответственно)
    '''
    if instruction == 1:
        while True:
            cnt = input(f'{st_input}:\n')
            try:
                cnt_valid = int(cnt)
                if cnt_valid <= 0:
                    print('Нужно ввести целое число больше 0')
                    continue
                break
            except:
                print('Нужно вести целое число')
        return int(cnt)
    elif instruction == 2:
        while True:
            cnt = input(f'{st_input}:\n')
            try:
                cnt_valid = int(cnt)
                if cnt_valid not in [0, 1]:
                    print('Нужно ввести целое число 0 или 1')
                    continue
                break
            except:
                print('Нужно вести целое число')
        return int(cnt)
    else:
        print('Передан второй некорректный аргумент')

# def generate password
def generate_password(length, chars):
    '''
    Функция для генерации пароля по заданой длине
    Входные параметры:
    length - Длина пароля
    chars - Символы из которых может состоять пароль
    '''
    password = ''
    for _ in range(length):
        password += random.choice(chars)

    return password

# Параметры паролей
cnt_password = input_num_valid('Введите количество генерируемых паролей')
len_password = input_num_valid('Введите длину одного пароля')

# Флаги для значений в пароле
flag_numbers = input_num_valid('Включить цифры в пароль? Введите 0 или 1, где 0 - нет, 1 - да', 2)
flag_upper = input_num_valid('Включить прописные буквы? Введите 0 или 1, где 0 - нет, 1 - да', 2)
flag_lower = input_num_valid('Включить строчные буквы? Введите 0 или 1, где 0 - нет, 1 - да', 2)
flag_symbol = input_num_valid('Включить символы? Введите 0 или 1, где 0 - нет, 1 - да', 2)
flag_ambiguous_symbol = input_num_valid('Исключить неоднозначные символы (пример 0 (ноль) и О (буква О))? Введите 0 или 1, где 0 - нет, 1 - да', 2)

# Массивы с ответами пользователя и константами в программе, важно чтобы было правильное сопостовление
arr_answers = [flag_numbers, flag_upper, flag_lower, flag_symbol]
arr_constants = [digits, uppercase_letters, lowercase_letters, punctuation]

# Отбор символов по флагам от пользователя
for i in range(0 , len(arr_answers)):
    if arr_answers[i] == 1:
        chars += arr_constants[i]

# Удаление неоднозначных символов
if flag_ambiguous_symbol == 1:
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

# Генерация нужного числа паролей и заданой длиной
dict_pasword = {}
for i in range(cnt_password):
    dict_pasword[i+1] = generate_password(len_password, chars)

# Вывод паролей
for key, value in dict_pasword.items():
    print('Пароль {0} : {1}'.format(key, value))