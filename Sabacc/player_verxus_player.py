# -*- coding: utf-8 -*-
"""
Игра Сабакк
"""
import random
try:
    from colorama import init, Fore#библиотека используется для вывода цветного текста в терминал
except ImportError:
    pass

import module_functions

try:
    init()#инициализация библиотеки colorama
except Exception:
    pass

CARDS = ["1 Монеты", "2 Монеты", "3 Монеты", "4 Монеты", "5 Монеты", "6 Монеты",
         "7 Монеты", "8 Монеты", "9 Монеты", "10 Монеты", "11 Монеты",
         "12 Командир Монеты", "13 Госпожа Монеты", "14 Мастер Монеты", "15 Туз Монеты",
         "1 Мечи", "2 Мечи", "3 Мечи", "4 Мечи", "5 Мечи", "6 Мечи", "7 Мечи",
         "8 Мечи", "9 Мечи", "10 Мечи", "11 Мечи", "12 Командир Мечи", "13 Госпожа Мечи",
         "14 Мастер Мечи", "15 Туз Мечи",
         "1 Фляги", "2 Фляги", "3 Фляги", "4 Фляги", "5 Фляги", "6 Фляги", "7 Фляги",
         "8 Фляги", "9 Фляги", "10 Фляги", "11 Фляги", "12 Командир Фляги",
         "13 Госпожа Фляги", "14 Мастер Фляги", "15 Туз Фляги",
         "1 Шесты", "2 Шесты", "3 Шесты", "4 Шесты", "5 Шесты", "6 Шесты", "7 Шесты",
         "8 Шесты", "9 Шесты", "10 Шесты", "11 Шесты", "12 Командир Шесты",
         "13 Госпожа Шесты", "14 Мастер Шесты", "15 Туз Шесты",
         "-2 Королева Воздуха и Тьмы", "-8 Выносливость", "-11 Баланс", "-13 Гибель",
         "-14 Выдержка", "-15 Коварный", "-17 Звезда", "0 Идиот",
         "-2 Королева Воздуха и Тьмы", "-8 Выносливость", "-11 Баланс", "-13 Гибель",
         "-14 Выдержка", "-15 Коварный", "-17 Звезда", "0 Идиот"]

class Player(object):
    """Один игрок"""
    TOTAL = 0 #всего создано экземпляров класса Player
    NAME = ""
    PLAYER_LIST = []
    BANKROLL = 0
    LIST_INTERFERENCE = []
    AMOUNT_OF_PLAYER_CARDS = 0#сумма карт игрока
    def __init__(self, name, bankroll, player_list, list_interference):
        '''создание одного игрока'''
        self.name = name
        self.bankroll = bankroll
        self.player_list = player_list
        self.list_interference = list_interference
        Player.TOTAL = Player.TOTAL + 1
    def function_list(self):
        '''функция превращает все параметры игрока в список'''
        rep = [self.name, self.bankroll, self.player_list, self.list_interference]
        return rep

def delete_card(card):
    '''удалениет карты из общего списка'''
    CARDS.remove(card)

def add_card(card):
    '''возврашение карты в список'''
    CARDS.append(card)

def new_card(card):
    '''если у нескольких претендентов на победу одинаковые значения карт'''
    value = card.function_list()
    name = value[0]
    player_list = value[2]
    if name and player_list is not None:     #нужно выдать новую карту
        shufflingcards = random.choice(CARDS)#для определения победителя
        print("Игрок", name, "получил новую карту", shufflingcards)
        delete_card(shufflingcards)
        player_list.append(shufflingcards)#значение карты + результат игрока
        print("Результат игрока", name, "=", player_list)
        return player_list, card

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

LIST_PLAYERS_RATE = [] #список ставок игроков в раунде
POSITIVE_ANSWER, NEGATIVE_ANSWER, INTERFERENCE = read_regulations_with_file()

def field_interference(card):
    '''поле помех'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    list_interference = []
    if value[3] is not None:
        list_interference = value[3]
    print(name, "вы хотите поместить карты в поле помех?")
    choice = module_functions.repeat_choice_str()#игрок не хотел изменять карту, он мог "заморозить"
    if choice == POSITIVE_ANSWER:# её значение поместив карту в поле помех в ходе раунда
        i = len(player_list)
        while i > 0:
            print(name, "выберите карту.")
            choice_card_field_interference = module_functions.repeat_choice_str()
            if choice_card_field_interference in player_list:
                if choice_card_field_interference not in list_interference:
                    list_interference.append(choice_card_field_interference)
                    amount = card.AMOUNT_OF_PLAYER_CARDS
                    card = Player(name, bankroll, player_list, list_interference)
                    card.AMOUNT_OF_PLAYER_CARDS = amount
                    print("Карта", choice_card_field_interference, "помещена в поле помех")
                else:
                    count_card = list_interference.count(choice_card_field_interference)
                    qwerty = player_list.count(choice_card_field_interference)
                    if count_card < qwerty:
                        list_interference.append(choice_card_field_interference)
                        amount = card.AMOUNT_OF_PLAYER_CARDS
                        card = Player(name, bankroll, player_list, list_interference)
                        card.AMOUNT_OF_PLAYER_CARDS = amount
                        print("Карта", choice_card_field_interference, "помещена в поле помех")
                    else:
                        print("Карта уже находиться в списке.")
            else:
                print("Вы ввели ошибочные значения карт.")
            i = i - 1
    elif choice == NEGATIVE_ANSWER:
        print("Не забывайте ваши карты могут измениться в любую минуту.")
    return card

def function_player_list():
    '''функция для формирования списка игрока'''
    list_player = []                     #объявление списка игрока
    score = random.choice(CARDS)         #выбор случайного элемента списка CARDS
    shufflingcards = random.choice(CARDS)#и присваивание его переменной score
    delete_card(shufflingcards)
    delete_card(score)
    list_player.append(score)            #добавление элемента score в список игрока
    list_player.append(shufflingcards)   #нужно добавить 2 случайных элемента в список
    return list_player                   #возвращение списка

def identification_of_player_data(num):#определение данных игроков
    '''определить данные игроков'''
    card1 = None
    card2 = None
    card3 = None
    card4 = None
    card5 = None
    card6 = None
    card7 = None
    card8 = None
    for i in range(num): #определение имени игроков и суммы денег на которые они будут играть
        if i == 0:
            list_player = function_player_list()#module_functions.player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card1 = Player(name_player, bankroll_player, list_player, None)
        if i == 1:
            list_player = function_player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card2 = Player(name_player, bankroll_player, list_player, None)
        if i == 2:
            list_player = function_player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card3 = Player(name_player, bankroll_player, list_player, None)
        if i == 3:
            list_player = function_player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card4 = Player(name_player, bankroll_player, list_player, None)
        if i == 4:
            list_player = function_player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card5 = Player(name_player, bankroll_player, list_player, None)
        if i == 5:
            list_player = function_player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card6 = Player(name_player, bankroll_player, list_player, None)
        if i == 6:
            list_player = function_player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card7 = Player(name_player, bankroll_player, list_player, None)
        if i == 7:
            list_player = function_player_list()
            name_player = module_functions.player_name()
            bankroll_player = module_functions.player_bankroll()
            card8 = Player(name_player, bankroll_player, list_player, None)
    return card1, card2, card3, card4, card5, card6, card7, card8

def jummer(card_value):
    '''jummer - изменение карт игрока'''
    value = card_value.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    list_interference = []
    if value[3] is not None:
        list_interference = value[3]
    list_jummer = [] #новый список
    for i in player_list:
        if i in list_interference:
            list_jummer.append(i)
            list_interference.remove(i)
        else:
            shufflingcard_0 = random.choice(CARDS)
            list_jummer.append(shufflingcard_0)
            delete_card(shufflingcard_0)
    print("Список карт игрока", name, "после изменения ", list_jummer)
    card_value = Player(name, bankroll, list_jummer, list_interference)
    return card_value

def change_player_card(card):
    '''фактор случайности - изменяться ли карты у игрока'''
    if card is not None:
        card1 = jummer(card)
    return card1

def change_players_cards(card1, card2, card3, card4, card5, card6, card7, card8):
    '''изменение карт у игроков'''
    print("Произошло изменение карт.")
    if card1 is not None:
        card1 = change_player_card(card1)
    if card2 is not None:
        card2 = change_player_card(card2)
    if card3 is not None:
        card3 = change_player_card(card3)
    if card4 is not None:
        card4 = change_player_card(card4)
    if card5 is not None:
        card5 = change_player_card(card5)
    if card6 is not None:
        card6 = change_player_card(card6)
    if card7 is not None:
        card7 = change_player_card(card7)
    if card8 is not None:
        card8 = change_player_card(card8)
    return card1, card2, card3, card4, card5, card6, card7, card8

def bet_size(card, rate):#размер ставки
    '''размер ставки, которую может сделать игрок'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    print(name, "введите сумму ставки?")
    choice = module_functions.repeat_choice_int()
    if choice > 0:#чтобы игроки не делали "нулевых" ставок
        if bankroll >= choice:
            print(name, "сделал ставку", choice)
            LIST_PLAYERS_RATE.append(choice)
            rate = rate + choice
            bankroll = bankroll - choice
        else:
            print("У вас недостаточно средств для такой ставки. Сделайте меньшую ставку.")
            if bankroll > 0:
                bankroll, rate, card = bet_size(card, rate)
            else:
                print(name, "не имеет денег для продолжения и покидает игру.")
                name = None
                bankroll = None
                player_list = None
                list_interference = None
                card = Player(name, bankroll, player_list, list_interference)
    else:
        print("Вы не можете сделать нулевую ставку.")
        bankroll, rate, card = bet_size(card, rate)#функция вызывает сама себя
    card = Player(value[0], bankroll, value[2], value[3])
    return bankroll, rate, card

def bet_size_in_betting_odds(card, difference, rate):#размер ставки,
    '''размер ставки, которую может сделать игрок'''#если игроки сделали разные ставки
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    list_interference = []
    if value[3] is not None:
        list_interference = value[3]
    if name is not None and difference != 0:#проверка на присутствие игрока в игре
        print(name, "сделаете ставку", difference, "?")#и не делать лишнего действия
        choice = module_functions.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            if bankroll >= difference:#rate >= 0:
                print(name, "сделал ставку", difference)
                bankroll = bankroll - difference
                rate = rate + difference
            else:
                print("Вы не можете сделать ставку и покидаете игру.")
                del card
                name = None
                bankroll = None
                player_list = None
                list_interference = None
        elif choice == NEGATIVE_ANSWER:
            print(name, "не сделал ставку и вышел из игры.")
            del card
            name = None
            bankroll = None
            player_list = None
            list_interference = None
        elif choice == INTERFERENCE:
            card = field_interference(card)
            card, difference = player_done_rate(card, difference)
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(name, bankroll, player_list, list_interference)
        card.AMOUNT_OF_PLAYER_CARDS = amount
    return card, rate

def player_done_rate(card, rate):
    '''игроки делают ставки'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    list_interference = []
    if value[3] is not None:
        list_interference = value[3]
    print(name, "будете делать ставку")
    choice = module_functions.repeat_choice_str()
    if choice == POSITIVE_ANSWER:
        bankroll, rate, card = bet_size(card, rate)
        card_check = card.function_list()
        if card_check[1] is None:
            card = Player(None, None, None, None)
        else:
            amount = card.AMOUNT_OF_PLAYER_CARDS
            card = Player(name, bankroll, player_list, list_interference)
            card.AMOUNT_OF_PLAYER_CARDS = amount
    elif choice == NEGATIVE_ANSWER:
        if len(LIST_PLAYERS_RATE) > 0:#чтобы избежать ситуации, когда первый игрок не делает ставку
            max_valua = max(LIST_PLAYERS_RATE)#и игра вылетает
            if max_valua == 0:
                print(name, "не сделал ставку.")
                LIST_PLAYERS_RATE.append(0)
            else:
                print(name, "не сделал ставку и вышел из игры.")
                card = Player(None, None, None, None)
                LIST_PLAYERS_RATE.append(0)#для того чтобы не сбивались номера в списке ставок
        else:
            print(name, "не сделал ставку.")
            LIST_PLAYERS_RATE.append(0)
    elif choice == INTERFERENCE:
        card = field_interference(card)
        card, rate = player_done_rate(card, rate)
    else:
        print("Вы ввели неверное значение")
    amount = card.AMOUNT_OF_PLAYER_CARDS
    card.AMOUNT_OF_PLAYER_CARDS = amount
    return card, rate

def players_rate(card1, card2, card3, card4, card5, card6, card7, card8, rate):
    '''игроки по очереди делают ставки'''
    if card1 is not None:
        card1, rate = player_done_rate(card1, rate)
    if card2 is not None:
        card2, rate = player_done_rate(card2, rate)
    if card3 is not None:
        card3, rate = player_done_rate(card3, rate)
    if card4 is not None:
        card4, rate = player_done_rate(card4, rate)
    if card5 is not None:
        card5, rate = player_done_rate(card5, rate)
    if card6 is not None:
        card6, rate = player_done_rate(card6, rate)
    if card7 is not None:
        card7, rate = player_done_rate(card7, rate)
    if card8 is not None:
        card8, rate = player_done_rate(card8, rate)
    return card1, card2, card3, card4, card5, card6, card7, card8, rate

def betting_odds(card1, card2, card3, card4, card5, card6, card7, card8, rate):
    '''если игроки сделали разные ставки'''#разница ставок игроков
    min_value = 0
    max_value = 0
    if len(LIST_PLAYERS_RATE) > 0:
        max_value = max(LIST_PLAYERS_RATE)
        min_value = min(LIST_PLAYERS_RATE)
    if min_value != max_value:
        if card1 is not None:
            difference = max_value - LIST_PLAYERS_RATE[0]#difference - разница
            card1, rate = bet_size_in_betting_odds(card1, difference, rate)
        if card2 is not None:
            difference = max_value - LIST_PLAYERS_RATE[1]
            card2, rate = bet_size_in_betting_odds(card2, difference, rate)
        if card3 is not None:
            difference = max_value - LIST_PLAYERS_RATE[2]
            card3, rate = bet_size_in_betting_odds(card3, difference, rate)
        if card4 is not None:
            difference = max_value - LIST_PLAYERS_RATE[3]
            card4, rate = bet_size_in_betting_odds(card4, difference, rate)
        if card5 is not None:
            difference = max_value - LIST_PLAYERS_RATE[4]
            card5, rate = bet_size_in_betting_odds(card5, difference, rate)
        if card6 is not None:
            difference = max_value - LIST_PLAYERS_RATE[5]
            card6, rate = bet_size_in_betting_odds(card6, difference, rate)
        if card7 is not None:
            difference = max_value - LIST_PLAYERS_RATE[6]
            card7, rate = bet_size_in_betting_odds(card7, difference, rate)
        if card8 is not None:
            difference = max_value - LIST_PLAYERS_RATE[7]
            card8, rate = bet_size_in_betting_odds(card8, difference, rate)
    return card1, card2, card3, card4, card5, card6, card7, card8, rate

def stage_change_players(card1, card2, card3, card4, card5, card6, card7, card8):
    '''игроки 1-4 по очереди делают ставки'''
    if card1 is not None:
        card1 = stage_change(card1)
    if card2 is not None:
        card2 = stage_change(card2)
    if card3 is not None:
        card3 = stage_change(card3)
    if card4 is not None:
        card4 = stage_change(card4)
    if card5 is not None:
        card5 = stage_change(card5)
    if card6 is not None:
        card6 = stage_change(card6)
    if card7 is not None:
        card7 = stage_change(card7)
    if card8 is not None:
        card8 = stage_change(card8)
    return card1, card2, card3, card4, card5, card6, card7, card8

def stage_change(card):
    '''стадия изменение'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    list_interference = []
    if value[3] is not None:
        list_interference = value[3]
    amount = card.AMOUNT_OF_PLAYER_CARDS
    card = Player(name, bankroll, player_list, list_interference)
    card.AMOUNT_OF_PLAYER_CARDS = amount
    if name is not None:
        print(name, "хотите изменить какую-либо карту из своей колоды")
        choice = module_functions.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            print(name, "выберите какую карту хотите изменить?")
            card_player = module_functions.repeat_choice_str()
            if card_player in player_list:
                player_list.remove(card_player)
                new_card_0 = random.choice(CARDS)
                player_list.append(new_card_0)
                add_card(card_player)
            else:
                print("Такой карты нет в списке")
        elif choice == NEGATIVE_ANSWER:
            print(name, "отказался от изменения колоды.")
        elif choice == INTERFERENCE:
            card = field_interference(card)
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(name, bankroll, player_list, list_interference)
        card.AMOUNT_OF_PLAYER_CARDS = amount
    return card

def open_list_stage(name, list_player):
    '''функция для подсчета суммы карт, выводит результат игрока'''
    card_amount = 0#сумма карт
    list_result = []
    if list_player is not None:
        for line in list_player:
            result = line.split()
            list_result.append(result[0])
        for i in list_result:
            try:
                i = int(i)
                card_amount = card_amount + i
            except ValueError:
                pass
        print("Сумма карт игрока", name, "=", card_amount)
    return card_amount

def stage_opening_cards(card):
    '''стадия открытие карт'''
    value = card.function_list()
    name = value[0]
    player_list = value[2]
    answer = False#игрок открыл карты или нет
    if name is not None:# and len(game_result) == 0:
        print(name, "будете открывать карты?")
        choice = module_functions.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            if name and player_list is not None:
                answer = True
        elif choice == NEGATIVE_ANSWER:
            print(name, "не стал раскрывать карты")
        elif choice == INTERFERENCE:
            card = field_interference(card)
    return answer

def player_open_cards(card, game_results):
    '''игрок открывает свои карты'''
    value = card.function_list()#name
    if value[0] is not None:
        print("Игрок ", value[0], " открылся.")#player_list
        print("Карты игрока ", value[2])
        card_amount = open_list_stage(value[0], value[2])
        if card_amount < 24 and card_amount > -24:
            card.AMOUNT_OF_PLAYER_CARDS = card_amount
            game_results.append(card_amount)#добавление результата игрока в список
        else:
            game_results.append(-10000)#если напишу None, for не сможет перебрать список
    return game_results, card

def stage_opening_players_1(card1, card2, card3, card4, card5):
    '''игроки 1-5 по очереди открывают карты'''
    game_results = []
    if card1 is not None:
        answer = stage_opening_cards(card1)
    if card2 is not None and answer is False:
        answer = stage_opening_cards(card2)
    if card3 is not None and answer is False:
        answer = stage_opening_cards(card3)
    if card4 is not None and answer is False:
        answer = stage_opening_cards(card4)
    if card5 is not None and answer is False:
        answer = stage_opening_cards(card5)
    if answer is True:
        if card1 is not None:
            game_results, card1 = player_open_cards(card1, game_results)
        if card2 is not None:
            game_results, card2 = player_open_cards(card2, game_results)
        if card3 is not None:
            game_results, card3 = player_open_cards(card3, game_results)
        if card4 is not None:
            game_results, card4 = player_open_cards(card4, game_results)
        if card5 is not None:
            game_results, card5 = player_open_cards(card5, game_results)
    return answer, game_results

def stage_opening_players_2(card6, card7, card8, answer, game_results):
    '''игроки 6-8 по очереди открывают карты'''
    if card6 is not None and answer is False:
        answer = stage_opening_cards(card6)
    if card7 is not None and answer is False:
        answer = stage_opening_cards(card7)
    if card8 is not None and answer is False:
        answer = stage_opening_cards(card8)
    if answer is True:
        if card6 is not None:
            game_results, card6 = player_open_cards(card6, game_results)
        if card7 is not None:
            game_results, card7 = player_open_cards(card7, game_results)
        if card8 is not None:
            game_results, card8 = player_open_cards(card8, game_results)
    return answer, game_results

def phase_change_cycle(card):
    '''стадия получение'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    len_player_list = len(player_list)
    list_interference = []
    if value[3] is not None:
        list_interference = value[3]
    if name is not None and len_player_list < 5:
        print("Игрок", name, "вам нужна новая карта?")
        choice = module_functions.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            shufflingcard = random.choice(CARDS)
            player_list.append(shufflingcard)
            delete_card(shufflingcard)
        elif choice == NEGATIVE_ANSWER:
            print("Вы отказались от карты.\n")
        elif choice == INTERFERENCE:
            print("Помещение карт в поле помех.")
            if len(player_list) is None:# != 0:#вызов функции в функции
                card = field_interference(card)
            choice_2 = module_functions.repeat_choice_str()#если игрок помещал карты в поле помех
            if choice_2 == POSITIVE_ANSWER:#необходимо чтобы он изменил или не изменил колоду карт
                shufflingcard = random.choice(CARDS)
                player_list.append(shufflingcard)
                delete_card(shufflingcard)
            elif choice == NEGATIVE_ANSWER:
                print("Вы отказались от карты.\n", player_list)
            else:
                print("Вы нажали неверную кнопку.")
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(name, bankroll, player_list, list_interference)
        card.AMOUNT_OF_PLAYER_CARDS = amount
    if len_player_list == 5:
        print("У игрока уже есть 5 карт.")
    return card

def stage_new_cards_players(card1, card2, card3, card4, card5, card6, card7, card8):
    '''стадия получение карт для игроков'''
    if card1 is not None:
        card1 = phase_change_cycle(card1)
    if card2 is not None:
        card2 = phase_change_cycle(card2)
    if card3 is not None:
        card3 = phase_change_cycle(card3)
    if card4 is not None:
        card4 = phase_change_cycle(card4)
    if card5 is not None:
        card5 = phase_change_cycle(card5)
    if card6 is not None:
        card6 = phase_change_cycle(card6)
    if card7 is not None:
        card7 = phase_change_cycle(card7)
    if card8 is not None:
        card8 = phase_change_cycle(card8)
    return card1, card2, card3, card4, card5, card6, card7, card8

def no_winners(gain):
    '''если победителей в игре нет'''
    print("Победителей нет, банк переходит в следующую игру.")
    module_functions.write_rate_in_file(gain)

def duplicate_card_one(rate, max_value, card1, card2, card3, card4, card5, card6, card7, card8):
    '''если победитель один'''
    if card1 is not None and max_value == card1.AMOUNT_OF_PLAYER_CARDS:
        value = card1.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    elif card2 is not None and max_value == card2.AMOUNT_OF_PLAYER_CARDS:# и его результата в файл
        value = card2.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    elif card3 is not None and max_value == card3.AMOUNT_OF_PLAYER_CARDS:
        value = card3.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    elif card4 is not None and max_value == card4.AMOUNT_OF_PLAYER_CARDS:
        value = card4.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    elif card5 is not None and max_value == card5.AMOUNT_OF_PLAYER_CARDS:
        value = card5.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    elif card6 is not None and max_value == card6.AMOUNT_OF_PLAYER_CARDS:
        value = card6.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    elif card7 is not None and max_value == card7.AMOUNT_OF_PLAYER_CARDS:
        value = card7.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    elif card8 is not None and max_value == card8.AMOUNT_OF_PLAYER_CARDS:
        value = card8.function_list()
        name = value[0]
        print("Победил игрок", name, ", его выигрыш =", rate)
        module_functions.write_in_file(name, rate)
    else:
        no_winners(rate)

def several_winners_number(card, gain, max_card):
    '''один игрок'''
    value = card.function_list()
    if value[0] is not None:
        if max_card == card.AMOUNT_OF_PLAYER_CARDS:
            print("Победил игрок", value[0], ", его выигрыш =", gain)#запись имени победителя
            module_functions.write_in_file(value[0], gain)#и его результата в файл

def several_winners(max_card, gain, card1, card2, card3, card4, card5, card6, card7, card8):
    '''несколько победителей'''
    if card1 is not None:
        several_winners_number(card1, gain, max_card)
    if card2 is not None:
        several_winners_number(card2, gain, max_card)
    if card3 is not None:
        several_winners_number(card3, gain, max_card)
    if card4 is not None:
        several_winners_number(card4, gain, max_card)
    if card5 is not None:
        several_winners_number(card5, gain, max_card)
    if card6 is not None:
        several_winners_number(card6, gain, max_card)
    if card7 is not None:
        several_winners_number(card7, gain, max_card)
    if card8 is not None:
        several_winners_number(card8, gain, max_card)

def list_game_results_players(game_results, card):
    '''выдача 1 новой карты каждому игроку с одинаково наибольшими результатам'''
    if card is not None:
        list_player, card = new_card(card)
        value = card.function_list()
        list_player = value[2]
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(value[0], value[1], list_player, value[3])
        card.AMOUNT_OF_PLAYER_CARDS = amount
        result = open_list_stage(value[0], list_player)
        card.AMOUNT_OF_PLAYER_CARDS = result
        game_results.append(result)
    return game_results, card

def duplicate_cards(rate, game_results, card1, card2, card3, card4, card5, card6, card7, card8):
    '''предполагаемых победителей несколько'''
    print("Несколько игроков претендуют на победу.")
    gain = 0.0#для получения дробного выражения
    game_results_players = []
    game_results.clear()
    game_results_players, card1 = list_game_results_players(game_results, card1)
    game_results_players, card2 = list_game_results_players(game_results, card2)
    game_results_players, card3 = list_game_results_players(game_results, card3)
    game_results_players, card4 = list_game_results_players(game_results, card4)
    game_results_players, card5 = list_game_results_players(game_results, card5)
    game_results_players, card6 = list_game_results_players(game_results, card6)
    game_results_players, card7 = list_game_results_players(game_results, card7)
    game_results_players, card8 = list_game_results_players(game_results, card8)
    victory = module_functions.function_victory(game_results_players)
    max_card = max(game_results_players, key=abs)#key=abs абсолютное значение
    if victory == 0:
        no_winners(rate)
    else:
        print("Победителей ", victory)
        gain = rate / victory#расчитывется выигрыш каждого игрока
        several_winners(max_card, gain, card1, card2, card3, card4, card5, card6, card7, card8)

def def_win(rate, game_results, card1, card2, card3, card4, card5, card6, card7, card8):
    '''определение победителя'''
    game_results = module_functions.function_list_game_results(game_results)
    max_value = max(game_results, key=abs)#key=abs абсолютное значение
    minus_max_value = -max_value
    if minus_max_value in game_results:
        duplicate_cards(rate, game_results, card1, card2, card3, card4, card5, card6, card7, card8)
    duplicate_max_card = game_results.count(max_value)#узнаем сколько раз значение встречатеся
    if duplicate_max_card == 1:
        duplicate_card_one(rate, max_value, card1, card2, card3, card4, card5, card6, card7, card8)
    elif duplicate_max_card > 1:
        duplicate_cards(rate, game_results, card1, card2, card3, card4, card5, card6, card7, card8)
    elif duplicate_max_card == 0:
        no_winners(rate)

def def_check(card, name, number):
    '''проверка - есть ли игрок в игре или нет'''
    if card is not None:
        value = card.function_list()
        if value[0] is not None:
            value = card.function_list()
            if value[0] is not None:
                number = number + 1
                name = value[0]
    return name, number

def check_presence_game(rate, card1, card2, card3, card4, card5, card6, card7, card8):
    '''проверка игроков после раунда ставок в игре'''
    number = 0
    name = 0
    name, number = def_check(card1, name, number)
    name, number = def_check(card2, name, number)
    name, number = def_check(card3, name, number)
    name, number = def_check(card4, name, number)
    name, number = def_check(card5, name, number)
    name, number = def_check(card6, name, number)
    name, number = def_check(card7, name, number)
    name, number = def_check(card8, name, number)
    if number == 0:
        no_winners(rate)
    elif number == 1:
        print("Игрок", name, "выиграл банк", rate)
        module_functions.write_in_file(name, rate)

def game():
    '''начало игры, перед раундами'''
    rate = 0
    rate = module_functions.rate_with_last_games()
    try:
        print(Fore.GREEN + "Начинаем игру в сабакк!")
    except Exception:
        print("Начинаем игру в сабакк!")
    num = module_functions.ask()
    card1, card2, card3, card4, card5, card6, card7, card8 = identification_of_player_data(num)
    return card1, card2, card3, card4, card5, card6, card7, card8, rate

def output_of_game_results_1(card1, card2, card3, card4, card5):
    '''выводит на экран результаты игроков 1-5'''
    if card1 is not None:
        name = card1.function_list()
        print("Результаты игрока", name[0], name[2])
    if card2 is not None:
        name = card2.function_list()
        print("Результаты игрока", name[0], name[2])
    if card3 is not None:
        name = card3.function_list()
        print("Результаты игрока", name[0], name[2])
    if card4 is not None:
        name = card4.function_list()
        print("Результаты игрока", name[0], name[2])
    if card5 is not None:
        name = card5.function_list()
        print("Результаты игрока", name[0], name[2])

def output_of_game_results_2(card6, card7, card8):
    '''выводит на экран результаты игроков 6-8'''
    if card6 is not None:
        name = card6.function_list()
        print("Результаты игрока", name[0], name[2])
    if card7 is not None:
        name = card7.function_list()
        print("Результаты игрока", name[0], name[2])
    if card8 is not None:
        name = card8.function_list()
        print("Результаты игрока", name[0], name[2])

def round_first(number_rounds):#, card1, card2, card3, card4, card5, card6, card7, card8, rate):
    '''1 раунд игры - стадия торг'''#change_players_cards - генератор помех
    print("Раунд", number_rounds, "\nСтадия Торг")#игроки по очереди делают ставки

def round_first_1(card1, card2, card3, card4, card5, card6, card7, card8, rate):
    '''1 раунд игры - стадия торг'''
    card1, card2, card3, card4, card5, card6, card7, card8, rate = players_rate(card1, card2, card3, card4, card5, card6, card7, card8, rate)
    card1, card2, card3, card4, card5, card6, card7, card8, rate = betting_odds(card1, card2, card3, card4, card5, card6, card7, card8, rate)
    return card1, card2, card3, card4, card5, card6, card7, card8, rate

def round_second(card1, card2, card3, card4, card5, card6, card7, card8):
    '''2 раунд - изменение карт игроков, в зависимости от броска кубика'''
    print("Стадия Изменение.")#"бросание кубик" и определяет
    likely_to_change_card_deck = module_functions.block()#смогут ли игроки изменить свои карты
    if likely_to_change_card_deck < 4:#цикл для изменения колоды карт, функция block это кубик
        print("На шестигранном кубике выпало:", likely_to_change_card_deck)
        print("Изменения карт не будет")
    else:
        print("На шестигранном кубике выпало:", likely_to_change_card_deck)
        card1, card2, card3, card4, card5, card6, card7, card8 = stage_change_players(card1, card2, card3, card4, card5, card6, card7, card8)
    return card1, card2, card3, card4, card5, card6, card7, card8

def round_fourth(card1, card2, card3, card4, card5, card6, card7, card8):
    '''стадия получения карт'''
    print("Стадия Получение.")
    card1, card2, card3, card4, card5, card6, card7, card8 = stage_new_cards_players(card1, card2, card3, card4, card5, card6, card7, card8)
    return card1, card2, card3, card4, card5, card6, card7, card8

def function_jummer(card1, card2, card3, card4, card5, card6, card7, card8):
    '''функция вызывающая изменение карт у всех игроков'''
    block = module_functions.block()#функция, определяющяя будет изменение карт или нет
    if block == 1:
        card1, card2, card3, card4, card5, card6, card7, card8 = change_players_cards(card1, card2, card3, card4, card5, card6, card7, card8)
    return card1, card2, card3, card4, card5, card6, card7, card8

def game_pvp():
    '''основная часть'''
    variable_game = True
    number_rounds = 1
    card1, card2, card3, card4, card5, card6, card7, card8, rate = game()
    output_of_game_results_1(card1, card2, card3, card4, card5)
    output_of_game_results_2(card6, card7, card8)
    while variable_game:
        LIST_PLAYERS_RATE.clear()#очищение списка ставок в начале каждой игры
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        round_first(number_rounds)
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        card1, card2, card3, card4, card5, card6, card7, card8, rate = round_first_1(card1, card2, card3, card4, card5, card6, card7, card8, rate)
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        check_presence_game(rate, card1, card2, card3, card4, card5, card6, card7, card8)
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        card1, card2, card3, card4, card5, card6, card7, card8 = round_second(card1, card2, card3, card4, card5, card6, card7, card8)
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        if number_rounds >= 4:
            card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
            print("Стадия Открытие карт.")#opening stage по английски
            answer, game_result = stage_opening_players_1(card1, card2, card3, card4, card5)
            answer, game_result = stage_opening_players_2(card6, card7, card8, answer, game_result)
            if answer is True:#значит игроки открылись
                def_win(rate, game_result, card1, card2, card3, card4, card5, card6, card7, card8)
                variable_game = False
                break
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        card1, card2, card3, card4, card5, card6, card7, card8 = round_fourth(card1, card2, card3, card4, card5, card6, card7, card8)
        card1, card2, card3, card4, card5, card6, card7, card8 = function_jummer(card1, card2, card3, card4, card5, card6, card7, card8)
        print("Конец раунда", number_rounds)
        number_rounds = number_rounds + 1
        LIST_PLAYERS_RATE.clear()#очищение списка ставок в конце каждого раунда

if __name__ == "__main__":
    print("This is a module with game Sabacc.")
    input("\n\nPress the enter key to exit.")
