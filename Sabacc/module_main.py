# -*- coding: utf-8 -*-кодировка файла
'''Модуль меню для игры'''
import sys  #библиотека используется для выхода из программы
import os #библиотека используется для очистки экрана
import time #библиотека используется для определения времени
try:
    from colorama import init, Fore#библиотека используется для вывода цветного текста в терминал
except ImportError:
    pass

import player_verxus_player  #импорт из файла player_verxus_player - основного класса игры
import module_regulations
import player_verxus_computer

try:
    init()#инициализация библиотеки colorama
except Exception:
    pass

def results_last_game():
    '''функция выводит дату и результаты 10 последних игр.'''
    try:#Если их меньше 10 - выводит все.
        my_file = open('Save.txt', 'r')
        number_lines = my_file.readlines()
        len_number_lines = len(number_lines) #количество считанных строк
        filename = 'Save.txt'
        first_fail = open(filename, 'r')
        second_fail = first_fail.readlines()
        if len_number_lines > 11:
            len_number_lines = len_number_lines - 10
            for i, line in enumerate(second_fail):#Возвращает enumerate (нумерованный) объект
                line = line.replace("\n", "")#в роли sequence выступает любой итерируемый объект
                if i >= len_number_lines:#если i больше или равно количества строк
                    print(line)#определенного на 80 строке
        else:
            for line in second_fail: #считывание файла построчно
                print(line)
        my_file.close()
        first_fail.close()
    except IOError:
        print("Извините, не удалось считать файл с результатами.")

def rules_of_the_games():
    '''rules_of_the_games - правила игры'''
    print("""
Состав колоды:
Стандартная колода(иногда называемая Оригинальной) для игры в сабакк состоит из
76 карт (60 карт 4-х мастей и 16 картинок):
    Монеты, Фляги, Мечи, Шесты:
        Младшие карты, пронумерованные от 1 до 11
        Старшие карты:
            Командир(12)
            Госпожа(13)
            Мастер(14)
            Туз(15) 
Карты "Гибель", "Выдержка" и "Коварный".
    "Картинки"(две копии каждой карты):
        Королева Воздуха и Тьмы(-2)
        Выносливость(-8)
        Баланс(-11)
        Гибель(-13)
        Выдержка(-14)
        Коварный(-15)
        Звезда(-17)
        Идиот(0) 
Игра обыкновенными картами
Дилер и любой желающий игрок могут перетасовать разделенную на части колоду, 
пока все карты не будут перетасованы и собраны обратно в колоду. Любой игрок 
может снять колоду. Дополнительная чистая карта помещается лицом в основание.
Раздача
Дилер раздает по одной карте рубашкой кверху каждому игроку, включая себя (если
игра ведется без специализированного дилера-дроида) попеременно и затем 
повторяет раздачу. Таким образом, каждый игрок, включая дилера, получает две 
карты.
Процесс игры
Каждая партия играется раундами. Раунд состоит из четырех стадий: 
    - торг;
    - изменение;
    - открытие;
    - получение.
    Торг: Начиная с игрока находящегося слева от дилера, каждый игрок может 
        выбрать - торговаться или спасовать. В дружественных играх, 
        максимальная ставка торга определена заранее. Однако, ставка может быть
        любой по желанию игрока. Казино обычно имеет более строгую систему 
        ставок. Идя по часовой стрелке от того игрока, каждый следующий игрок 
        должен сделать такую же ставку, чтобы остаться в партии. Они также 
        могут поднять ставку. Количество увеличения ставки может быть не 
        больше, чем предопределенный максимум. Если ставка была увеличена, то 
        соответственно все игроки должны, как минимум, сделать такие же ставки, 
        чтобы остаться в партии. Когда ставку больше никто не подымает, первая 
        стадия "торг" закончена. Варианты торга:
        Правила торга казино: Максимальное увеличения ставки - текущая ставка. 
        Т.е., если текущая ставка составляет - N фишек, игрок может поднять 
        ставку максимум на N фишек.
        Правила торга Вуки: Нет никакого минимума или максимума и к ставке и к 
        увеличению ставки. Каждый игрок волен назначить ставку любой суммы, 
        и также увеличить ее на любое количество. 
    Изменение: Дилер бросает шестигранный кубик. Если результат броска составил 
    1, 2 или 3, то никакого изменения не происходит. Если результат броска 4, 5 
    или 6, то происходит изменение. Собственно шанс того что произойдет 
    изменение в раунде, составляет 50 на 50. После изменения каждый игрок 
    выбирает, какую карту оставить, какую выкинуть. Выброшенные карты дилер 
    складывает в основание колоды, ниже чистой карты. После этого дилер раздает
    по одной новой карте каждому игроку с вершины колоды. 
    Открытие: Стадия "открытие" следует за стадией "изменение" только на 
    четвертом и последующих после него раундах. Никто не может открыться, пока 
    не будет сыграно, как минимум, четыре раунда. После этого любой игрок в 
    любом раунде после стадии "изменение" может открыться. Когда игрок 
    открывается, игра немедленно заканчивается, без последней стадии 
    "получение". Каждый кладет на стол свои карты лицом к верху, и победитель и
    выигрыш определяется. 
    Получение: Если никто не решается открыться (или не сыграно 4-х раундов), 
    каждый игрок, начиная с игрока по левую сторону от дилера, по часовой 
    стрелке, может получить дополнительную карту, рубашкой кверху. Игрок может 
    добавить карту к своим картам, если она ему подходит, но также может и 
    отказаться от любой карты на свой выбор, включая и ту карту, которую только 
    что получил. Вы можете иметь больше, но никогда не меньше чем две карты в 
    течении игры. После чего игра продолжается следующим новым раундом, 
    начинаемого со стадии "торг" и продолжается как обычно. 
Определение победителя
Когда карты открываются, каждый открывает лицо своих карт. Игрок, имеющий самый
высокий счет, побеждает и забирает фишки, поставленные на кон.
Если складывается спорная ситуация между двумя или более игроками (чьи 
результаты одинаковы), каждый игрок получает на руки по дополнительной карте. 
Игрок с лучшей измененной комбинацией является победителем. Банк выигрывается 
только в двух случаях и если его никто не берет, он переносится на следующую 
партию.
    Если игрок имеет +23 или -23, он имеет Чистый Сабакк, и выигрывает и кон и 
    банк.
    Игрок, имеющий "Расклад Идиота", по некоторым вариантам правила имеет самый
    лучший результат в сабакке и бьет даже Чистый Сабакк, получая тем самым и 
    кон, и банк. 
В случае одинакового результата, игроки получают по дополнительной карте. Если 
и в этом случае результат совпадет, игроки делят выигрыш пополам. Если оба 
игрока имеют на руках "бомбы", они оба платят штрафы (если используются обычные
 правила), а победитель партии - игрок, имеющий на руках следующую самую 
высокую комбинацию, исключая пасовавших. Если других победителей нет, Банк 
партии идет в Банк Сабакка, а игра начинается новой партией.     
""")

def screencleaning():#очистка экрана
    '''функция очистки экрана'''
    if sys.platform == 'win32':
        os.system('cls')#очистка экрана от адреса файла и прочего
    else:
        os.system('clear')

def endgame():
    '''окончаниe игры, выход в меню'''
    print("Игра окончена\n Для выхода в меню введите exit.") #
    variable_exit_game = input()#ввод значения
    if variable_exit_game == 'exit':
        menu()
    else:#на случай если пользователь ошибся при вводе
        print("Повторите ввод.")
        variable_exit_game = input()
        if variable_exit_game == 'exit': #если все правильно, вызывается меню игры
            menu()
        else:
            menu()

def change_game():
    '''выбор варианта игры'''
    print("Выберите вариант игры:")
    print("1 - игрок против игроков")
    print("2 - игрок против компьютера")
    change = int(input())
    if change == 1:
        player_verxus_player.game_pvp()#вызов функции Игра из файла player_verxus_player
    elif change == 2:
        player_verxus_computer.player_v_computer()
    else:
        print("Введено неверное значение.")

def menu():
    '''функция для меню игры'''
    screencleaning()
    try:
        print(Fore.MAGENTA + "Добро пожаловать в наше казино!") #1 надпись на экране
    except Exception:
        print("Добро пожаловать в наше казино!")
    localtime = time.asctime(time.localtime(time.time())) #вывод текущего времени
    print("Текущее время", localtime) #вывод на экран текущего времени
    while True:    #цикл будет продожаться вечно
        print("""
1 Новая игра
2 Результаты прошлых игр
3 Правила игры
4 Настройки и инструкции к работе с программой
5 Выход
        """)
        print("Введите номер пункта меню\n")#программа выводит на экран слова
        choice = input()
        if choice == "1": #в кавычках и ждет пока игрок выберет пункт меню
            screencleaning()#если пользователь ввел 1, выбирается 1 пункт меню
            change_game()
        elif choice == "2": #следующие пункты меню аналогично 1
            screencleaning()
            results_last_game()#функция находиться в этом файле
        elif choice == "3":
            screencleaning()
            rules_of_the_games()
        elif choice == "4":
            screencleaning()
            print("""
Инструкции к работе с программой:
1. В игре используется английская раскладка.          
2. Если программа спрашивает какое-нибудь число - введите с клавиатуры число.
3. Чтобы ответить на вопрос - нажмите y в случае положительного ответа и n в 
случае отрицательного ответа.
4. Чтобы поместить карту в поле помех - нажмите i.
5. Когда программа спрашивает имя игрока - введите его (можно использовать
любую раскладку).
""")
            pos_answer, neg_answer, interference = module_regulations.read_regulations_with_file()
            print("Настройки игры.\nКлавиши для управления игрой:")
            print("Для положительного ответа ", pos_answer)
            print("Для отрицательного ответа ", neg_answer)
            print("Помещение карт в поле помех ", interference)
            print("  ")
            module_regulations.choice_change_regulations()
        elif choice == "5":
            screencleaning()
            print("Спасибо за посещение нашего казино, ждем вас снова.")
            print("Нажмите клавишу Enter для выхода.")
            input()
            sys.exit()
        else:
            print("Извините, но в меню нет такого пункта", choice)

if __name__ == "__main__":
    print("This is a module with game Sabacc.")
    input("\n\nPress the enter key to exit.")