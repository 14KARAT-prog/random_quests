import random

word_list_easy = ['лист', 'привет', 'ноль', 'папа', 'лиса', 'собака', 'кот', 'рыба', 'мысль'
                  , 'мама', 'часы', 'дядя', 'река', 'врач', 'ручка', 'буква', 'слово', 'сосед'
                  , 'доход', 'мясо'
                  ]
word_list_medium = ['начало', 'экономика', 'мужчина', 'ресурс', 'кандидат', 'субъект', 'пьеса'
                    , 'таблица', 'препарат', 'техника', 'саженец', 'телескоп', 'уголь', 'фантом'
                    , 'хозяин', 'центр', 'частокол', 'шампур', 'электричество', 'ятаган'
                    ]
word_list_hard = ['шарнир', 'сварганить', 'челядь', 'теплоэлектроцентраль', 'углежжение'
                  , 'франк', 'хитон', 'целлюлоза', 'элеватор', 'явствовать', 'янычар'
                  , 'эмир', 'юрисдикция', 'фамильяр', 'топаз', 'сульфид', 'сияние', 'угнетатель'
                  , 'хускарл', 'шкодить'
                  ]

# Генерим рандомное слово и приводим в верхний регистр
def get_world(word_list):
    word = random.choice(word_list).upper()
    return word

# Рисуем висилицу
def display_hangman(tries):
    stages = [# финальное состояние: голова, торс, обе руки, обе ноги
        """
            ---------
            |       |
            |       0
            |      \\|/
            |       |
            |      / \\
           ---
        """,
        # голова, торс, обе руки, одна нога
        """
            ---------
            |       |
            |       0
            |      \\|/
            |       |
            |      /
           ---
        """,
        # голова, торс, обе руки
        """
            ---------
            |       |
            |       0
            |      \\|/
            |       |
            |      
           ---
        """,
        # голова, торс и одна рука
        """
            ---------
            |       |
            |       0
            |      \\|
            |       |
            |      
           ---
        """,
        # голова и торс
        """
            ---------
            |       |
            |       0
            |       |
            |       |
            |      
           ---
        """,
        # голова
        """
            ---------
            |       |
            |       0
            |       
            |       
            |      
           ---
        """,
        # начальное состояние
        """
            ---------
            |       |
            |       
            |       
            |       
            |      
           ---
        """
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)   # строка, содержащая символы _ на каждую букву задуманного слова
    tries_num = 6                       # количество попыток
    guessed = False                    # сигнальная метка, по умолчанию False - означает слово не угадано
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов

    print(f'Начальное кол-во попыток = {str(tries_num)}')
    print('Начальное состояние:', display_hangman(tries_num))
    print(f'Кол-во букв в слове: {len(word)}', word_completion, sep='\n\n', end='\n\n')
    print('Вы можете назвать слово целиком в любой момент, либо называть по одной букве - все из этого считается за попытку'
          , 'Если вписать больше одной буквы, то это будет считаться за попытку угадать слово'
          , 'Использовать можно только буквы русского алфавита от А до Я'
          , sep='\n')

    while not guessed:
        let = input('Напишите слово целиком или букву: ')

    # Переменая которая пропускает итерацию цикла
        cont = False
    # Проверяю каждый символ который ввел пользователь, если это не буква русского алфавита, то заного ввод
        for w in let:
            if ord(w) < 1040 or ord(w) > 1103:
                print('Необходимо ввести букву или слово символами русского алфавита')
                cont = True
                break

        if cont:
            continue

        let = let.upper()

    # Проверяю вводил ли пользователь такую букву или слово ранее
        if let in guessed_letters:
            print('Такую букву вы уже вводили, попробуйте другую')
            continue
        elif let in guessed_words:
            print('Такое слово вы уже вводили попробуйте другое')
            continue
        
    # Основная логическая ветка игры
        if let == word:
            print('Поздравляю, вы угадали!', f'Загаданное слово: {word}', sep='\n')
            guessed = True
            continue
        elif len(let) > 1 and let != word:
            guessed_words.append(let)
            tries_num = tries_num - 1
            if tries_num == 0:
                print('Слово неверное, к сожелению вы проиграли:(')
                print(display_hangman(tries_num))
                print(f'Загаданное слово: {word}')
                break
            print('Слово неверное', f'Осталось попыток = {tries_num}', sep='\n')
            print('Текущее состояние:', display_hangman(tries_num))
        elif len(let) == 1 and let in word:
            # Ищу позиции букв в слове
            # Запаковываю word_completion в массив
            # Заменяю "_" на букву
            # Заменяю старый word_completion на новый
            index_let = [pos for pos, char in enumerate(word) if char == let]
            temp = list(word_completion)
            for i in index_let:
                temp[i] = list(word)[i]
            word_completion = ''.join(temp)
            if '_' not in word_completion:
                print('Поздравляю вы угадали слово!', f'Загаданное слово: {word}', sep="\n")
                guessed = True
                continue
            else:
                guessed_letters.append(let)
                print('Вы угадали букву!', word_completion, sep='\n\n', end='\n\n')
                continue
        else:
            guessed_letters.append(let)
            tries_num = tries_num - 1
            if tries_num == 0:
                print('Буква неверная, к сожелению вы проиграли:(')
                print(display_hangman(tries_num))
                print(f'Загаданное слово: {word}')
                break
            print('Буква неверная', f'Осталось попыток = {tries_num}', sep='\n')
            print('Текущее состояние:', display_hangman(tries_num))

while True:
    print('Давай сыграем с тобой в угадайку слов!')
    print('Выбери уровень сложности 1,2,3,4 где', '1 - легкий', '2 - средний', '3 - тяжелый', '4 - случайный из трех', sep='\n')
    lvl = input(': ')

    if lvl == '1':
        play(get_world(word_list_easy))
    # Остановился тут

