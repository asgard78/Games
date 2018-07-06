# -*- coding: utf-8 -*-
"""
Игрок против компьютера
"""
import random
try:
    from colorama import init, Fore#библиотека используется для вывода цветного текста в терминал
except ImportError:
    pass

import module_functions_game

try:
    init()#инициализация библиотеки colorama
except Exception:
    pass

LIST_PLAYERS_RATE = [] #список ставок игроков в раунде
POSITIVE_ANSWER, NEGATIVE_ANSWER, INTERFERENCE = module_functions_game.read_regulations_with_file()

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

def delete_card(card):
    '''удалениет карты из общего списка'''
    CARDS.remove(card)

def add_card(card):
    '''возврашение карты в список'''
    CARDS.append(card)

def function_player_list():
    '''функция для формирования списка игрока'''
    list_player = []                     #объявление списка игрока
    score = random.choice(CARDS)         #выбор случайного элемента списка CARDS
    shufflingcards = random.choice(CARDS)#и присваивание его переменной score
    list_player.append(score)            #добавление элемента score в список игрока
    list_player.append(shufflingcards)   #нужно добавить 2 случайных элемента в список
    delete_card(score)         #удаление карт из общего списка
    delete_card(shufflingcards)#чтобы они не были повторно розданы другому (-им) игрокам
    return list_player                   #возвращение списка

def new_card(dict_player):
    '''если у нескольких претендентов на победу одинаковые значения карт'''
    if dict_player['name'] and dict_player['player_list'] is not None:
        shufflingcards = random.choice(CARDS) #нужно выдать новую карту, для определения победителя
        print("Игрок", dict_player['name'], "получил новую карту", shufflingcards)
        dict_player['player_list'].append(shufflingcards)#значение карты + результат игрока
        delete_card(shufflingcards)
        print("Результат игрока", dict_player['name'], "=", dict_player['player_list'])
    return dict_player['player_list'], dict_player

def computer_bankroll():
    '''деньги на которые компьютер будет играть'''
    bankroll = random.randint(10, 100)
    return bankroll

def igentification_gamer(player, computer_player):
    '''идентификация игрока'''
    player['player_list'] = function_player_list()#данные для игрока
    player['name'] = module_functions_game.player_name()
    player['bankroll'] = module_functions_game.player_bankroll()
    computer_player['player_list'] = function_player_list()#данные для ии
    computer_player['bankroll'] = computer_bankroll()
    return player, computer_player

def jummer(dict_player):
    '''jummer - изменение карт игрока'''
    list_jummer = [] #новый список
    for i in dict_player['player_list']:
        if i in dict_player['list_interference']:
            list_jummer.append(i)
            dict_player['list_interference'].remove(i)
        else:
            shufflingcard_0 = random.choice(CARDS)
            list_jummer.append(shufflingcard_0)
            delete_card(shufflingcard_0)
    print("Список карт игрока", dict_player['name'], "после изменения ", list_jummer)
    dict_player['player_list'] = list_jummer
    return dict_player

def change_player_card(dict_player):
    '''фактор случайности - изменяться ли карты у игрока'''
    if dict_player['name'] is not None:
        dict_player = jummer(dict_player)
    return dict_player

def change_players_cards(player, computer_player):
    '''изменение карт у игроков'''
    print("Произошло изменение карт.")
    if player['name'] is not None:
        player = change_player_card(player)
    if computer_player['name'] is not None:
        computer_player = change_player_card(computer_player)
    return player, computer_player

def function_jummer(player, computer_player):
    '''функция вызывающая изменение карт у всех игроков'''
    block = module_functions_game.block()#функция, определяющяя будет изменение карт или нет
    if block == 1:
        player, computer_player = change_players_cards(player, computer_player)
    return player, computer_player

def game(player, computer_player):
    '''начало игры, перед раундами'''
    rate = 0
    rate = module_functions_game.rate_with_last_games()
    try:
        print(Fore.YELLOW + "Начинаем игру в сабакк!")
    except Exception:
        print("Начинаем игру в сабакк!")
    player, computer_player = igentification_gamer(player, computer_player)
    return player, computer_player, rate

def output_of_game_results(player, computer_player):
    '''выводит на экран результаты игроков'''
    if player['name'] is not None:
        print("Результаты игрока", player['name'], player['player_list'])
    if computer_player is not None:
        print("Результаты игрока", computer_player['name'], computer_player['player_list'])

def bet_size(dict_player, rate):#размер ставки
    '''размер ставки, которую может сделать игрок'''
    print(dict_player['name'], "введите сумму ставки?")
    choice = module_functions_game.repeat_choice_int()
    if choice > 0:#чтобы игроки не делали "нулевых" ставок
        if dict_player['bankroll'] >= choice:
            print(dict_player['name'], "сделал ставку", choice)
            LIST_PLAYERS_RATE.append(choice)
            rate = rate + choice
            dict_player['bankroll'] = dict_player['bankroll'] - choice
        else:
            print("У вас недостаточно средств для такой ставки. Сделайте меньшую ставку.")
            if dict_player['bankroll'] > 0:
                dict_player['bankroll'], rate, dict_player = bet_size(dict_player, rate)
            else:
                print(dict_player['name'], "не имеет денег для продолжения и покидает игру.")
                dict_player = {'name': None, 'bankroll': None, 'player_list': None,
                               'list_interference': None, 'amount': None, 'ii_or_human': None}
    else:
        print("Вы не можете сделать нулевую ставку.")
        dict_player['bankroll'], rate, dict_player = bet_size(dict_player, rate)#def вызывает себя
    return dict_player['bankroll'], rate, dict_player

def bet_size_computer(dict_player, rate):#размер ставки
    '''размер ставки, которую может сделать игрок'''
    if dict_player['bankroll'] > 0:#чтобы игроки не делали "нулевых" ставок
        choice = random.randint(1, 3)
        if dict_player['bankroll'] >= choice:
            print(dict_player['name'], "сделал ставку", choice)
            LIST_PLAYERS_RATE.append(choice)
            rate = rate + choice
            dict_player['bankroll'] = dict_player['bankroll'] - choice
        else:
            if dict_player['bankroll'] > 0:
                dict_player['bankroll'], rate, dict_player = bet_size_computer(dict_player, rate)
            else:
                print(dict_player['name'], "не имеет денег для продолжения и покидает игру.")
                dict_player = {'name': None, 'bankroll': None, 'player_list': None,
                               'list_interference': None, 'amount': None, 'ii_or_human': None}
    else:
        print(dict_player['name'], "может сделать нулевую ставку.")
        dict_player['bankroll'], rate, dict_player = bet_size(dict_player, rate)
    return dict_player['bankroll'], rate, dict_player

def player_done_rate(dict_player, rate):
    '''игроки делают ставки'''
    if dict_player['ii_or_human'] is True:
        dict_player['bankroll'], rate, dict_player = bet_size_computer(dict_player, rate)
    else:
        print(dict_player['name'], "будете делать ставку")
        choice = module_functions_game.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            dict_player['bankroll'], rate, dict_player = bet_size(dict_player, rate)
            if dict_player['name'] is None:
                dict_player = {'name': None, 'bankroll': None, 'player_list': None,
                               'list_interference': None, 'amount': None, 'ii_or_human': None}
        elif choice == NEGATIVE_ANSWER:
            value = len(LIST_PLAYERS_RATE)
            if value > 0:#чтобы избежать ситуации, когда 1 игрок не делает ставку
                max_valua = max(LIST_PLAYERS_RATE)#и игра вылетает
                if max_valua == 0:
                    print(dict_player['name'], "не сделал ставку.")
                    LIST_PLAYERS_RATE.append(0)
                else:
                    print(dict_player['name'], "не сделал ставку и вышел из игры.")
                    dict_player = {'name': None, 'bankroll': None, 'player_list': None,
                                   'list_interference': None, 'amount': None, 'ii_or_human': None}
                    LIST_PLAYERS_RATE.append(0)#для того чтобы не сбивались номера в списке ставок
            else:
                print(dict_player['name'], "не сделал ставку.")
                LIST_PLAYERS_RATE.append(0)
        elif choice == INTERFERENCE:
            dict_player = module_functions_game.field_interference(dict_player)
            dict_player, rate = player_done_rate(dict_player, rate)
        else:
            print("Вы ввели неверное значение")
    return dict_player, rate

def check_presence_game(rate, player, computer_player):
    '''проверка игроков после раунда ставок в игре'''
    number = 0
    name = 0
    player['name'], number = module_functions_game.def_check(player, name, number)
    computer_player['name'], number = module_functions_game.def_check(computer_player, name, number)
    if number == 0:
        module_functions_game.no_winners(rate)
    elif number == 1:
        print("Игрок", name, "выиграл банк ", rate)###################
        module_functions_game.write_in_file(name, rate)

def players_rate(player, computer_player, rate):
    '''игроки по очереди делают ставки'''
    if player['name'] is not None:
        player, rate = player_done_rate(player, rate)
    if computer_player['name'] is not None:
        computer_player, rate = player_done_rate(computer_player, rate)
    return player, computer_player, rate

def bet_size_in_betting_odds(dict_player, difference, rate):#размер ставки,
    '''размер ставки, которую может сделать игрок'''#если игроки сделали разные ставки
    if dict_player['name'] is not None and difference != 0 and dict_player['ii_or_human'] is False:
        print(dict_player['name'], "сделаете ставку", difference, "?")#и не делать лишнего действия
        choice = module_functions_game.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            if dict_player['bankroll'] >= difference:#rate >= 0:
                print(dict_player['name'], "сделал ставку", difference)
                dict_player['bankroll'] = dict_player['bankroll'] - difference
                rate = rate + difference
            else:
                print("Вы не можете сделать ставку и покидаете игру.")
                dict_player = {'name': None, 'bankroll': None, 'player_list': None,
                               'list_interference': None, 'amount': None, 'ii_or_human': None}
        elif choice == NEGATIVE_ANSWER:
            print(dict_player['name'], "не сделал ставку и вышел из игры.")
            dict_player = {'name': None, 'bankroll': None, 'player_list': None,
                           'list_interference': None, 'ii_or_human': None}
        elif choice == INTERFERENCE:
            dict_player = module_functions_game.field_interference(dict_player)
            dict_player, difference = player_done_rate(dict_player, difference)
    elif dict_player['name'] is not None and difference != 0 and dict_player['ii_or_human'] is True:
        if dict_player['bankroll'] >= difference:#rate >= 0:
            print(dict_player['name'], "сделал ставку", difference)
            dict_player['bankroll'] = dict_player['bankroll'] - difference
            rate = rate + difference
        else:
            print(dict_player['name'], "не сделал ставку и вышел из игры.")
            dict_player = {'name': None, 'bankroll': None, 'player_list': None,
                           'list_interference': None, 'amount': None, 'ii_or_human': None}
    return dict_player, rate

def betting_odds(card1, card2, rate):
    '''если игроки сделали разные ставки'''#разница ставок игроков
    min_value = 0
    max_value = 0
    value = len(LIST_PLAYERS_RATE)
    if value > 0:
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

def stage_change(dict_player):
    '''стадия изменение'''
    if dict_player['name'] is not None and dict_player['ii_or_human'] is False:
        print(dict_player['name'], "хотите изменить какую-либо карту из своей колоды")
        choice = module_functions_game.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            print(dict_player['name'], "выберите какую карту хотите изменить?")
            card_player = module_functions_game.repeat_choice_str()
            if card_player in dict_player['player_list']:
                dict_player['player_list'].remove(card_player)
                new_card_0 = random.choice(CARDS)
                dict_player['player_list'].append(new_card_0)
                add_card(card_player)
            else:
                print("Такой карты нет в списке")
        elif choice == NEGATIVE_ANSWER:
            print(dict_player['name'], "отказался от изменения колоды.")
        elif choice == INTERFERENCE:
            dict_player = module_functions_game.field_interference(dict_player)
    elif dict_player['name'] is not None and dict_player['ii_or_human'] is True:
        print("Игрок ", dict_player['name'], "изменил свои карты.")
        card_player = random.choice(dict_player['player_list'])#случайно выбираю, какую карту
        dict_player['player_list'].remove(card_player)#если у компьютера меньше
        add_card(card_player)
        new_card_0 = random.choice(CARDS)
        dict_player['player_list'].append(new_card_0)
        delete_card(new_card_0)
    return dict_player

def stage_change_players(player, computer_player):
    '''игроки по очереди делают ставки'''
    if player['name'] is not None:
        player = stage_change(player)
    if computer_player['name'] is not None:
        computer_player = stage_change(computer_player)
    return player, computer_player

def player_open_cards(dict_player, game_results):
    '''игрок открывает свои карты'''
    if dict_player['name'] is not None and dict_player['ii_or_human'] is True:
        print("Игрок ", dict_player['name'], " открылся.")#player_list
        print("Карты игрока ", dict_player['player_list'])
        val = module_functions_game.open_list_stage(dict_player['name'], dict_player['player_list'])
        if val < 24 and val > -24:
            game_results.append(val)#добавление результата игрока в список
        else:
            game_results.append(-10000)#если напишу None, for не сможет перебрать список
    if dict_player['name'] is not None and dict_player['ii_or_human'] is False:
        print("Игрок ", dict_player['name'], " открылся.")#player_list
        print("Карты игрока ", dict_player['player_list'])
        val = module_functions_game.open_list_stage(dict_player['name'], dict_player['player_list'])
        if val < 24 and val > -24:
            game_results.append(val)#добавление результата игрока в список
        else:
            game_results.append(-10000)#если напишу None, for не сможет перебрать список
    return game_results, dict_player

def opening_players(player, computer_player, answer, game_results):
    '''игроки по очереди открывают карты'''
    if computer_player['name'] is not None and answer is False:
        val_player = module_functions_game.amount_player(player['player_list'])
        answer = module_functions_game.computer_opening_cards(computer_player, val_player)
        if answer is False:
            print(computer_player['name'], "не стал открывать карты.")
    if player['name'] is not None and answer is False:
        answer = module_functions_game.stage_opening_cards(player)
    if answer is True:
        if player['name'] is not None:
            game_results, player = player_open_cards(player, game_results)
        if computer_player['name'] is not None:
            game_results, computer_player = player_open_cards(computer_player, game_results)
    return answer, game_results

def list_game_results_players(dict_player):
    '''выдача 1 новой карты каждому игроку с одинаково наибольшими результатам'''
    game_results = []
    if dict_player['name'] is not None:
        dict_player['player_list'], dict_player = new_card(dict_player)
        res = module_functions_game.open_list_stage(dict_player['name'], dict_player['player_list'])
        game_results.append(res)
    return game_results, dict_player

def duplicate_card_one(rate, max_value, player, computer_player):
    '''если победитель один'''
    if player['name'] is not None and max_value == player['amount']:
        print("Победил игрок", player['name'], ", его выигрыш =", rate)
        module_functions_game.write_in_file(player['name'], rate)
    elif computer_player['name'] is not None and max_value == computer_player['amount']:
        print("Победил игрок", computer_player['name'], ", его выигрыш =", rate)
        module_functions_game.write_in_file(computer_player['name'], rate)
    else:
        module_functions_game.no_winners(rate)

def duplicate_cards(rate, player, computer_player):
    '''предполагаемых победителей несколько'''
    print("Двое игроков претендуют на победу.")
    gain = 0.0#для получения дробного выражения
    game_results_players = []
    game_results_players, player = list_game_results_players(player)
    game_results_players, computer_player = list_game_results_players(computer_player)
    victory = module_functions_game.function_victory(game_results_players)
    max_card = max(game_results_players, key=abs)#key=abs абсолютное значение
#    print("376", victory, computer_player['amount'], player['amount'], max_card)
    if victory == 0:
        module_functions_game.no_winners(rate)
    elif victory == 1:
        duplicate_card_one(rate, max_card, player, computer_player)
    elif victory == 2:
        print("Победителей ", victory)
        gain = rate / victory  #расчитывется выигрыш каждого игрока
        if player['name'] is not None and player['amount'] == max_card:
            module_functions_game.several_winners_number(player, gain)
        if computer_player['name'] is not None and computer_player['amount'] == max_card:
            module_functions_game.several_winners_number(computer_player, gain)

def def_win(rate, game_results, player, computer_player):
    '''определение победителя'''
    game_results = module_functions_game.function_list_game_results(game_results)
    player['amount'] = module_functions_game.amount_player(player['player_list'])
    computer_player['amount'] = module_functions_game.amount_player(computer_player['player_list'])
    max_value = max(game_results, key=abs)#key=abs абсолютное значение
    minus_max_value = -max_value
    if minus_max_value in game_results:
        duplicate_cards(rate, player, computer_player)
        duplicate_minus_max_card = game_results.count(minus_max_value)
        if duplicate_minus_max_card == 1:
            duplicate_card_one(rate, max_value, player, computer_player)
        elif duplicate_minus_max_card > 1:
            duplicate_cards(rate, player, computer_player)
        elif duplicate_minus_max_card == 0:
            module_functions_game.no_winners(rate)
    duplicate_max_card = game_results.count(max_value)#узнаем сколько раз значение встречатеся
    if duplicate_max_card == 0:
        module_functions_game.no_winners(rate)
    elif duplicate_max_card == 1:
        duplicate_card_one(rate, max_value, player, computer_player)
    elif duplicate_max_card > 1:
        duplicate_cards(rate, player, computer_player)

def phase_change_cycle_computer(dict_player):#функция для игрока компьютера
    '''стадия получение'''
    if dict_player['name'] is not None:
        shufflingcard = random.choice(CARDS)
        dict_player['player_list'].append(shufflingcard)
#        print("Компьютер получил карту", shufflingcard)
        delete_card(shufflingcard)
        dict_player['amount'] = module_functions_game.amount_player(dict_player['player_list'])
        if dict_player['amount'] == 23 or dict_player['amount'] == -23:
            for i in dict_player['player_list']:
                dict_player['list_interference'].append(i)
    return dict_player

def phase_change_cycle(dict_player):
    '''стадия получение'''
    if dict_player['name'] is not None:
        print("Игрок", dict_player['name'], "вам нужна новая карта?")
        choice = module_functions_game.repeat_choice_str()
        if choice == POSITIVE_ANSWER:
            shufflingcard = random.choice(CARDS)
            dict_player['player_list'].append(shufflingcard)
            print("Игрок получил карту", shufflingcard)
            delete_card(shufflingcard)
        elif choice == NEGATIVE_ANSWER:
            print("Вы отказались от карты.\n")
        elif choice == INTERFERENCE:
            print("Помещение карт в поле помех.")
            if len(dict_player['player_list']) is None:# != 0:#вызов функции в функции
                dict_player = module_functions_game.field_interference(dict_player)
            choice_2 = module_functions_game.repeat_choice_str()#игрок помещал карты в поле помех
            if choice_2 == POSITIVE_ANSWER:#необходимо чтобы он изменил или не изменил колоду карт
                shufflingcard = random.choice(CARDS)
                dict_player['player_list'].append(shufflingcard)
                delete_card(shufflingcard)
            elif choice == NEGATIVE_ANSWER:
                print("Вы отказались от карты.\n", dict_player['player_list'])
            else:
                print("Вы нажали неверную кнопку.")
    return dict_player

def stage_new_cards_players(player, computer_player):
    '''стадия получение карт для игроков'''
    len_list_player = len(player['player_list'])
    len_list_computer = len(computer_player['player_list'])
    if player['name'] is not None and len_list_player < 5:
        player = phase_change_cycle(player)
    if len_list_player == 5:
        print("У игрока уже есть 5 карт на руках.")
    if computer_player['name'] is not None and len_list_computer < 5:
        computer_player = phase_change_cycle_computer(computer_player)
    return player, computer_player

def round_1(player, computer_player, number_rounds, rate):
    '''1 раунд игры - стадия торг'''
    print("Раунд", number_rounds, "\nСтадия Торг")#игроки по очереди делают ставки
    player, computer_player, rate = players_rate(player, computer_player, rate)
    player, computer_player, rate = betting_odds(player, computer_player, rate)
    return player, computer_player, rate

def round_second(player, computer_player):
    '''2 раунд - изменение карт игроков, в зависимости от броска кубика'''
    print("Стадия Изменение.")#"бросание кубик" и определяет
    likely_to_change_card_deck = module_functions_game.block()#смогут ли игроки изменить свои карты
    if likely_to_change_card_deck < 4:#цикл для изменения колоды карт, функция block это кубик
        print("На шестигранном кубике выпало:", likely_to_change_card_deck)
        print("Изменения карт не будет")
    else:
        print("На шестигранном кубике выпало:", likely_to_change_card_deck)
        player, computer_player = stage_change_players(player, computer_player)
    return player, computer_player

def round_fourth(player, computer_player):
    '''стадия получения карт'''
    print("Стадия Получение.")
    player, computer_player = stage_new_cards_players(player, computer_player)
    return player, computer_player

def player_v_computer():
    '''цикл игры'''
    player = {'name': 'noname', 'bankroll': 0, 'player_list': [], 'list_interference': [],
              'amount': 0, 'ii_or_human': False}
    computer_player = {'name': 'Computer', 'bankroll': 0, 'player_list': [],
                       'list_interference': [], 'amount': 0, 'ii_or_human': True}
    variable_game = True
    number_rounds = 1
    player, computer_player, rate = game(player, computer_player)
    output_of_game_results(player, computer_player)
    while variable_game:
        player, computer_player = function_jummer(player, computer_player)
        player, computer_player, rate = round_1(player, computer_player, number_rounds, rate)
        player, computer_player = function_jummer(player, computer_player)
        check_presence_game(rate, player, computer_player)
        player, computer_player = round_second(player, computer_player)
        player, computer_player = function_jummer(player, computer_player)
        if number_rounds > 3:
            answer = False
            game_result = []
            player, computer_player = function_jummer(player, computer_player)
            print("Стадия Открытие карт.")#opening stage по английски
            answer, game_result = opening_players(player, computer_player, answer, game_result)
            if answer is True:#значит игроки открылись
                def_win(rate, game_result, player, computer_player)
                variable_game = False
                break
        player, computer_player = function_jummer(player, computer_player)
        player, computer_player = round_fourth(player, computer_player)
        player, computer_player = function_jummer(player, computer_player)
        print("Конец раунда", number_rounds)
        number_rounds = number_rounds + 1
        LIST_PLAYERS_RATE.clear()

if __name__ == "__main__":                     #если победителей 2,
    print("This is a module with game Sabacc.")#на экран 2 раза выводятся имя и выигрыш победителя
    input("\n\nPress the enter key to exit.")  #появляются 2 одинаковые записи в сохранениях
