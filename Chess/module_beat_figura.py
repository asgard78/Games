# -*- coding: utf-8 -*-
"""Created on Wed Nov 15 20:39:02 2017 @author: Egor"""
SPACE = '\u0020' #символ пробела в юникоде
KEY = {'\u265F': 'pawn_black', '\u265C': 'rook_black',
       '\u265E': 'horse_black', '\u265D': 'elephant_black',
       '\u265A': 'king_black', '\u265B': 'queen_black',
       '\u2659': 'pawn_white', '\u2656': 'rook_white',
       '\u2658': 'horse_white', '\u2657': 'elephant_white',
       '\u2654': 'king_white', '\u2655': 'queen_white'}
LIST_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]
KING_BLACK_MOVE = False
KING_WHITE_MOVE = False

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
    color = "color"
    if 'white' in name:
        color = 'white'
    elif 'black' in name:
        color = 'black'
    return color

def add_list(lst, colour, colour_1, change, board):
    '''добавление 2 параметров в список'''
    if board[lst[0]][lst[1]] != SPACE and colour != colour_1:
        if lst[0] in LIST_NUMBERS and lst[1] in LIST_NUMBERS:
            change.append(lst)
    return change

def pawn_beat_1(coordinata_pawn, change, board):
    '''возможность бить пешкой'''
    colour = color_definition(coordinata_pawn, board)
    if colour == 'white' and coordinata_pawn[0] < 8 and coordinata_pawn[1] < 7:
        x_pos = coordinata_pawn[0] - 1
        y_pos = coordinata_pawn[1] + 1
        colour_1 = color_definition([x_pos, y_pos], board)
        change = add_list([x_pos, y_pos], colour, colour_1, change, board)
        x_pos = coordinata_pawn[0] + 1
        y_pos = coordinata_pawn[1] + 1
        colour_1 = color_definition([x_pos, y_pos], board)
        change = add_list([x_pos, y_pos], colour, colour_1, change, board)
    elif colour == 'black' and coordinata_pawn[0] < 8 and coordinata_pawn[1] < 7:
        x_pos = coordinata_pawn[0] + 1
        y_pos = coordinata_pawn[1] + 1
        colour_1 = color_definition([x_pos, y_pos], board)
        change = add_list([x_pos, y_pos], colour, colour_1, change, board)
        x_pos = coordinata_pawn[0] - 1
        y_pos = coordinata_pawn[1] + 1
        colour_1 = color_definition([x_pos, y_pos], board)
        change = add_list([x_pos, y_pos], colour, colour_1, change, board)
    return change

def pawn_beat_2(change, board):
    '''возможность бить пешкой'''
    len_change = len(change)
    if len_change > 0:
        for i in change:
            colour = color_definition(i, board)
            if colour == 'white' and i[0] < 7 and i[1] < 8:
                x_pos = i[0] - 1
                y_pos = i[1] + 1
                colour_1 = color_definition([x_pos, y_pos], board)
                change = add_list([x_pos, y_pos], colour, colour_1, change, board)
                x_pos = i[0] + 1
                y_pos = i[1] + 1
                colour_1 = color_definition([x_pos, y_pos], board)
                change = add_list([x_pos, y_pos], colour, colour_1, change, board)
            elif colour == 'black' and i[0] > 2 and i[1] > 2:
                x_pos = i[0] - 1
                y_pos = i[1] - 1
                colour_1 = color_definition([x_pos, y_pos], board)
                change = add_list([x_pos, y_pos], colour, colour_1, change, board)
                x_pos = i[0] - 1
                y_pos = i[1] - 1
                colour_1 = color_definition([x_pos, y_pos], board)
                change = add_list([x_pos, y_pos], colour, colour_1, change, board)
    return change

def pawn_beat(coordinates_figura, board, change):
    '''взятие фигуры пешкой'''
    change = pawn_beat_1(coordinates_figura, change, board)
    change = pawn_beat_2(change, board)
    return change                     #добавляются в список для ходов

def beat_black_pawn(board, change):
    '''список мест для удара черными пешками'''
    coordinates_figura = []
    for i in board:
        for element in i:
            if element == '\u265F':
                coordinates_figura = [board.index(i), i.index(element)]
                change = pawn_beat(coordinates_figura, board, change)
    return change

def beat_white_pawn(board, change):
    '''список мест для удара белыми пешками'''
    coordinates_figura = []
    for i in board:
        for element in i:
            if element == '\u2659':
                coordinates_figura = [board.index(i), i.index(element)]
                change = pawn_beat(coordinates_figura, board, change)
    return change

if __name__ == "__main__":
    print("This is a module with game Chess.")
    input("\nPress the enter key to exit.")
