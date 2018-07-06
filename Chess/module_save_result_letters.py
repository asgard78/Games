# -*- coding: utf-8 -*-
"""Created on Wed Nov 22 17:26:19 2017 @author: Egor """
import time

def write_game_result(board, name_winner):
    '''запись результата игры в файл'''
    file = open('Preserving moves in batches.txt', 'a')
    today = time.asctime(time.localtime(time.time()))#фиксация времени окончания игры
    file.write('Игра закончилась' + today + '\n')
    file.write('Победил игрок' + name_winner + '\n')
    for i in board:
        for element in i:
            element = str(element)
            file.write(element)
    file.close()

def letters_conversions_part_2(answer_player, answer):
    '''преобразования букв в цифры'''
    len_list = len(answer_player)
    if len_list > 0:
        if answer_player[1] == 1:
            answer.append(8)
        elif answer_player[1] == 2:
            answer.append(7)
        elif answer_player[1] == 3:
            answer.append(6)
        elif answer_player[1] == 4:
            answer.append(5)
        elif answer_player[1] == 5:
            answer.append(4)
        elif answer_player[1] == 6:
            answer.append(3)
        elif answer_player[1] == 7:
            answer.append(2)
        elif answer_player[1] == 8:
            answer.append(1)
    return answer

def letters_conversions(answer_player):
    '''преобразования букв в цифры'''
    answer = []
    answer_player.reverse()
    len_list = len(answer_player)
    if len_list > 0:
        if answer_player[0] == 1:
            answer.append('a')
        elif answer_player[0] == 2:
            answer.append('b')
        elif answer_player[0] == 3:
            answer.append('c')
        elif answer_player[0] == 4:
            answer.append('d')
        elif answer_player[0] == 5:
            answer.append('e')
        elif answer_player[0] == 6:
            answer.append('f')
        elif answer_player[0] == 7:
            answer.append('g')
        elif answer_player[0] == 8:
            answer.append('h')
    answer = letters_conversions_part_2(answer_player, answer)
    return answer

def write_time_game_began():
    '''функция записывает время, когда партия начинается'''
    file = open('Preserving moves in batches.txt', 'a')
    value_time = time.asctime(time.localtime(time.time()))  #время хода
    file.write('Игра началась' + value_time + '\n')
    file.close()

def write_step(name_player, value):
    '''запись каждого хода'''
    len_0 = len(value[0])
    len_1 = len(value[1])
    if len_0 > 0 and len_1 > 0:
        value_0 = letters_conversions(value[0])
        value_1 = letters_conversions(value[1])
        value_2 = str(value_0[0]) + str(value_0[1])
        value_3 = str(value_1[0]) + str(value_1[1])
        file = open('Preserving moves in batches.txt', 'a')
        now = time.asctime(time.localtime(time.time()))  #время хода
        file.write('    ' + name_player + ' ' + value_2 + ' - ' + value_3 + ' ' + now + '\n')
        file.close()

if __name__ == "__main__":
    print("This is a module with game Chess.")
    input("\nPress the enter key to exit.")
