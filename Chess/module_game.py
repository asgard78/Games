# -*- coding: utf-8 -*-
"""Created on Mon Oct 23 22:16:19 2017 @author: Egor"""
import module_movement_figure
import module_board
import module_beat_figura
import module_save_result

LIST_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]
PLAYER_WHITE = ['white']
PLAYER_BLACK = ['black']
LIST_WHITE = []  #список координат, куда бьют все белые фигуры
LIST_BLACK = []  #список координат, куда бьют все черные фигуры
SHAH_COORDINATES = []  #координаты фигур(ы), объявивших шах

def what_color_figura(player, coordinates_figura):
    '''определение цвета фигуры, которую игрок выбрал'''
    colour = module_movement_figure.color_definition(coordinates_figura, module_board.BOARD)
    if colour == PLAYER_WHITE[1] and player == PLAYER_WHITE[0]:
        pass
    elif colour == PLAYER_BLACK[1] and player == PLAYER_BLACK[0]:
        pass
    else:
        coordinates_figura.clear()
    return coordinates_figura

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
        answer = question_coordinates(player)
    return answer

def numbers_conversions(answer_player):
    '''преобразования цифр в координату'''
    answer = []
    if answer_player[0] == 8:
        answer_player.remove(8)
        answer_player.insert(0, 1)
    elif answer_player[0] == 7:
        answer_player.remove(7)
        answer_player.insert(0, 2)
    elif answer_player[0] == 6:
        answer_player.remove(6)
        answer_player.insert(0, 3)
    elif answer_player[0] == 5:
        answer_player.remove(5)
        answer_player.insert(0, 4)
    elif answer_player[0] == 4:
        answer_player.remove(4)
        answer_player.insert(0, 5)
    elif answer_player[0] == 3:
        answer_player.remove(3)
        answer_player.insert(0, 6)
    elif answer_player[0] == 2:
        answer_player.remove(2)
        answer_player.insert(0, 7)
    elif answer_player[0] == 1:
        answer_player.remove(1)
        answer_player.insert(0, 8)
    for i in answer_player:
        int_i = int(i)
        answer.append(int_i)
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
        else:
            value = int(i)
            answer.append(value)
    answer.reverse()
    answer = numbers_conversions(answer)
    return answer

def define_coordinates_figura(figura, board):
    '''определение координат любой фигуры'''
    coordinates_figura = []
    for i in board:
        for element in i:
            if element == figura:
                coordinates_figura = [board.index(i), i.index(element)]
    return coordinates_figura

def castling_figures(king, change, answer, board):
    '''рокировка фигур'''
    coordinates_rook = []
    colour = ''
    if king == '\u265A' or king == '\u2654':#эта фигура белый или черный король
        if answer in change:
            coordinates_figura = define_coordinates_figura(king, board)
            colour = module_movement_figure.color_definition(coordinates_figura, board)
        if colour == 'white':
            if answer[0] == 8 and answer[1] == 7:
                coordinates_rook = [8, 8]
            elif answer[0] == 8 and answer[1] == 3:
                coordinates_rook = [8, 1]
        elif colour == 'black':
            if answer[0] == 1 and answer[1] == 7:
                coordinates_rook = [1, 8]
            elif answer[0] == 1 and answer[1] == 3:
                coordinates_rook = [1, 1]
        if coordinates_rook not in module_movement_figure.FIGURES_MOVE:
            print("Произошла рокировка.")
            rook = board[coordinates_rook[0]][coordinates_rook[1]]
            board[coordinates_rook[0]][coordinates_rook[1]] = king
            board[answer[0]][answer[1]] = rook

def take_on_the_aisle(change, board, value): #взятие на проходе
    '''взятие на проходе'''
    list_beat_black_pawn = module_beat_figura.beat_black_pawn(board, change)
    list_beat_white_pawn = module_beat_figura.beat_white_pawn(board, change)
    len_aisle = len(module_movement_figure.AISLE)
    if len_aisle > 0:
        change.append(value)
        module_movement_figure.AISLE.clear()
    if value in list_beat_black_pawn or value in list_beat_white_pawn:
        module_movement_figure.AISLE = value
        change.append(value)
    return change

def check_pawn(figura, change, answer):
    '''проверка является ли фигура пешкой'''
    if figura == '\u265F' or figura == '\u2659':
        change = take_on_the_aisle(change, module_board.BOARD, answer) #взятие на проходе
    return change

def function_mat(change):
    '''функция шах королю'''
    white_king = define_coordinates_figura('\u2654', module_board.BOARD)
    black_king = define_coordinates_figura('\u265A', module_board.BOARD)
    print("166", white_king, black_king, change)
    if white_king in change:
        print("Мат белому королю.")
        module_movement_figure.MAT_KING = True
    if black_king in change:
        print("Мат черному королю.")
        module_movement_figure.MAT_KING = True

def new_coordinate(name_player, figura, change, coordinates_figure):
    '''новые кординаты фигуры'''
    answer = question_coordinates(name_player)  #новые координаты фигуры
    answer = letters_conversions(answer)  #преобразования букв в цифры
    if answer[0] not in LIST_NUMBERS and answer[1] not in LIST_NUMBERS:
        answer = new_coordinate(name_player, figura, change, coordinates_figure)
    change = check_pawn(figura, change, answer)
    print("180 возможные ходы фигуры", change)
    if answer in change:
        function_mat(change)
        module_board.BOARD[answer[0]][answer[1]] = figura
    elif answer not in change:
        print("Вы ввели координаты занятого места на доске.")
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
        if current_figura == '\u265F' or current_figura == '\u2659':
            if answer[0] != coordinates_figura[0] and answer[1] != coordinates_figura[1]:
                module_board.BOARD[last_figura[0]][last_figura[1]] = module_board.SPACE
    return moves

def movement_of_figures(name_player, coordinates_figura, change, moves):
    '''передвижение фигур'''  #coordinates_figura = координаты фигуры
    len_change = len(change)
    answer = []
    if len_change == 0:
        print("Нет возможных ходов для фигуры.")
    else:
        figura = module_board.BOARD[coordinates_figura[0]][coordinates_figura[1]]
        answer = new_coordinate(name_player, figura, change, coordinates_figura)
        moves = clear_after_aisle(moves, answer, figura, coordinates_figura)
        castling_figures(figura, change, answer, module_board.BOARD)  #рокировка
        try:
            module_board.BOARD[coordinates_figura[0]][coordinates_figura[1]] = module_board.SPACE
        except TypeError:  #операция применена к объекту несоответствующего типа
            print("None")
    return answer, moves

def define_coordinate(answer, player):
    '''вопрос игроку'''
    print(player, "выберите координаты фигуры?")
    answer_player = input()
    len_answer_player = len(answer_player)
    if len_answer_player == 0:
        answer = define_coordinate(answer, player)
    answer = letters_conversions(answer_player)
    answer = what_color_figura(player, answer)
    return answer

def stroke(player):  #ход
    '''будет ход или нет'''
    answer = []
    answer = define_coordinate(answer, player)
    if answer[0] != module_board.SPACE or answer[1] != module_board.SPACE:
        print("Вы ввели координаты пустого места на доске.")
        answer = define_coordinate(answer, player)
    else:
        print("Повторите ввод.")
        answer = define_coordinate(answer, player)
    return answer

def output_board():
    '''вывод фигур на экран'''
    for i in module_board.BOARD:
        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])

def add_in_rooks(coordinates_figure, board):
    '''список ходов каждой туры и/или короля'''
    name = module_movement_figure.name_definition(coordinates_figure, board)
    if "rook" in name:
        module_movement_figure.FIGURES_MOVE.append(coordinates_figure)
    elif "king" in name:
        module_movement_figure.FIGURES_MOVE.append(coordinates_figure)

def end_game(board):
    '''условие конца игры'''
    mat = False
    winner = ''
    list_board = []
    for i in board:
        for element in i:
            figura = board[board.index(i)][i.index(element)]
            list_board.append(figura)
    if '\u2654' not in list_board:  #белый король
        mat = True
        winner = 'black'
    elif '\u265A' not in list_board:  #черный король
        mat = True
        winner = 'white'
    return mat, winner

def one_player(name_player, moves, counter, game_continues):
    '''игровой процесс для одного игрока'''
    output_board()                             #вывод игровой доски на экран
    coordinates_figura = stroke(name_player)  #ход игрока, след. строка - определение фигуры
    change = module_movement_figure.figure_definition(coordinates_figura, module_board.BOARD)
    change = module_beat_figura.pawn_beat(coordinates_figura, module_board.BOARD, change)
    coordinata, moves = movement_of_figures(name_player, coordinates_figura, change, moves)
    add_in_rooks(coordinates_figura, module_board.BOARD)
    module_save_result.write_step(name_player, [coordinates_figura, coordinata])
    counter = counter + 1
    mat, winner = end_game(module_board.BOARD)
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
        module_save_result.write_time_game_began()
        if continues is True and module_movement_figure.MAT_KING is False:
            continues, counter, name_winner = one_player(player_white, moves, counter, continues)
        if continues is True and module_movement_figure.MAT_KING is False:
            continues, counter, name_winner = one_player(player_black, moves, counter, continues)
    module_save_result.write_game_result(module_board.BOARD, name_winner)
    print("Игра закончилась. Партию выиграл - ", name_winner)

if __name__ == "__main__":
    print("This is a module with game Chess.")
    input("\nPress the enter key to exit.")
