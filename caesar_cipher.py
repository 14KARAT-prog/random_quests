print('Привет, тебя приветствует программа Шифр Цезаря!')

def validator(st_input, instruction = 0):
    if instruction == 0:
        while True:
            flag = input(f'{st_input}\n')

            if flag == '1' or flag == '0':
                break
            else:
                print('Введите 0 или 1')
                continue
        return int(flag)
    elif instruction == 1:
        while True:
            flag = input(f'{st_input}\n').lower()

            if flag == 'ru' or flag == 'en':
                break
            else:
                print('Введите ru или en')
                continue
        return flag
    else:
        print('Передан второй некорректный аргумент')


direction = validator('Введите направление 1 или 0, где 1 - шифрование, 0 - дешифрование:', 0)
language = validator('Введите язык алфавита ru или en, где ru - русский, en - английский:', 1)
step_type = validator('Введите в какую сторону был сдвиг 1 или 0, где 1 - вправо, 0 - влево:', 0)

while True:
    step = input('Введите шаг сдвига (Положительное целое число, если алфавит русский то не больше 32 если английский то не больше 25):\n')

    try:
        step_valid = int(step)
        if language == 'ru' and (step_valid <= 0 or step_valid >= 33):
            print('Нужно ввести число от 1 до 32')
            continue
        elif language == 'en' and (step_valid <= 0 or step_valid >= 26):
            print('Нужно ввести число от 1 до 25')
            continue
        break
    except:
        print('Нужно вести целое число')
        continue

step = int(step)

offer = input('Введите строку для шифрования или дешифрования (Необходимо ввести строку в соответсвии с указаным языком алфавита, иначе сработает некорректно):\n')

offer_arr = list(offer)

# Шифрование врпаво - плюсую
# Шифрование влево - минусую
# Дешифрование вправо - минусую
# Дешифрование влево - плюсую

# Первый интервал для большого регистра 65 - 90
# Второй интервал для малого регистра 97 - 122

offer_end = ''

if language == 'en':
    if (direction == 1 and step_type == 1) or (direction == 0 and step_type == 0):
        # Плюсую
        for let in offer:
            let_num = ord(let.lower())

            if let_num >= 97 and let_num <= 122:
                let_num_next = let_num + step

                if let_num_next > 122 and (ord(let) >= 97 and ord(let) <= 122):
                    offer_end += chr(96 + (let_num_next - 122))
                elif let_num_next <= 122 and (ord(let) >= 97 and ord(let) <= 122):
                    offer_end += chr(let_num_next)
                elif let_num_next > 122 and (ord(let) >= 65 and ord(let) <= 90):
                    offer_end += chr((96 + (let_num_next - 122)) - 32)
                else:
                    offer_end += chr(let_num_next - 32)
            else:
                offer_end += let

    if (direction == 1 and step_type == 0) or (direction == 0 and step_type == 1):
        # Минусую
        for let in offer:
            let_num = ord(let.lower())

            if let_num >= 97 and let_num <= 122:
                let_num_next = let_num - step

                if let_num_next < 97 and (ord(let) >= 97 and ord(let) <= 122):
                    offer_end += chr(123 - (97 - let_num_next))
                elif let_num_next >= 97 and (ord(let) >= 97 and ord(let) <= 122):
                    offer_end += chr(let_num_next)
                elif let_num_next < 97 and (ord(let) >= 65 and ord(let) <= 90):
                    offer_end += chr((123 - (97 - let_num_next)) - 32)
                else:
                    offer_end += chr(let_num_next - 32)
            else:
                offer_end += let
elif language == 'ru':
    if (direction == 1 and step_type == 1) or (direction == 0 and step_type == 0):
        # Плюсую
        for let in offer:
            let_num = ord(let.lower())

            if let_num >= 1072 and let_num <= 1103:
                let_num_next = let_num + step

                if let_num_next > 1103 and (ord(let) >= 1072 and ord(let) <= 1103):
                    offer_end += chr(1071 + (let_num_next - 1103))
                elif let_num_next <= 1103 and (ord(let) >= 1072 and ord(let) <= 1103):
                    offer_end += chr(let_num_next)
                elif let_num_next > 1103 and (ord(let) >= 1040 and ord(let) <= 1071):
                    offer_end += chr((1071 + (let_num_next - 1103)) - 32)
                else:
                    offer_end += chr(let_num_next - 32)
            else:
                offer_end += let

    if (direction == 1 and step_type == 0) or (direction == 0 and step_type == 1):
        # Минусую
        for let in offer:
            let_num = ord(let.lower())

            if let_num >= 1072 and let_num <= 1103:
                let_num_next = let_num - step

                if let_num_next < 1072 and (ord(let) >= 1072 and ord(let) <= 1103):
                    offer_end += chr(1104 - (1072 - let_num_next))
                elif let_num_next >= 1072 and (ord(let) >= 1072 and ord(let) <= 1103):
                    offer_end += chr(let_num_next)
                elif let_num_next < 1072 and (ord(let) >= 1040 and ord(let) <= 1071):
                    offer_end += chr((1104 - (1072 - let_num_next)) - 32)
                else:
                    offer_end += chr(let_num_next - 32)
            else:
                offer_end += let

print('Вот что получилось:', offer_end, sep='\n')