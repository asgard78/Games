# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:12:26 2017
"""
import random
import time

def read_regulations_with_file():#считывает 3 настройки из файла
    '''считывание настроек из файла'''
    pos_ans = 'y'
    neg_ans = 'n'
    intrfrn = 'i' #interference = сокращенно intrfrn
    try:
        file_open = open('Regulations.txt', 'r')
        for line in file_open:
            if 'Positive_answer' in line:
                pos_ans = line.split()
                pos_ans = pos_ans[1]
            elif 'Negative_answer' in line:
                neg_ans = line.split() #переменной присваивается
                neg_ans = neg_ans[1]
            elif 'Interference' in line:
                intrfrn = line.split() #переменной присваивается
                intrfrn = intrfrn[1]
    except IOError:
        print("Извините, не удалось считать файл с настройками.")
    return pos_ans, neg_ans, intrfrn

POSITIVE_ANSWER, NEGATIVE_ANSWER, INTERFERENCE = read_regulations_with_file()

def repeat_choice_int():#для ввода цифр
    '''если была нажата клавиша Enter при пустой строке ввода'''
    end_cycle = True
    number = 5
    while end_cycle:
        choice = input()
        if len(choice) is not 0:# > 0:
            try:
                choice = int(choice)
            except ValueError:
                number = number - 1
                print("Введено некорректное значение, у вас ", number, " попыток повторного ввода.")
                if number == 0:
                    end_cycle = False
                    choice = random.randint(2, 8)
                    print("Автоматически нажато", choice)
            end_cycle = False
        else:
            number = number - 1
            print("Введено некорректное значение, у вас ", number, " попыток повторного ввода.")
            if number == 0:
                end_cycle = False
                choice = random.randint(2, 8)
                print("Автоматически нажато", choice)
    return choice

def repeat_choice_str():#для ввода букв и слов
    '''если была нажата клавиша Enter при пустой строке ввода'''
    end_cycle = True
    number = 5
    while end_cycle:
        choice = input()
        if len(choice) is not 0:#== 0:
            end_cycle = False
        else:
            print("Вы ничего не ввели, у вас есть", number, " попыток, для ввода нужного значения.")
            number = number - 1
            if number == 0:
                end_cycle = False
                choice = 'n'
                print("Автоматически нажато 'n'.")
    return choice

def field_interference(dict_player):
    '''поле помех'''
    print(dict_player['name'], "вы хотите поместить карты в поле помех?")
    choice = repeat_choice_str()#игрок не хотел изменять карту, он мог "заморозить"
    if choice == POSITIVE_ANSWER:# её значение поместив карту в поле помех в ходе раунда
        i = len(dict_player['player_list'])
        while i > 0:
            print(dict_player['name'], "выберите карту.")
            card_field_interference = repeat_choice_str()
            if card_field_interference in dict_player['player_list']:
                if card_field_interference not in dict_player['list_interference']:
                    dict_player['list_interference'].append(card_field_interference)
                    print("Карта", card_field_interference, "помещена в поле помех")
                else:
                    count_card = dict_player['list_interference'].count(card_field_interference)
                    qwerty = dict_player['player_list'].count(card_field_interference)
                    if count_card < qwerty:
                        dict_player['list_interference'].append(card_field_interference)
                        print("Карта", card_field_interference, "помещена в поле помех")
                    else:
                        print("Карта уже находиться в списке.")
            else:
                print("Вы ввели ошибочные значения карт.")
            i = i - 1
    elif choice == NEGATIVE_ANSWER:
        print("Не забывайте ваши карты могут измениться в любую минуту.")
    return dict_player

def def_check(dict_player, name, number):
    '''проверка - есть ли игрок в игре или нет'''
    if dict_player['name'] is not None:
        number = number + 1
        name = dict_player['name']
    return name, number

def write_rate_in_file(rate):
    '''запись в файл только ставки и времени игры'''
    localtime_2 = time.asctime(time.localtime(time.time()))#фиксация времени окончания игры
    my_file = open('Save.txt', 'a')    #открытие файла в режиме дозаписи
    rate = str(rate) #приведение формата ставки в строку
    my_file.write(localtime_2 + ' ' + rate + '\n')#запиcm времени игры и банка в файл
    my_file.close()    #обязательно закрывается файл

def no_winners(gain):
    '''если победителей в игре нет'''
    print("Победителей нет, банк переходит в следующую игру.")
    write_rate_in_file(gain)

def open_list_stage(name, list_player):
    '''функция для подсчета суммы карт, выводит результат игрока'''
    card_amount = 0#сумма карт
    list_result = []
    if list_player is not None:
        for line in list_player:
            result = line.split()
            list_result.append(result[0])
        for i in list_result:
            try:
                i = int(i)
                card_amount = card_amount + i
            except ValueError:
                pass
        print("Сумма карт игрока", name, "=", card_amount)
    return card_amount

def amount_player(list_player):
    '''функция для подсчета суммы карт, выводит результат игрока'''
    card_amount = 0#сумма карт
    list_result = []
    if list_player is not None:
        for line in list_player:
            result = line.split()
            list_result.append(result[0])
        for i in list_result:
            try:
                i = int(i)
                card_amount = card_amount + i
            except ValueError:
                pass
    return card_amount

def computer_opening_cards(dict_player, val_player):
    '''стадия открытие карт игрока компьютера'''
    answer = False
    if dict_player['amount'] >= val_player:
        answer = True
    return answer

def stage_opening_cards(dict_player):
    '''стадия открытие карт'''
    answer = False#игрок открыл карты или нет
    if dict_player['name'] is not None:# and len(game_result) == 0:
        print(dict_player['name'], "будете открывать карты?")
        choice = repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            if dict_player['name'] and dict_player['player_list'] is not None:
                answer = True
        elif choice == NEGATIVE_ANSWER:
            print(dict_player['name'], "не стал раскрывать карты")
        elif choice == INTERFERENCE:
            dict_player = field_interference(dict_player)
    return answer

def several_winners_number(dict_player, gain):#dict - словарь
    '''один игрок'''
    print("Победил игрок", dict_player['name'], ", его выигрыш =", gain)
    write_in_file(dict_player['name'], gain)#и его результата в файл

def random_name():
    '''выбор произвольного имени для игрока '''
    #'''если была нажата клавиша Enter при пустой строке ввода'''
    bukva = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',
             'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
             'x', 'c', 'v', 'b', 'n', 'm', 'p', 'z']
    end_cycle = True
    number = 5
    truth = True
    while end_cycle:
        choice = input()
        if len(choice) is not 0:#== 0:
            end_cycle = False
        else:
            print("Вы ничего не ввели, у вас есть", number, " попыток, для ввода нужного значения.")
            number = number - 1
            if number == 0:
                end_cycle = False
                while truth:
                    random_bukva = random.choice(bukva)
                    choice = choice + random_bukva
                    number = number + 1
                    if number > 5:
                        truth = False
                print("Автоматически нажато")
    return choice

def player_name():
    '''функция для ввода имени игрока'''
    print("Имя игрока: ")
    name = random_name()#ввод имени игроком и присваивание его переменной
    if name is None:
        name = random_name()
    return name

def player_bankroll():
    '''функция для ввода сумму денег, на которые игрок будет играть'''
    print("Введите сумму денег предназначенную для игры.")
    try:  #исключения, если все нормально, выполняется следующая строка
        bankroll = repeat_choice_int()#repeat_bankroll_int()
    except ValueError:#если игрок ввел неправильное значение
        print("Повторите ввод.")#вызывается исключение и игрок снова может ввести значение
        bankroll = repeat_choice_int()
    return bankroll

def block():
    '''шестигранный кубик, предназначен для измененения карт'''
    block_1 = random.randint(1, 6)
    return block_1

def read_rate_in_file():
    '''функция считывания информации из файла'''
    line_rate = 0.0
    try:
        my_file = open('Rate.txt', 'r')    #открытие файла в режиме чтение
        for line in my_file: #считывание файла построчно
            try:
                line_rate = float(line)
            except ValueError:
                line_rate = 0.0
        my_file.close()
    except IOError:
        print("Извините, не удалось считать файл с данными предыдущих ставок.")
    return line_rate

def read_two_regulations_with_file():  #считывает 2 (из 3) настройки из файла
    '''считывание настроек из файла''' #там, где нужны только
    pos_ans = 'y'                      #положительный и отрицательный ответы
    neg_ans = 'n'
    try:
        file_open = open('Regulations.txt', 'r')
        for line in file_open:
            if 'Positive_answer' in line:
                pos_ans = line.split()
                pos_ans = pos_ans[1]
            elif 'Negative_answer' in line:
                neg_ans = line.split() #переменной присваивается
                neg_ans = neg_ans[1]
    except IOError:
        print("Извините, не удалось считать файл с настройками.")
    return pos_ans, neg_ans

def rate_with_last_games():
    '''функция перехода ставки из прошлой игры'''
    pos_answer, neg_answer = read_two_regulations_with_file()
    rate_in_file = read_rate_in_file()
    rate = 0
    if rate_in_file > 0:
        print("Из прошлой игры возможен переход банка =", rate_in_file)
        choice = input("Вы согласны?\n")
        if choice == pos_answer:
            rate = rate_in_file
            my_file = open('Rate.txt', 'w')
            my_file.write(' ')
            my_file.close()
        elif choice == neg_answer:
            print("Ставка останется до востребования.")
        else:
            print("Вы нажали не на ту клавишу.")
    return rate

def write_in_file(name, rate):
    '''функция запись в файл имени победителя и его выигрыша'''
    localtime_2 = time.asctime(time.localtime(time.time()))#фиксация времени окончания игры
    my_file = open('Save.txt', 'a')
    rate = str(rate)
    name = str(name)
    my_file.write(localtime_2 + ' ' + name + ':' + rate + '\n')
    my_file.close()

def function_victory(list_of_game_results):
    '''нахождение модуля значений каждого списка'''
    list_of_game_results = function_list_game_results(list_of_game_results)
    high_card = max(list_of_game_results, key=abs)
    abscard = list_of_game_results.count(abs(high_card))
    if abscard == 0:
        abscard = list_of_game_results.count(high_card)
    return abscard

def function_list_game_results(list_game_results):
    '''удаление результатов из списка'''
    copy_list_game_results = list_game_results
    for i in copy_list_game_results:
        if i > 23:
            list_game_results.remove(i)
        if i < -23:
            list_game_results.remove(i)
    return list_game_results

if __name__ == "__main__":
    print("This is a module with game Sabacc.")
    input("\n\nPress the enter key to exit.")
