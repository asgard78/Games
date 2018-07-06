# -*- coding: utf-8 -*-
"""
Начало игры
"""
import module_main

try:#проверка наличия файла ставки предыдущих игр
    FILE_RATE = open('Rate.txt', 'r')    #открытие файла в режиме чтение
    FILE_RATE.close()
except IOError:
    FILE_RATE = open('Rate.txt', 'w')    #открытие файла в режиме чтение
    FILE_RATE.close()

try:#проверка наличия файла с настройками
    FILE_REGULATIONS = open('Regulations.txt', 'r')
    FILE_REGULATIONS.close()
except IOError:
    REGULATIONS_GAME = """Positive_answer y
Negative_answer n
Interference i"""
    REGULATIONS = open('Regulations.txt', 'w')    #открытие файла в режиме записи
    REGULATIONS.write(REGULATIONS_GAME + '\n')
    REGULATIONS.close()    #обязательно закрывается файл

try:#проверка наличия файла с результатами игр
    FILE_SAVE = open('Save.txt', 'r')    #открытие файла в режиме чтение
    FILE_SAVE.close()
except IOError:
    SAVE = open('Save.txt', 'w')    #открытие файла в режиме записи
    SAVE.close()    #обязательно закрывается фай

module_main.menu()
