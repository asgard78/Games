# -*- coding: utf-8 -*-
"""
Игрок против компьютера
"""
import random
try:
    from colorama import init, Fore#библиотека используется для вывода цветного текста в терминал
except  ImportError:
    pass

import player_verxus_computer as player_vs_computer
import player_verxus_player
import module_functions
import module_main
import module_regulations

try:
    init()#инициализация библиотеки colorama
except Exception:
    pass

LIST_PLAYERS_RATE = [] #список ставок игроков в раунде  player_verxus_player
POSITIVE_ANSWER, NEGATIVE_ANSWER, INTERFERENCE = module_regulations.read_regulations_with_file()

class Player(object):
    """Один игрок"""
    TOTAL = 0 #всего создано экземпляров класса Player
    NAME = ""
    PLAYER_LIST = []
    BANKROLL = 0
    LIST_INTERFERENCE = []
    AMOUNT_OF_PLAYER_CARDS = 0#сумма карт игрока
    def __init__(self, name, bankroll, player_list, list_interference, computer_or_human):
        '''создание одного игрока'''
        self.name = name
        self.bankroll = bankroll
        self.player_list = player_list
        self.list_interference = list_interference
        self.computer = computer_or_human
        Player.TOTAL = Player.TOTAL + 1
    def function_list(self):
        '''функция превращает все параметры игрока в список'''
        rep = [self.name, self.bankroll, self.player_list, self.list_interference, self.computer]
        return rep

def computer_name():
    '''выбор произвольного имени для компьютера'''
    #'''если нажата клавиша Enter при пустой строке ввода'''
    bukva = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',
             'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
             'x', 'c', 'v', 'b', 'n', 'm', 'p', 'z']

    truth = True
    number = 0
    name = ""
    while truth:
        random_bukva = random.choice(bukva)
        name = name + random_bukva
        number = number + 1
        if number > 5:
            truth = False
    return name

def computer_bankroll():
    '''деньги на которые компьютер будет играть'''
    bankroll = random.randint(10, 100)
    print("59 computer_bankroll", bankroll)
    return bankroll

def igentification_gamer():
    '''идентификация игрока'''
    list_player = player_verxus_player.function_player_list()#данные для игрока
    name_player = module_functions.player_name()
    bankroll_player = module_functions.player_bankroll()
    card_player = Player(name_player, bankroll_player, list_player, None, False)
    list_player = player_verxus_player.function_player_list()#данные для компьютера
    name_player = computer_name()
    bankroll_player = computer_bankroll()
    card_computer = Player(name_player, bankroll_player, list_player, None, True)
    return card_player, card_computer

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
            shufflingcard_0 = random.choice(player_verxus_player.CARDS)
            list_jummer.append(shufflingcard_0)
    print("Список карт игрока", name, "после изменения ", list_jummer)
    card_value = Player(name, bankroll, list_jummer, list_interference, value[4])
    return card_value

def change_player_card(card):
    '''фактор случайности - изменяться ли карты у игрока'''
    if card is not None:
        card = jummer(card)
    return card

def change_players_cards(card_player, card_computer):
    '''изменение карт у игроков'''
    print("Произошло изменение карт.")
    if card_player is not None:
        card_player = change_player_card(card_player)
    if card_computer is not None:
        card_computer = change_player_card(card_computer)
    return card_player, card_computer

def function_jummer(card_player, card_computer):
    '''функция вызывающая изменение карт у всех игроков'''
    block = module_functions.block()#функция, определяющяя будет изменение карт или нет
    if block == 1:
        card_player, card_computer = change_players_cards(card_player, card_computer)
    return card_player, card_computer

def game():
    '''начало игры, перед раундами'''
    rate = 0
    rate = module_functions.rate_with_last_games()
    print("Начинаем игру в сабакк!")
    card_player, card_computer = igentification_gamer()
    return card_player, card_computer, rate

def output_of_game_results(card_player, card_computer):
    '''выводит на экран результаты игроков 1-5'''
    if card_player is not None:
        name = card_player.function_list()
        print("Результаты игрока", name[0], name[2])
    if card_computer is not None:
        name = card_computer.function_list()
        print("Результаты игрока", name[0], name[2])

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
                card = Player(name, bankroll, player_list, list_interference, value[4])
    else:
        print("Вы не можете сделать нулевую ставку.")
        bankroll, rate, card = bet_size(card, rate)#функция вызывает сама себя
    card = Player(value[0], bankroll, value[2], value[3], value[4])
    return bankroll, rate, card

def bet_size_computer(card, rate):#размер ставки
    '''размер ставки, которую может сделать игрок'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    computer = value[4]
    if bankroll > 0:#чтобы игроки не делали "нулевых" ставок
        choice = random.randint(1, 3)
        if bankroll >= choice:
            print(name, "сделал ставку", choice)
            LIST_PLAYERS_RATE.append(choice)
            rate = rate + choice
            bankroll = bankroll - choice
        else:
            if bankroll > 0:
                bankroll, rate, card = bet_size_computer(card, rate)
            else:
                print(name, "не имеет денег для продолжения и покидает игру.")
                name = None
                bankroll = None
                player_list = None
                list_interference = None
                card = Player(name, bankroll, player_list, list_interference, computer)
    else:
        print(name, "может сделать нулевую ставку.")
        bankroll, rate, card = bet_size(card, rate)#функция вызывает сама себя
    card = Player(value[0], bankroll, value[2], value[3], value[4])
    return bankroll, rate, card

def player_done_rate(card, rate):
    '''игроки делают ставки'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    if value[4] is True:
        bankroll, rate, card = bet_size_computer(card, rate)
    else:
        print(name, "будете делать ставку")
        choice = module_functions.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            bankroll, rate, card = bet_size(card, rate)
            card_check = card.function_list()
            if card_check[1] is None:
                card = Player(None, None, None, None, None)
            else:
                amount = card.AMOUNT_OF_PLAYER_CARDS
                card = Player(name, bankroll, value[2], value[3], value[4])
                card.AMOUNT_OF_PLAYER_CARDS = amount
        elif choice == NEGATIVE_ANSWER:
            if len(LIST_PLAYERS_RATE) > 0:#чтобы избежать ситуации, когда 1 игрок не делает ставку
                max_valua = max(LIST_PLAYERS_RATE)#и игра вылетает
                if max_valua == 0:
                    print(name, "не сделал ставку.")
                    LIST_PLAYERS_RATE.append(0)
                else:
                    print(name, "не сделал ставку и вышел из игры.")
                    del card
                    name = None
                    bankroll = None
                    value[3] = None
                    card = Player(name, bankroll, None, value[3], value[4])
                    LIST_PLAYERS_RATE.append(0)#для того чтобы не сбивались номера в списке ставок
            else:
                print(name, "не сделал ставку.")
                LIST_PLAYERS_RATE.append(0)
        elif choice == INTERFERENCE:
            card = player_verxus_player.field_interference(card)
            card, rate = player_done_rate(card, rate)
        else:
            print("Вы ввели неверное значение")
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card.AMOUNT_OF_PLAYER_CARDS = amount
    return card, rate

def check_presence_game(rate, card1, card2):
    '''проверка игроков после раунда ставок в игре'''
    number = 0
    name = 0
    name, number = player_verxus_player.def_check(card1, name, number)
    name, number = player_verxus_player.def_check(card2, name, number)
    if number == 0:
        player_verxus_player.no_winners(rate)
        module_main.endgame()
    elif number == 1:
        print("Игрок", name, "выиграл банк", rate)
        module_functions.write_in_file(name, rate)
        module_main.endgame()

def players_rate(card1, card2, rate):
    '''игроки по очереди делают ставки'''
    if card1 is not None:
        card1, rate = player_done_rate(card1, rate)
    if card2 is not None:
        card2, rate = player_done_rate(card2, rate)
    return card1, card2, rate

def bet_size_in_betting_odds(card, difference, rate):#размер ставки,
    '''размер ставки, которую может сделать игрок'''#если игроки сделали разные ставки
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    if name is not None and difference != 0 and value[4] is False:#есть игрока в игре или нет
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
                value[3] = None
        elif choice == NEGATIVE_ANSWER:
            print(name, "не сделал ставку и вышел из игры.")
            del card
            name = None
            bankroll = None
            player_list = None
            value[3] = None
        elif choice == INTERFERENCE:
            card = player_verxus_player.field_interference(card)
            card, difference = player_done_rate(card, difference)
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(name, bankroll, player_list, value[3], value[4])
        card.AMOUNT_OF_PLAYER_CARDS = amount
    elif name is not None and difference != 0 and value[4] is True:
        if bankroll >= difference:#rate >= 0:
            print(name, "сделал ставку", difference)
            bankroll = bankroll - difference
            rate = rate + difference
        else:
            print(name, "не сделал ставку и вышел из игры.")
            del card
            card = Player(None, None, None, None, None)
    return card, rate

def betting_odds(card1, card2, rate):
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
    return card1, card2, rate

def stage_change(card):
    '''стадия изменение'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    amount = card.AMOUNT_OF_PLAYER_CARDS
    card = Player(name, bankroll, player_list, value[3], value[4])
    card.AMOUNT_OF_PLAYER_CARDS = amount
    if name is not None and value[4] is False:
        print(name, "хотите изменить какую-либо карту из своей колоды")
        choice = module_functions.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            print(name, "выберите какую карту хотите изменить?")
            card_player = module_functions.repeat_choice_str()
            if card_player in player_list:
                player_list.remove(card_player)
                new_card_0 = random.choice(player_verxus_player.CARDS)
                player_list.append(new_card_0)
            else:
                print("Такой карты нет в списке")
        elif choice == NEGATIVE_ANSWER:
            print(name, "отказался от изменения колоды.")
        elif choice == INTERFERENCE:
            card = player_verxus_player.field_interference(card)
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(name, bankroll, player_list, value[3], value[4])
        card.AMOUNT_OF_PLAYER_CARDS = amount
    elif name is not None and value[4] is True:
        amount = card.AMOUNT_OF_PLAYER_CARDS
        if amount in [-23, 23]:#!= 23 or amount != -23:#вставить подсчет результата игрока человека
            card_player = random.choice(player_list)#случайно выбираю, какую карту нужно изменить
            print("354", player_list)#и менять карту по одной если у компьютера меньше
            player_list.remove(card_player)
            new_card_0 = random.choice(player_verxus_player.CARDS)
            player_list.append(new_card_0)
    return card

def stage_change_players(card_player, card_computer):
    '''игроки по очереди делают ставки'''
    if card_player is not None:
        card_player = stage_change(card_player)
    if card_computer is not None:
        card_computer = stage_change(card_computer)
    return card_player, card_computer

def player_open_cards(card, game_results):
    '''игрок открывает свои карты'''
    value = card.function_list()#name
    if value[0] is not None:
        print("Игрок ", value[0], " открылся.")#player_list
        print("Карты игрока ", value[2])
        card_amount = player_verxus_player.open_list_stage(value[0], value[2])
        if card_amount < 24 and card_amount > -24:
            card.AMOUNT_OF_PLAYER_CARDS = card_amount
            game_results.append(card_amount)#добавление результата игрока в список
        else:
            game_results.append(-10000)#если напишу None, for не сможет перебрать список
    return game_results, card

def opening_players(card_player, card_computer, answer, game_results):
    '''игроки по очереди открывают карты'''
    if card_player is not None and answer is False:
        answer = player_verxus_player.stage_opening_cards(card_player)
    if card_computer is not None and answer is False:
        answer = player_verxus_player.stage_opening_cards(card_computer)
    if answer is True:
        if card_player is not None:
            game_results, card_player = player_open_cards(card_player, game_results)
        if card_computer is not None:
            game_results, card_computer = player_open_cards(card_computer, game_results)
    return answer, game_results

def list_game_results_players(game_results, card):
    '''выдача 1 новой карты каждому игроку с одинаково наибольшими результатам'''
    if card is not None:
        list_player, card = player_vs_computer.new_card(card)#module_functions
        value = card.function_list()
        list_player = value[2]
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(value[0], value[1], list_player, value[3], value[4])
        card.AMOUNT_OF_PLAYER_CARDS = amount
        result = player_verxus_player.open_list_stage(value[0], list_player)
        card.AMOUNT_OF_PLAYER_CARDS = result
        game_results.append(result)
    return game_results, card

def several_winners(max_card, gain, card1, card2):
    '''несколько победителей'''
    if card1 is not None:
        player_verxus_player.several_winners_number(card1, gain, max_card)
    if card2 is not None:
        player_verxus_player.several_winners_number(card2, gain, max_card)
    module_main.endgame()

def duplicate_cards(rate, game_results, card1, card2):
    '''предполагаемых победителей несколько'''
    print("Несколько игроков претендуют на победу.")
    gain = 0.0#для получения дробного выражения
    game_results_players = []
    game_results.clear()
    game_results_players, card1 = list_game_results_players(game_results, card1)
    game_results_players, card2 = list_game_results_players(game_results, card2)
    victory = module_functions.function_victory(game_results_players)
    max_card = max(game_results_players, key=abs)#key=abs абсолютное значение
    if victory == 0:
        player_verxus_player.no_winners(rate) # player_verxus_player
    else:
        print("Победителей ", victory)
        gain = rate / victory#расчитывется выигрыш каждого игрока
        several_winners(max_card, gain, card1, card2)


def duplicate_card_one(rate, max_value, card1, card2):
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
    else:
        player_verxus_player.no_winners(rate) #player_verxus_player

def def_win(rate, game_results, card1, card2):
    '''определение победителя'''
    game_results = module_functions.function_list_game_results(game_results)
    max_value = max(game_results, key=abs)#key=abs абсолютное значение
    minus_max_value = -max_value
    if minus_max_value in game_results:
        duplicate_cards(rate, game_results, card1, card2)
    duplicate_max_card = game_results.count(max_value)#узнаем сколько раз значение встречатеся
    if duplicate_max_card == 1:
        duplicate_card_one(rate, max_value, card1, card2)
    elif duplicate_max_card > 1:
        duplicate_cards(rate, game_results, card1, card2)
    elif duplicate_max_card == 0:
        player_verxus_player.no_winners(rate) #player_verxus_player

def phase_change_cycle_computer(card):#функция для игрока компьютера
    '''стадия получение'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    if name is not None:
        shufflingcard = random.choice(player_verxus_player.CARDS)
        player_list.append(shufflingcard)
        print("Компьютер получил карту", shufflingcard)
#        print("Вы отказались от карты.\n")
#        print("Помещение карт в поле помех.")
#        if len(player_list) is None:# != 0:#вызов функции в функции
#            card = player_verxus_player.field_interference(card)
#        choice_2 = module_functions.repeat_choice_str()#если игрок помещал карты в поле помех
#        if choice_2 == POSITIVE_ANSWER:#необходимо чтобы он изменил или не изменил колоду карт
#            shufflingcard = random.choice(player_verxus_player.CARDS)
#            player_list.append(shufflingcard)
#            print(player_list)
#        elif choice == NEGATIVE_ANSWER:
#            print("Вы отказались от карты.\n", player_list)
#        else:
#            print("Вы нажали неверную кнопку.")
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(name, bankroll, player_list, value[3], value[4])
        card.AMOUNT_OF_PLAYER_CARDS = amount
    return card

def phase_change_cycle(card):
    '''стадия получение'''
    value = card.function_list()
    name = value[0]
    bankroll = value[1]
    player_list = value[2]
    if name is not None:
        print("Игрок", name, "вам нужна новая карта?")
        choice = module_functions.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            shufflingcard = random.choice(player_verxus_player.CARDS)
            player_list.append(shufflingcard)
            print("Игрок получил карту", shufflingcard)
        elif choice == NEGATIVE_ANSWER:
            print("Вы отказались от карты.\n")
        elif choice == INTERFERENCE:
            print("Помещение карт в поле помех.")
            if len(player_list) is None:# != 0:#вызов функции в функции
                card = player_verxus_player.field_interference(card)
            choice_2 = module_functions.repeat_choice_str()#если игрок помещал карты в поле помех
            if choice_2 == POSITIVE_ANSWER:#необходимо чтобы он изменил или не изменил колоду карт
                shufflingcard = random.choice(player_verxus_player.CARDS)
                player_list.append(shufflingcard)
                print("501", player_list)
            elif choice == NEGATIVE_ANSWER:
                print("Вы отказались от карты.\n", player_list)
            else:
                print("Вы нажали неверную кнопку.")
        amount = card.AMOUNT_OF_PLAYER_CARDS
        card = Player(name, bankroll, player_list, value[3], value[4])
        card.AMOUNT_OF_PLAYER_CARDS = amount
    return card

def stage_new_cards_players(card1, card2):
    '''стадия получение карт для игроков'''
    card = card1.function_list()
    if card1 is not None and card[4] is False:
        card1 = phase_change_cycle(card1)
    card = card2.function_list()
    if card2 is not None and card[4] is True:
        card2 = phase_change_cycle_computer(card2)
    return card1, card2

def round_1(card_player, card_computer, number_rounds, rate):
    '''1 раунд игры - стадия торг'''
    print("Раунд", number_rounds, "\nСтадия Торг")#игроки по очереди делают ставки
    card_player, card_computer, rate = players_rate(card_player, card_computer, rate)
    card_player, card_computer, rate = betting_odds(card_player, card_computer, rate)
    return card_player, card_computer, rate

def round_second(card_player, card_computer):
    '''2 раунд - изменение карт игроков, в зависимости от броска кубика'''
    print("Стадия Изменение.")#"бросание кубик" и определяет
    likely_to_change_card_deck = module_functions.block()#смогут ли игроки изменить свои карты
    if likely_to_change_card_deck < 4:#цикл для изменения колоды карт, функция block это кубик
        print("На шестигранном кубике выпало:", likely_to_change_card_deck)
        print("Изменения карт не будет")
    else:
        print("На шестигранном кубике выпало:", likely_to_change_card_deck)
        card_player, card_computer = stage_change_players(card_player, card_computer)
    return card_player, card_computer

def round_fourth(card1, card2):
    '''стадия получения карт'''
    print("Стадия Получение.")
    card1, card2 = stage_new_cards_players(card1, card2)
    return card1, card2

def player_verxus_computer():
    '''цикл игры'''
    try:
        print(Fore.YELLOW + "Игра началась")
    except Exception:
        print("Игра началась")
    variable_game = True
    number_rounds = 1
    card_player, card_computer, rate = game()
    output_of_game_results(card_player, card_computer)
    while variable_game:
        card_player, card_computer = function_jummer(card_player, card_computer)
        card_player, card_computer, rate = round_1(card_player, card_computer, number_rounds, rate)
        card_player, card_computer = function_jummer(card_player, card_computer)
        check_presence_game(rate, card_player, card_computer)
        card_player, card_computer = round_second(card_player, card_computer)
        card_player, card_computer = function_jummer(card_player, card_computer)
        if number_rounds >= 1:
            answer = False
            game_result = []
            card_player, card_computer = function_jummer(card_player, card_computer)
            print("Стадия Открытие карт.")#opening stage по английски
            answer, game_result = opening_players(card_player, card_computer, answer, game_result)
            if answer is True:#значит игроки открылись
                def_win(rate, game_result, card_player, card_computer)
                variable_game = False
                break
        card_player, card_computer = function_jummer(card_player, card_computer)
        card_player, card_computer = round_fourth(card_player, card_computer)
        card_player, card_computer = function_jummer(card_player, card_computer)
        print("Конец раунда", number_rounds)
        number_rounds = number_rounds + 1
        variable_game = False
        LIST_PLAYERS_RATE.clear()

#player_verxus_computer()
if __name__ == "__main__":
    print("This is a module with game Sabacc.")
    input("\n\nPress the enter key to exit.")
