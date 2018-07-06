"""Изменения настроек игры"""
# -*- coding: utf-8 -*-
import random

import module_functions

def repeat_choice_type_str():#для ввода букв и слов
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
                english = ['q', 'w', 'e', 'r', 't', 'y', 'u',
                           'i', 'o', 'p', 'a', 's', 'd', 'f',
                           'g', 'h', 'j', 'k', 'l', 'z', 'x',
                           'c', 'v', 'b', 'n', 'm']
                choice = random.choice(english)
                print("Автоматически нажато ", choice)
    return choice

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

def write_in_file(pos_ans, neg_ans, intrfrn):
    '''функция запись в файл имени победителя и его выигрыша'''
    my_file = open('Regulations.txt', 'w')
    my_file.write("Positive_answer" + ' ' + pos_ans + '\n')
    my_file.write("Negative_answer" + ' ' + neg_ans + '\n')
    my_file.write("Interference" + ' ' + intrfrn + '\n')
    my_file.close()

def change_regulation(choice_change, pos_ans, neg_ans, intrfrn):
    '''выбор наcтройки для ее изменения'''
    if choice_change == 1:
        print("Введите значение.\n")
        pos_ans = repeat_choice_type_str()
        write_in_file(pos_ans, neg_ans, intrfrn)
    elif choice_change == 2:
        print("Введите значение.\n")
        neg_ans = repeat_choice_type_str()
        write_in_file(pos_ans, neg_ans, intrfrn)
    elif choice_change == 3:
        print("Введите значение.\n")
        intrfrn = repeat_choice_type_str()
        write_in_file(pos_ans, neg_ans, intrfrn)
    else:
        print("Вы ввели неверное значение.")
    return pos_ans, neg_ans, intrfrn

def choice_change_regulations():
    '''будет игрок менять настройки игры или нет'''
    pos_ans = 'y'
    neg_ans = 'n'
    intrfrn = 'i'
    i = 3
    while i > 0:#for i in range(3):
        i = i - 1
        print("Вы хотите изменить настройки игры?")
        choice = module_functions.repeat_choice_str()
        if choice == 'y':
            print("""Какие настройки вы хотите изменить? Нажмите соответствующую цифру.
Для положительного ответа = 1
Для отрицательного ответа = 2
Помещение карт в поле помех = 3\n""")
            choice_change = module_functions.repeat_choice_int()
            pos_ans, neg_ans, intrfrn = change_regulation(choice_change, pos_ans, neg_ans, intrfrn)
        elif choice == 'n':
            print("Вы не захотели изменить настрoйки.")
            break
        else:
            print("Настройки не были изменены.")

if __name__ == "__main__":
    print("This is a module with Regulations for the games.")
    input("\n\nPress the enter key to exit.")
