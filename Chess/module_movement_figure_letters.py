# -*- coding: utf-8 -*-
"""Created on Wed Nov  1 01:38:23 2017 @author: Egor """
SPACE = '      ' #символ пробела в юникоде
KEY = {' П(ч) ': 'pawn_black', ' Т(ч) ': 'rook_black',
       ' К(ч) ': 'horse_black', ' С(ч) ': 'elephant_black',
       'Кор(ч)': 'king_black', ' Ф(ч) ': 'queen_black',
       ' П(б) ': 'pawn_white', ' Т(б) ': 'rook_white',
       ' К(б) ': 'horse_white', ' С(б) ': 'elephant_white',
       'Кор(б)': 'king_white', ' Ф(б) ': 'queen_white'}
LIST_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]
SHAH = False  #шах не объявлен (False) или объявлен (True)
FIGURES_MOVE = []
CASTLING_WHITE_DONE = False
CASTLING_BLACK_DONE = False
AISLE = []
MAT_KING = False #мат

def name_definition(coordinates_figura, board):
    '''определение имени фигуры'''
    name_figura = 'i'
    for i in KEY:
        if i == board[coordinates_figura[0]][coordinates_figura[1]]:
            name_figura = KEY[i]
    return name_figura

def color_definition(coordinates_figura, board):
    '''определение цвета фигуры'''
    name = name_definition(coordinates_figura, board)
    colour = 'colour'
    if 'white' in name:
        colour = 'white'
    elif 'black' in name:
        colour = 'black'
    return colour

def position_figure(coordinata, board):
    '''проверка на наличие фигуры на клетке'''
    value = False
    if board[coordinata[0]][coordinata[1]] == SPACE:
        value = True
    return value

def add_list(x_pos, y_pos, change, board):
    '''добавление элементов в список'''
    if board[x_pos][y_pos] == SPACE:
        change.append([x_pos, y_pos])
    return change

def pawn(coordinates_figura, board):
    '''пешка'''
    change = []
    name_figura = name_definition(coordinates_figura, board)
    if 'black' in name_figura:
        if coordinates_figura[0] == 2:
            position = coordinates_figura[0] + 1
            change = add_list(position, coordinates_figura[1], change, board)
            position = coordinates_figura[0] + 2
            change = add_list(position, coordinates_figura[1], change, board)
        else:
            position = coordinates_figura[0] + 1
            change.append([position, coordinates_figura[1]])
    elif 'white' in name_figura:
        if coordinates_figura[0] == 7:
            position = coordinates_figura[0] - 1
            change = add_list(position, coordinates_figura[1], change, board)
            position = coordinates_figura[0] - 2
            change = add_list(position, coordinates_figura[1], change, board)
        else:
            position = coordinates_figura[0] - 1
            change = add_list(position, coordinates_figura[1], change, board)
    return change

def change_figura(list_rook, colour_rook, board, change):
    '''добавление в список фигур, которых фигура побьет'''
    colour = color_definition(list_rook, board)
    if colour_rook != colour:
        change.append([list_rook[0], list_rook[1]])
    return change

def rook(coordinates_figura, board):
    '''тура'''
    change = []
    colour_rook = color_definition(coordinates_figura, board)
    position_1 = coordinates_figura[0]
    while position_1 < 8:
        position_1 = position_1 + 1
        if board[position_1][coordinates_figura[1]] != SPACE:
            change = change_figura([position_1, coordinates_figura[1]], colour_rook, board, change)
            break
        else:
            new_list = [position_1, coordinates_figura[1]]
            change.append(new_list)
    position_2 = coordinates_figura[1]
    while position_2 < 8:
        position_2 = position_2 + 1
        if board[coordinates_figura[0]][position_2] != SPACE:
            change = change_figura([coordinates_figura[0], position_2], colour_rook, board, change)
            break
        else:
            new_list = [coordinates_figura[0], position_2]
            change.append(new_list)
    position_3 = coordinates_figura[0]
    while position_3 > 1:
        position_3 = position_3 - 1
        if board[position_3][coordinates_figura[1]] != SPACE:
            change = change_figura([position_3, coordinates_figura[1]], colour_rook, board, change)
            break
        else:
            change.append([position_3, coordinates_figura[1]])
    position_4 = coordinates_figura[1]
    while position_4 > 1:
        position_4 = position_4 - 1
        if board[coordinates_figura[0]][position_4] != SPACE:
            change = change_figura([coordinates_figura[0], position_4], colour_rook, board, change)
            break
        else:
            change.append([coordinates_figura[0], position_4])
    return change

def x_y_decrease(coordinata_figura, change, board, colour_rook):
    '''уменьшение у и x'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos > 1 and y_pos > 1:
        x_pos = x_pos - 1
        y_pos = y_pos - 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def x_y_enlargement(coordinata_figura, change, board, colour_rook):
    '''уменьшение у и x'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos < 8 and y_pos < 8:
        x_pos = x_pos + 1
        y_pos = y_pos + 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def x_enlargement_y_decrease(coordinata_figura, change, board, colour_rook):
    '''уменьшение у и увеличение x'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos < 8 and y_pos > 1:
        x_pos = x_pos + 1
        y_pos = y_pos - 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def y_enlargement_x_decrease(coordinata_figura, change, board, colour_rook):
    '''уменьшение x и увеличение y'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos > 1 and y_pos < 8:
        x_pos = x_pos - 1
        y_pos = y_pos + 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def elephant(coordinata_figura, board):
    '''офицер'''
    change = []
    colour_rook = color_definition(coordinata_figura, board)
    change = x_y_decrease(coordinata_figura, change, board, colour_rook)
    change = x_y_enlargement(coordinata_figura, change, board, colour_rook)
    change = x_enlargement_y_decrease(coordinata_figura, change, board, colour_rook)
    change = y_enlargement_x_decrease(coordinata_figura, change, board, colour_rook)
    return change

def move_horse_1(coordinata_figura, change, board, position, colour_rook):
    '''движение коня'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    x_pos = x_pos + position[0]
    y_pos = y_pos - position[1]
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def move_horse_2(coordinata_figura, change, board, position, colour_rook):
    '''движение коня'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    x_pos = x_pos - position[0]
    y_pos = y_pos - position[1]
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def move_horse_3(coordinata_figura, change, board, position, colour_rook):
    '''движение коня'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    x_pos = x_pos - position[1]
    y_pos = y_pos + position[0]
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def move_horse_4(coordinata_figura, change, board, position, colour_rook):
    '''движение коня'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    x_pos = x_pos + position[0]
    y_pos = y_pos + position[1]
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def horse(coordinata_figura, board):
    '''конь'''
    change = []
    colour_rook = color_definition(coordinata_figura, board)
    change = move_horse_1(coordinata_figura, change, board, [1, 2], colour_rook)
    change = move_horse_2(coordinata_figura, change, board, [1, 2], colour_rook)
    change = move_horse_3(coordinata_figura, change, board, [2, 1], colour_rook)
    change = move_horse_4(coordinata_figura, change, board, [2, 1], colour_rook)
    change = move_horse_1(coordinata_figura, change, board, [2, 1], colour_rook)
    change = move_horse_2(coordinata_figura, change, board, [2, 1], colour_rook)
    change = move_horse_3(coordinata_figura, change, board, [1, 2], colour_rook)
    change = move_horse_4(coordinata_figura, change, board, [1, 2], colour_rook)
    return change

def move_king_1(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0] + 1
    y_pos = coordinata_figura[1] + 1
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def move_king_2(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0] + 1
    if x_pos in LIST_NUMBERS and coordinata_figura[1] in LIST_NUMBERS:
        if board[x_pos][coordinata_figura[1]] == SPACE:
            change.append([x_pos, coordinata_figura[1]])
        else:
            change = change_figura([x_pos, coordinata_figura[1]], colour_rook, board, change)
    return change

def move_king_3(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0] + 1
    y_pos = coordinata_figura[1] - 1
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def move_king_4(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    y_pos = coordinata_figura[1] - 1
    if coordinata_figura[0] in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[coordinata_figura[0]][y_pos] == SPACE:
            change.append([coordinata_figura[0], y_pos])
        else:
            change = change_figura([coordinata_figura[0], y_pos], colour_rook, board, change)
    return change

def move_king_5(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0] - 1
    y_pos = coordinata_figura[1] - 1
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def move_king_6(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0] - 1
    if x_pos in LIST_NUMBERS and coordinata_figura[1] in LIST_NUMBERS:
        if board[x_pos][coordinata_figura[1]] == SPACE:
            change.append([x_pos, coordinata_figura[1]])
        else:
            change = change_figura([x_pos, coordinata_figura[1]], colour_rook, board, change)
    return change

def move_king_7(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0] - 1
    y_pos = coordinata_figura[1] + 1
    if x_pos in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
    return change

def move_king_8(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    y_pos = coordinata_figura[1] + 1
    if coordinata_figura[0] in LIST_NUMBERS and y_pos in LIST_NUMBERS:
        if board[coordinata_figura[0]][y_pos] == SPACE:
            change.append([coordinata_figura[0], y_pos])
        else:
            change = change_figura([coordinata_figura[0], y_pos], colour_rook, board, change)
    return change

def coordinates_for_castling(coordinata_king, change, board, colour_king):
    '''координаты для рокировки'''
    y_pos = coordinata_king[1] - 2
    if y_pos in LIST_NUMBERS:
        if board[coordinata_king[0]][y_pos] == SPACE:
            change.append([coordinata_king[0], y_pos])
        else:
            change = change_figura([coordinata_king[0], y_pos], colour_king, board, change)
    y_pos = coordinata_king[1] + 2
    if y_pos in LIST_NUMBERS:# and coordinata_king[1] in LIST_NUMBERS:
        if board[coordinata_king[0]][y_pos] == SPACE:
            change.append([coordinata_king[0], y_pos])
        else:
            change = change_figura([coordinata_king[0], y_pos], colour_king, board, change)
    return change

def castling(coordinata_king, change, board, colour):
    '''рокировка'''
    if colour == 'white' and CASTLING_WHITE_DONE is False and coordinata_king not in FIGURES_MOVE:
        change = coordinates_for_castling(coordinata_king, change, board, colour)
    if colour == 'black' and CASTLING_BLACK_DONE is False and coordinata_king not in FIGURES_MOVE:
        change = coordinates_for_castling(coordinata_king, change, board, colour)
    return change

def king(coordinata_figura, board):
    '''король'''
    change = []
    colour_rook = color_definition(coordinata_figura, board)
    change = move_king_1(coordinata_figura, change, board, colour_rook)
    change = move_king_2(coordinata_figura, change, board, colour_rook)
    change = move_king_3(coordinata_figura, change, board, colour_rook)
    change = move_king_4(coordinata_figura, change, board, colour_rook)
    change = move_king_5(coordinata_figura, change, board, colour_rook)
    change = move_king_6(coordinata_figura, change, board, colour_rook)
    change = move_king_7(coordinata_figura, change, board, colour_rook)
    change = move_king_8(coordinata_figura, change, board, colour_rook)
    change = castling(coordinata_figura, change, board, colour_rook)
    return change

def move_queen_1(coordinata_figura, change, board, colour_rook):
    '''ход королевы'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos < 8 and y_pos < 8:
        x_pos = x_pos + 1
        y_pos = y_pos + 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def move_queen_2(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0]
    while x_pos < 8:
        x_pos = x_pos + 1
        if board[x_pos][coordinata_figura[1]] == SPACE:
            change.append([x_pos, coordinata_figura[1]])
        else:
            change = change_figura([x_pos, coordinata_figura[1]], colour_rook, board, change)
            break
    return change

def move_queen_3(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos < 8 and y_pos > 1:
        x_pos = x_pos + 1
        y_pos = y_pos - 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def move_queen_4(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    y_pos = coordinata_figura[1]
    while y_pos > 1:
        y_pos = y_pos - 1
        if board[coordinata_figura[0]][y_pos] == SPACE:
            change.append([coordinata_figura[0], y_pos])
        else:
            change = change_figura([coordinata_figura[0], y_pos], colour_rook, board, change)
            break
    return change

def move_queen_5(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos > 1 and y_pos > 1:
        x_pos = x_pos - 1
        y_pos = y_pos - 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def move_queen_6(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0]
    while x_pos > 1:
        x_pos = x_pos - 1
        if board[x_pos][coordinata_figura[1]] == SPACE:
            change.append([x_pos, coordinata_figura[1]])
        else:
            change = change_figura([x_pos, coordinata_figura[1]], colour_rook, board, change)
            break
    return change

def move_queen_7(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    x_pos = coordinata_figura[0]
    y_pos = coordinata_figura[1]
    while x_pos > 1 and y_pos < 8:
        x_pos = x_pos - 1
        y_pos = y_pos + 1
        if board[x_pos][y_pos] == SPACE:
            change.append([x_pos, y_pos])
        else:
            change = change_figura([x_pos, y_pos], colour_rook, board, change)
            break
    return change

def move_queen_8(coordinata_figura, change, board, colour_rook):
    '''ход короля'''
    y_pos = coordinata_figura[1]
    while y_pos < 8:
        y_pos = y_pos + 1
        if board[coordinata_figura[0]][y_pos] == SPACE:
            change.append([coordinata_figura[0], y_pos])
        else:
            change = change_figura([coordinata_figura[0], y_pos], colour_rook, board, change)
            break
    return change

def queen(coordinata_figura, board):
    '''королева (ферзь)'''
    change = []
    colour_rook = color_definition(coordinata_figura, board)
    change = move_queen_1(coordinata_figura, change, board, colour_rook)
    change = move_queen_1(coordinata_figura, change, board, colour_rook)
    change = move_queen_2(coordinata_figura, change, board, colour_rook)
    change = move_queen_3(coordinata_figura, change, board, colour_rook)
    change = move_queen_4(coordinata_figura, change, board, colour_rook)
    change = move_queen_5(coordinata_figura, change, board, colour_rook)
    change = move_queen_6(coordinata_figura, change, board, colour_rook)
    change = move_queen_7(coordinata_figura, change, board, colour_rook)
    change = move_queen_8(coordinata_figura, change, board, colour_rook)
    return change

def figure_definition(coordinata_figura, board):
    '''определение фигуры'''
    figura = board[coordinata_figura[0]][coordinata_figura[1]]
    name = '1'
    change = []
    for i in KEY:
        if i == figura:
            name = KEY[i]
    if 'pawn' in name:
        change = pawn(coordinata_figura, board)
    elif 'rook' in name:
        change = rook(coordinata_figura, board)
    elif 'horse' in name:
        change = horse(coordinata_figura, board)
    elif 'elephant' in name:
        change = elephant(coordinata_figura, board)
    elif 'king' in name:
        change = king(coordinata_figura, board)
    elif 'queen' in name:
        change = queen(coordinata_figura, board)
    else:
        print("516")
    return change

if __name__ == "__main__":
    print("This is a module with game Chess.")
    input("\nPress the enter key to exit.")
