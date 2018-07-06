# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:12:26 2017
"""
import random
import time

import module_regulations

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

def rate_with_last_games():
    '''функция перехода ставки из прошлой игры'''
    pos_answer, neg_answer = module_regulations.read_two_regulations_with_file()
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

def ask():#функция позволяет задать вопросы игрокам в начале игры, q = question
    '''функция позволяет задать вопросы игрокам в начале игры'''
    response = None
    low = 2
    high = 9
    number = 5
    print("Сколько игроков участвует? (2 - 8)")
    response = repeat_choice_int()
    while response not in range(low, high):
        number = number - 1
        print("Введено некорректное значение, у вас есть", number, " попыток повторного ввода.")
        response = repeat_choice_int()
        if number == 0:
            response = random.randint(2, 8)
            print("Автоматически выбрано значение", response)
    return response

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

def repeat_bankroll_int():#для ввода цифр
    '''если была нажата клавиша Enter при пустой строке ввода'''
    end_cycle = True
    number = 5
    while end_cycle:
        choice = input()
        if len(choice) is not 0:# > 0:
            choice = int(choice)
            end_cycle = False
        else:
            number = number - 1
            print("Введено некорректное значение, у вас есть", number, " попыток повторного ввода.")
            if number == 0:
                end_cycle = False
                choice = random.randint(10, 50)#диапазон денег, на которые будет играть пользователь
                print("Автоматически нажато", choice)
    return choice

def player_bankroll():
    '''функция для ввода сумму денег, на которые игрок будет играть'''
    print("Введите сумму денег предназначенную для игры.")
    try:  #исключения, если все нормально, выполняется следующая строка
        bankroll = repeat_bankroll_int()
    except ValueError:#если игрок ввел неправильное значение
        print("Повторите ввод.")#вызывается исключение и игрок снова может ввести значение
        bankroll = repeat_choice_int()
    return bankroll

def block():
    '''шестигранный кубик, предназначен для измененения карт'''
    block_1 = random.randint(1, 6)
    return block_1

def function_list_game_results(list_game_results):
    '''удаление результатов из списка'''
    copy_list_game_results = list_game_results
    for i in copy_list_game_results:
        if i > 23:
            list_game_results.remove(i)
        if i < -23:
            list_game_results.remove(i)
    return list_game_results

def function_victory(list_of_game_results):
    '''нахождение модуля значений каждого списка'''
    list_of_game_results = function_list_game_results(list_of_game_results)
    high_card = max(list_of_game_results, key=abs)
    abscard = list_of_game_results.count(abs(high_card))
    if abscard == 0:
        abscard = list_of_game_results.count(high_card)
    return abscard

def write_in_file(name, rate):
    '''функция запись в файл имени победителя и его выигрыша'''
    localtime_2 = time.asctime(time.localtime(time.time()))#фиксация времени окончания игры
    my_file = open('Save.txt', 'a')
    rate = str(rate)
    name = str(name)
    my_file.write(localtime_2 + ' ' + name + ':' + rate + '\n')
    my_file.close()

def write_rate_in_file(rate):
    '''запись в файл только ставки и времени игры'''
    my_file = open('Rate.txt', 'w')    #открытие файла в режиме дозаписи
    rate = str(rate) #приведение формата ставки в строку
    my_file.write(rate + '\n')
    my_file.close()    #обязательно закрывается файл

if __name__ == "__main__":
    print("This is a module with game Sabacc.")
    input("\n\nPress the enter key to exit.")
