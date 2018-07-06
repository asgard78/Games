# -*- coding: utf-8 -*-
"""Created on Mon Oct 23 22:16:19 2017 @author: Egor"""
import sys

import module_movement_figure_letters as movement_figure_letters
import module_board_letters as board_letter
import module_beat_figura_letters
import module_save_result_letters

LIST_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]
PLAYER_WHITE = ['white']
PLAYER_BLACK = ['black']
LIST_WHITE = []  #список координат, куда бьют все белые фигуры
LIST_BLACK = []  #список координат, куда бьют все черные фигуры
SHAH_COORDINATES = []  #координаты фигур(ы), объявивших шах

def exit_program():
    '''выход из программы'''
    answer = input("Если хотите выйти из игры - нажмите y.\n")
    if answer == 'y':
        sys.exit()
    else:
        pass

def name_players():
    '''игроки вводят свои имена'''
    player_white = ''
    player_black = ''
    print("Игрок 1 (белыми шахматами) введите свое имя:")
    player_white = input()
    print("Игрок 2 (черными шахматами) введите свое имя:")
    player_black = input()
    PLAYER_WHITE.insert(0, player_white)
    PLAYER_BLACK.insert(0, player_black)
    return player_white, player_black

def question_coordinates(player):
    '''новые координаты фигуры'''
    print(player, "выберите новые координаты фигуры?")
    answer = input()
    len_answer = len(answer)
    if len_answer == 0:
        exit_program()
        answer = question_coordinates(player)
    return answer

def numbers_conversions(answer_player, answer):
    '''преобразования цифр в координату'''
    for i in answer_player:
        if i == '8':
            answer.append(1)
        elif i == '7':
            answer.append(2)
        elif i == '6':
            answer.append(3)
        elif i == '5':
            answer.append(4)
        elif i == '4':
            answer.append(5)
        elif i == '3':
            answer.append(6)
        elif i == '2':
            answer.append(7)
        elif i == '1':
            answer.append(8)
    return answer

def letters_conversions(answer_player):
    '''преобразования букв в цифры'''
    answer = []
    for i in answer_player:
        if i == 'a':
            answer.append(1)
        elif i == 'b':
            answer.append(2)
        elif i == 'c':
            answer.append(3)
        elif i == 'd':
            answer.append(4)
        elif i == 'e':
            answer.append(5)
        elif i == 'f':
            answer.append(6)
        elif i == 'g':
            answer.append(7)
        elif i == 'h':
            answer.append(8)
    answer = numbers_conversions(answer_player, answer)
    answer.reverse()
    return answer

def define_coordinates_figura(figura, board):
    '''определение координат любой фигуры'''
    coordinates_figura = []
    for i in board:
        for element in i:
            if element == figura:
                coordinates_figura = [board.index(i), i.index(element)]
    return coordinates_figura

def check_figure(coordinates_figura):
    '''проверка фигуры для рокировки'''
    if coordinates_figura in movement_figure_letters.FIGURES_MOVE:
        print("Рокировка невозможна, т.к. эта фигура уже ходила.")
        coordinates_figura.clear()
    return coordinates_figura

def castling_figures(change, answer, board, coordinates_figura):
    '''рокировка фигур'''
    coordinates_rook = []
    colour = ''
    coordinates_figura = check_figure(coordinates_figura)#проверка ходов короля
    king = board[coordinates_figura[0]][coordinates_figura[1]]
    if king == 'Кор(б)' or king == 'Кор(ч)':  #эта фигура белый или черный король
        if answer in change:
            colour = movement_figure_letters.color_definition(coordinates_figura, board)
            if colour == 'white':
                if answer[0] == 8 and answer[1] == 7:
                    coordinates_rook = check_figure([8, 8])
                    coordinates_king = [8, 6]
                elif answer[0] == 8 and answer[1] == 3:
                    coordinates_rook = check_figure([8, 1])
                    coordinates_king = [8, 4]
            elif colour == 'black':
                if answer[0] == 1 and answer[1] == 7:
                    coordinates_rook = check_figure([1, 8])
                    coordinates_king = [1, 7]
                elif answer[0] == 1 and answer[1] == 3:
                    coordinates_rook = check_figure([1, 1])
                    coordinates_king = [1, 3]
            if coordinates_rook not in movement_figure_letters.FIGURES_MOVE:
                if coordinates_figura not in movement_figure_letters.FIGURES_MOVE:
                    print("Произошла рокировка.")
                    rook = board[coordinates_rook[0]][coordinates_rook[1]]
                    board[coordinates_king[0]][coordinates_king[1]] = rook
                    board[answer[0]][answer[1]] = king
                    board[coordinates_rook[0]][coordinates_rook[1]] = '      '
                else:
                    print("Рокировка невозможна, потому что король уже ходил.")
            else:
                print("Рокировка невозможна, потому что тура уже ходила.")
    return board

def take_on_the_aisle(change, board, value): #взятие на проходе
    '''взятие на проходе'''
    list_beat_black_pawn = module_beat_figura_letters.beat_black_pawn(board, change)
    list_beat_white_pawn = module_beat_figura_letters.beat_white_pawn(board, change)
    len_aisle = len(movement_figure_letters.AISLE)
    if len_aisle > 0:
        change.append(value)
        movement_figure_letters.AISLE.clear()
    if value in list_beat_black_pawn or value in list_beat_white_pawn:
        movement_figure_letters.AISLE = value
        change.append(value)
    return change

def check_pawn(figura, change, answer):
    '''проверка является ли фигура пешкой'''
    if figura == ' П(ч) ' or figura == ' П(б) ':
        change = take_on_the_aisle(change, board_letter.BOARD, answer) #взятие на проходе
    return change

def function_mat(change):
    '''функция шах королю'''
    white_king = define_coordinates_figura('Кор(б)', board_letter.BOARD)
    black_king = define_coordinates_figura('Кор(ч)', board_letter.BOARD)
    if white_king in change:
        print("Мат белому королю.")
        movement_figure_letters.MAT_KING = True
    if black_king in change:
        print("Мат черному королю.")
        movement_figure_letters.MAT_KING = True

def new_coordinate(name_player, figura, change, coordinates_figure):
    '''новые кординаты фигуры'''
    answer = question_coordinates(name_player)  #новые координаты фигуры
    answer = letters_conversions(answer)  #преобразования букв в цифры
    if answer[0] not in LIST_NUMBERS and answer[1] not in LIST_NUMBERS:
        answer = new_coordinate(name_player, figura, change, coordinates_figure)
    change = check_pawn(figura, change, answer)
    if answer in change:
        function_mat(change)
        board_letter.BOARD[answer[0]][answer[1]] = figura
    elif answer not in change:
        print("Вы ввели координаты занятого места на доске.")
        answer = new_coordinate(name_player, figura, change, coordinates_figure)
    else:
        print("Вы не можете поставить туда фигуру.")
        answer = new_coordinate(name_player, figura, change, coordinates_figure)
    return answer

def clear_after_aisle(moves, answer, current_figura, coordinates_figura):
    '''удаление пешки с игрового поля после взятия на проходе'''#current_figura текущая фигура
    answer = list(answer)
    moves.append(answer)
    len_list = len(moves)
    if len_list > 1:
        last_figura = moves[-2]
        if current_figura == ' П(ч) ' or current_figura == ' П(б) ':
            if answer[0] != coordinates_figura[0] and answer[1] != coordinates_figura[1]:
                board_letter.BOARD[last_figura[0]][last_figura[1]] = board_letter.SPACE
    return moves

def movement_of_figures(name_player, coordinate_figura, change, moves):
    '''передвижение фигур'''  #coordinates_figura = координаты фигуры
    len_change = len(change)
    answer = []
    if len_change == 0:
        print("Нет возможных ходов для фигуры.")
    else:
        figura = board_letter.BOARD[coordinate_figura[0]][coordinate_figura[1]]
        answer = new_coordinate(name_player, figura, change, coordinate_figura)
        moves = clear_after_aisle(moves, answer, figura, coordinate_figura)
        board_letter.BOARD = castling_figures(change, answer, board_letter.BOARD, coordinate_figura)
        try:
            board_letter.BOARD[coordinate_figura[0]][coordinate_figura[1]] = board_letter.SPACE
        except TypeError:  #операция применена к объекту несоответствующего типа
            print("None")
    return answer, moves

def check_coordinates(answer, player):
    '''проверка введенных координат'''
    print(player, "выберите координаты фигуры?")
    answer = input()
    len_answer_player = len(answer)#проверка количества введенных символов
    if len_answer_player == 0:
        answer = check_coordinates(answer, player)#define_coordinate(answer, player)
    elif len_answer_player == 2:
        check_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']#проверка правильности
        check_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']#введенных символов
        if answer[0] not in check_letters:
            print("Некорректные координаты, пожалуйста повторите ввод.")
            answer = check_coordinates(answer, player)#define_coordinate(answer, player)
        elif answer[1] not in check_numbers:
            print("Некорректные координаты, пожалуйста повторите ввод.")
            answer = check_coordinates(answer, player)#define_coordinate(answer, player)
    elif len_answer_player > 2:
        answer = check_coordinates(answer, player)#define_coordinate(answer, player)
    copy = answer    #проверка цвета выбранной фигуры
    copy = letters_conversions(copy)
    if '(б)' in board_letter.BOARD[copy[0]][copy[1]]:
        if player not in PLAYER_WHITE:
            answer = check_coordinates(answer, player)#define_coordinate(answer, player)
    elif '(ч)' in board_letter.BOARD[copy[0]][copy[1]]:
        if player not in PLAYER_BLACK:
            answer = check_coordinates(answer, player)#define_coordinate(answer, player)
    return answer

def define_coordinate(answer, player):
    '''вопрос игроку'''
    answer = check_coordinates(answer, player)
    answer = letters_conversions(answer)
    return answer

def stroke(player):  #ход
    '''будет ход или нет'''
    answer = []
    answer = define_coordinate(answer, player)
    if board_letter.BOARD[answer[0]][answer[1]] == board_letter.SPACE:
        print("Вы ввели координаты пустого места на доске.")
        answer = define_coordinate(answer, player)
#    else:
#        print("Повторите ввод.")
#        answer = define_coordinate(answer, player)
    return answer

def output_board():
    '''вывод фигур на экран'''
    for i in board_letter.BOARD:
        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])

def add_in_rooks_and_kings(coordinates_figure, board):
    '''список ходов каждой туры и/или короля'''
    name = movement_figure_letters.name_definition(coordinates_figure, board)
    if 'rook' in name:
        movement_figure_letters.FIGURES_MOVE.append(coordinates_figure)
    elif 'king' in name:
        movement_figure_letters.FIGURES_MOVE.append(coordinates_figure)

def end_game(board):
    '''условие конца игры'''
    mat = False
    winner = ''
    list_board = []
    for i in board:
        for element in i:
            figura = board[board.index(i)][i.index(element)]
            list_board.append(figura)
    if 'Кор(б)' not in list_board:  #белый король
        mat = True
        winner = 'black'
    elif 'Кор(ч)' not in list_board:  #черный король
        mat = True
        winner = 'white'
    return mat, winner

def one_player(name_player, moves, counter, game_continues):
    '''игровой процесс для одного игрока'''
    output_board()                             #вывод игровой доски на экран
    coordinates_figura = stroke(name_player)  #ход игрока, след. строка - определение фигуры
    change = movement_figure_letters.figure_definition(coordinates_figura, board_letter.BOARD)
    change = module_beat_figura_letters.pawn_beat(coordinates_figura, board_letter.BOARD, change)
    coordinata, moves = movement_of_figures(name_player, coordinates_figura, change, moves)
    add_in_rooks_and_kings(coordinates_figura, board_letter.BOARD)
    module_save_result_letters.write_step(name_player, [coordinates_figura, coordinata])
    counter = counter + 1
    mat, winner = end_game(board_letter.BOARD)
    name_winner = ''
    if winner in PLAYER_WHITE:
        name_winner = PLAYER_WHITE[0]
    elif winner in PLAYER_BLACK:
        name_winner = PLAYER_BLACK[0]
    if mat is True:
        game_continues = False
    return game_continues, counter, name_winner

def game_cycle():
    '''игровой цикл'''
    continues = True  #игра продолжается
    counter = 0  #счетчик
    moves = []
    player_white = ''  #имя играющего белыми шахматами
    player_black = ''  #имя играющего черными шахматами
    name_winner = ''  #имя победителя
    while continues:
        if counter == 0:
            player_white, player_black = name_players()
        module_save_result_letters.write_time_game_began()
        if continues is True and movement_figure_letters.MAT_KING is False:
            continues, counter, name_winner = one_player(player_white, moves, counter, continues)
        if continues is True and movement_figure_letters.MAT_KING is False:
            continues, counter, name_winner = one_player(player_black, moves, counter, continues)
    module_save_result_letters.write_game_result(board_letter.BOARD, name_winner)
    print("Игра закончилась. Партию выиграл - ", name_winner)

if __name__ == "__main__":
    print("This is a module with game Chess.")
    input("\nPress the enter key to exit.")
