# -*- coding: utf-8 -*-
"""Created on Tue Nov 7 22:48:30 2017  @author: Egor """
#сумма координат чной клетки - чётная, а бой - нечётная.
GRID = [['\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1'],
        ['\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0'],
        ['\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1'],
        ['\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0'],
        ['\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1'],
        ['\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0'],
        ['\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1'],
        ['\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0', '\u25A1', '\u25A0']]
BLACK_SQUARE = '\u25A0'
WHITE_SQUARE = '\u25A1'
SPACE = '\u0020' #символ проба в юникоде
LIST_ALL_FIGURES = ['\u265F', '\u265C', '\u265E', '\u265D',
                    '\u265A', '\u265B', '\u2659', '\u2656',
                    '\u2658', '\u2657', '\u2654', '\u2655']
DICTIONARY = {'pawn_black': '\u265F', 'rook_black': '\u265C',
              'horse_black': '\u265E', 'elephant_black': '\u265D',
              'king_black': '\u265A', 'queen_black': '\u265B',
              'pawn_white': '\u2659', 'rook_white': '\u2656',
              'horse_white': '\u2658', 'elephant_white': '\u2657',
              'king_white': '\u2654', 'queen_white': '\u2655'}   #LINE_0 - буквы
LINE_0 = ['\u00AD', '\u0061', '\u0062', '\u0063', '\u0064', '\u0065', '\u0066', '\u0067', '\u0068']
LINE_1 = ['\u0038', DICTIONARY['rook_black'], DICTIONARY['horse_black'],
          DICTIONARY['elephant_black'], DICTIONARY['queen_black'],
          DICTIONARY['king_black'], DICTIONARY['elephant_black'],
          DICTIONARY['horse_black'], DICTIONARY['rook_black']]
LINE_2 = ['\u0037', DICTIONARY['pawn_black'], DICTIONARY['pawn_black'],
          DICTIONARY['pawn_black'], DICTIONARY['pawn_black'],
          DICTIONARY['pawn_black'], DICTIONARY['pawn_black'],
          DICTIONARY['pawn_black'], DICTIONARY['pawn_black']]
LINE_3 = ['\u0036', SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE]
LINE_4 = ['\u0035', SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE]
LINE_5 = ['\u0034', SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE]
LINE_6 = ['\u0033', SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE]
LINE_7 = ['\u0032', DICTIONARY['pawn_white'], DICTIONARY['pawn_white'],
          DICTIONARY['pawn_white'], DICTIONARY['pawn_white'],
          DICTIONARY['pawn_white'], DICTIONARY['pawn_white'],
          DICTIONARY['pawn_white'], DICTIONARY['pawn_white']]
LINE_8 = ['\u0031', DICTIONARY['rook_white'], DICTIONARY['horse_white'],
          DICTIONARY['elephant_white'], DICTIONARY['queen_white'],
          DICTIONARY['king_white'], DICTIONARY['elephant_white'],
          DICTIONARY['horse_white'], DICTIONARY['rook_white']]
BOARD = [LINE_0, LINE_1, LINE_2, LINE_3, LINE_4, LINE_5, LINE_6, LINE_7, LINE_8]

if __name__ == "__main__":
    print("This is a module with game Chess.")
    input("\nPress the enter key to exit.")
