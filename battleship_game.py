# -*- coding: utf-8 -*-
"""Created on Sun Feb 18 18:27:25 2018 @author: Egor"""
import sys

def create_board():
    '''создание доски'''
    board = [['  ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К'],
             [' 1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' 9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['10', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    return board

def output_board(board):
    '''вывод на экран игровой доски'''
    for i in board:
        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])

def exit_program(answer):
    '''выход из программы'''
    if answer == "выход":
        sys.exit()

def coordinate_transformation(coordinates):
    '''преобразование координат, введенных игроком'''
    value = []
    if coordinates[0] == 'а':
        value.append(1)
    elif coordinates[0] == 'б':
        value.append(2)
    elif coordinates[0] == 'в':
        value.append(3)
    elif coordinates[0] == 'г':
        value.append(4)
    elif coordinates[0] == 'д':
        value.append(5)
    elif coordinates[0] == 'е':
        value.append(6)
    elif coordinates[0] == 'ж':
        value.append(7)
    elif coordinates[0] == 'з':
        value.append(8)
    elif coordinates[0] == 'и':
        value.append(9)
    elif coordinates[0] == 'к':
        value.append(10)
    if len(coordinates) == 2:
        value.append(int(coordinates[1]))
    elif len(coordinates) == 3:
        value.append(10)
    value.reverse()  #чтобы координаты вводились правильно
    return value

def check_coordinates(coordinates):
    '''проверка координат'''
    value = False
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        if coordinates[0] in check and coordinates[1] in check:
            value = True
    except IndexError:
        value = False
    return value

def check_coordinate_ship(coordinates):
    '''проверка координат для создания корабля на доске'''
    value = True
    if len(coordinates) == 2:
        one = coordinates[0]
        two = coordinates[1]
        if one[0] != two[0] and one[1] != two[1]:
            value = False
    return value

def correction_coor(answer, player_board, name_player, name_ship, coordinate):
    '''корректирока координат'''
    coordinate.remove(answer)
    print(name_player, "введите координаты", name_ship, "корабля на доске?")
    answer = input()
    exit_program(answer)
    answer = coordinate_transformation(answer)
    check_coor = check_coordinates(answer)
    coordinate.append(answer)
    check = check_coordinate_ship(coordinate)
    if check is True:
        if check_coor is True:
            player_board[answer[0]][answer[1]] = '\u1F6A2' #Корабль
            output_board(player_board)
    else:
        player_board = correction_coor(answer, player_board, name_player, name_ship, coordinate)
    return player_board

def check_len_answer(coordinates):
    '''проверка длины ответа игрока'''
    len_coordinates = len(coordinates)
    variable = True
    value = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']
    if len_coordinates != 2:
        variable = False
    if len_coordinates == 3 and '10' in coordinates and coordinates[-3] in value:
        variable = True
    return variable

def check_ship_on_board(board, x_pos, y_pos, continue_moves):
    '''чтобы не выходить за пределы массива'''
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if x_pos in value and y_pos in value:
        if board[x_pos][y_pos] == '\u26F5':
            continue_moves = False
        else:
            continue_moves = True
    else:
        continue_moves = False#True
    return continue_moves

def scan(board, x_pos, y_pos, moves):
    '''сканирование'''
    if x_pos and y_pos in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        moves = check_ship_on_board(board, x_pos - 1, y_pos - 1, moves)
        moves = check_ship_on_board(board, x_pos - 1, y_pos, moves)
        moves = check_ship_on_board(board, x_pos - 1, y_pos + 1, moves)
        moves = check_ship_on_board(board, x_pos, y_pos + 1, moves)
        moves = check_ship_on_board(board, x_pos + 1, y_pos + 1, moves)
        moves = check_ship_on_board(board, x_pos + 1, y_pos, moves)
        moves = check_ship_on_board(board, x_pos + 1, y_pos - 1, moves)
        moves = check_ship_on_board(board, x_pos, y_pos - 1, moves)
    else:
        moves = False
    if y_pos == 1 and x_pos in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: #заплата при расположении корабля
        moves = check_ship_on_board(board, x_pos, y_pos, moves) #в вертикали "а"
    print("137", moves)
    return moves

def scan_board(board, coordinates_ship, direction, ship_type):  #корабль рядом
    '''если рядом с указанными координатами другой корабль'''
    continue_moves = True
    x_pos = int(coordinates_ship[0])
    y_pos = int(coordinates_ship[1])
    if direction == 1:  #1 - вверх
        while ship_type > 0:
            continue_moves = scan(board, x_pos, y_pos, continue_moves)
            x_pos = x_pos - 1
            ship_type = ship_type - 1
    elif direction == 2:  #2 - вправо
        while ship_type > 0:
            continue_moves = scan(board, x_pos, y_pos, continue_moves)
            x_pos = x_pos + 1
            ship_type = ship_type - 1
    elif direction == 3:  #3 - вниз
        while ship_type > 0:
            continue_moves = scan(board, x_pos, y_pos, continue_moves)
            y_pos = y_pos + 1
            ship_type = ship_type - 1
    elif direction == 4:  #4 - влево
        while ship_type > 0:
            continue_moves = scan(board, x_pos, y_pos, continue_moves)
            x_pos = x_pos - 1
            ship_type = ship_type - 1
    return continue_moves

def asked_player(board, name_player, name_ship):
    '''вопрос игроку - где расположить корабль'''
    print(name_player, "введите координаты", name_ship, "корабля на доске?")
    answer = input()
    exit_program(answer)
    value = check_len_answer(answer)
    print(name_player, "введите направление", name_ship, "корабля")
    print("1 - вверх, 2 - вправо, 3 - вниз, 4 - влево")
    direction = input()
    exit_program(direction)
    try:
        direction = int(direction)
    except ValueError:
        direction = input()
        exit_program(answer)
        direction = int(direction)
    if direction not in [1, 2, 3, 4]:
        answer, direction = asked_player(board, name_player, name_ship)
    if value is False:
        answer, direction = asked_player(board, name_player, name_ship)
    return answer, direction

def add_ship(board, ship_type, direction, answer):
    '''добавление корабля на доску'''
    while ship_type > 0:
        ship_type = ship_type - 1
        if direction == 1:   #вверх
            board[answer[0] - ship_type][answer[1]] = '\u26F5'
        elif direction == 2: #вправо
            board[answer[0]][answer[1] + ship_type] = '\u26F5'
        elif direction == 3: #вниз
            board[answer[0] + ship_type][answer[1]] = '\u26F5'
        elif direction == 4: #влево
            board[answer[0]][answer[1] - ship_type] = '\u26F5'
    return board

def new_ship(board, name_player, ship_type, name_ship):
    '''Новый корабль на доске'''
    list_coordinate = []
    answer, direction = asked_player(board, name_player, name_ship)
    answer = coordinate_transformation(answer)
    check_coor = check_coordinates(answer)
    continue_moves = scan_board(board, answer, direction, ship_type)
    if continue_moves is False:
        print("Нельзя расположить корабль в этом месте.")
        answer.clear()
        board = new_ship(board, name_player, ship_type, name_ship)
    else:
        check = check_coordinate_ship(list_coordinate)
        len_answer = len(answer)
        if check_coor is True and check is True and len_answer > 0:
            board[answer[0]][answer[1]] = '\u26F5'  #Корабль
            board = add_ship(board, ship_type, direction, answer)
            output_board(board)
        else:
            board = new_ship(board, name_player, ship_type, name_ship)
        list_coordinate.append(answer)
    return board

def add_ships(player_board, name):
    '''создание кораблей на игровой доске игрока'''
    player_board = new_ship(player_board, name, 4, 'четырехместного')
    player_board = new_ship(player_board, name, 3, 'трехместного')
    player_board = new_ship(player_board, name, 3, 'трехместного')
    player_board = new_ship(player_board, name, 2, 'двухместного')
    player_board = new_ship(player_board, name, 2, 'двухместного')
    player_board = new_ship(player_board, name, 2, 'двухместного')
    player_board = new_ship(player_board, name, 1, 'одноместного')
    player_board = new_ship(player_board, name, 1, 'одноместного')
    player_board = new_ship(player_board, name, 1, 'одноместного')
    player_board = new_ship(player_board, name, 1, 'одноместного')
    return player_board

def damaged_ship(player_board, name_player, enemy_board):
    '''подбитый корабль'''
    output_board(enemy_board)
    print(name_player, "введите координаты места, куда хотите ударить.")
    coordinates = input()
    exit_program(coordinates)
    coordinates = coordinate_transformation(coordinates)
    check_coor = check_coordinates(coordinates)
    add_move = False #если попал, еще дается ход
    if player_board[coordinates[0]][coordinates[1]] == '\u1F6A2' and check_coor is True: #Корабль
        player_board[coordinates[0]][coordinates[1]] = '\u274C'#обзначение крестика попал в корабль
        enemy_board[coordinates[0]][coordinates[1]] = '\u274C' #попал в корабль
        output_board(enemy_board)
        add_move = True
    else:
        player_board[coordinates[0]][coordinates[1]] = '\u25AA'#обозначает черный маленькмй квадрат
        enemy_board[coordinates[0]][coordinates[1]] = '\u25AA'  #промазал   Точка U+002E
        output_board(enemy_board)
    return player_board, enemy_board, add_move

def info_player():#board):
    '''информация о игроке '''
    board = create_board()
    print("Введите свое имя?")
    name = input()
    exit_program(name)
    output_board(board)
    player_board = add_ships(board, name)
    return player_board, name  #board = player_enemy

def define_winner(board_1, board_2, name1, name2):
    '''определение победителя и конец игры'''
    game_continue = False
    winner_1 = False
    winner_2 = False
    for line in board_1:
        for i in line:
            if i == '\u1F6A2':
                game_continue = True
                winner_1 = True
    for line in board_2:
        for i in line:
            if i == '\u1F6A2':
                game_continue = True
                winner_2 = True
    if winner_1 is True:
        print("Игрок", name2, "проиграл.")
        print("Игрок", name1, "победил.")
    elif winner_2 is True:
        print("Игрок", name1, "проиграл.")
        print("Игрок", name2, "победил.")
    return game_continue

def check_board(player_board, name):
    '''првоерка игрового поля после игры'''
    print(name, "хотите посмотреть игровое поле соперника?")
    answer = input()
    exit_program(answer)
    variable = False
    if answer == 'y':
        output_board(player_board)
        print("Есть нарушения правил на игровом поле?")
        answer = input()
        exit_program(answer)
        if answer == 'y':
            print("Победа присваивается игроку ", name)
            variable = True
    return variable

def game_began():
    '''начало игры'''
    player_board_1, name1 = info_player() #
    player_board_2, name2 = info_player() #
    enemy_board1 = create_board()
    enemy_board2 = create_board()
    game_continue = True
    while game_continue:
        move = True
        while move:  #1 игрок
            player_board_1, enemy_board1, move = damaged_ship(player_board_2, name1, enemy_board2)
        move = True
        while move:  #2 игрок
            player_board_2, enemy_board2, move = damaged_ship(player_board_1, name2, enemy_board1)
        game_continue = define_winner(player_board_1, player_board_2, name1, name2)
        variable_1 = check_board(player_board_2, name1)
        variable_2 = check_board(player_board_1, name2)
        if variable_1 is True and variable_2 is True:
            print("Из-за нарушений в игре не может быть определен победитель.")

game_began()
input()
