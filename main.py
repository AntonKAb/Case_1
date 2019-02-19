"""
CASE_1
Developers: Anufrienko K., Kabaev A., Lankevich S.
"""


from random import randint, choice
from ru_local import *


class Game:
    turn = 0
    turns = {}
    life = True
    prince = False


class State:
    money = 1000
    food = 10000
    people = 200
    population_growing = 0.01
    distemper = 0
    army = 100
    year = 0
    land = 130
    technologies = {'cattle_breeding': 0, 'agriculture': 0, 'hunting': 0, 'warfare': 0, 'mansory': 0, 'religion': 0,
                    'rivalry': 0}
    buildings = {'windmill': 0, 'accounting_chamber': 0, 'moulin_rouge': 0}
    tech_effects = {'food': 1.0, 'money': 1.0, 'people': 1.0, 'distemper': 1.0, 'army': 1.0, 'land': 1.0}


def acknowledgement():
    available_technologies = []
    if turn_counter <= 4:
        for obj in State.technologies[:3].keys():
            if not State.technologies[obj]:
                available_technologies.append(obj)
        available_message = ACKNOWLEDGEMENT[0]
        for obj in available_technologies:
            available_message += obj + ', '
        available_message = available_message[:-2]
        print(available_message)
        answer = input(ACKNOWLEDGEMENT[1])
        while answer not in available_technologies:
            answer = input(ACKNOWLEDGEMENT[2])
        later_event(2, res_changes(answer, '+1'))
    if turn_counter > 4:
        for obj in State.technologies.keys():
            if not State.technologies[obj]:
                available_technologies.append(obj)
        available_message = ACKNOWLEDGEMENT[3]
        for obj in available_technologies:
            available_message += obj + ', '
        available_message = available_message[:-2]
        print(available_message)
        answer = input(ACKNOWLEDGEMENT[4])
        while answer not in available_technologies:
            answer = input(ACKNOWLEDGEMENT[5])
        later_event(2, res_changes(answer, '+1'))
        later_event(2, answer)


def moulin_rouge():
    print(MOULIN_ROUGE)
    res_changes('people', f'+{int((percent_changes(State.people, 3)))}'
                'distemper', f'-{int(percent_changes(State.distemper, 30))}'
                'money', f'-500')


def church():
    print(CHURCH)
    res_changes('distemper', f'-{(percent_changes(State.distemper, 50))}'
                'money', f'-2000')


def accounting_chamber():
    print(ACCOUNTING_CHAMBER)
    res_changes('money', f'+{int(percent_changes(State.money, 35))}')


def windmill():
    print(WINDMILL)
    res_changes('food', f'+{int(percent_changes(State.food, 20))}')
    res_changes('money', f'-{int(percent_changes(State.money, 50))}')


def barracks():
    print(BARRACKS)
    res_changes('money', f'-600')
    res_changes('army', f'+{int(percent_changes(State.army, 35))}')


def cattle_breeding():
    print(CATTLE_BREEDING)
    State.tech_effects.update({'food': 1.25})
    State.money -= 400


def agriculture():
    print(AGRICULTURE)
    State.tech_effects.update({'food': 1.25})
    State.money -= 400


def sailing():
    print(SAILING)
    State.tech_effects.update({'food': 1.25})
    State.tech_effects.update({'army': 1.15})
    State.money -= 400


def hunting():
    print(HUNTING)
    State.tech_effects.update({'food': 2})
    State.money -= 400


def warfare():
    print(WARFARE)
    State.buildings.update({'Казармы': 0})
    State.tech_effects.update({'army': 1.33})
    State.money -= 400


def religion():
    print(RELIGION)
    State.buildings.update({'Church': 0})
    State.money -= 400


def masonry():
    print(MASONRY)
    State.buildings.update({'The Great Wall': 0})
    State.money -= 400


def rivalry():
    print(RIVALRY)
    State.tech_effects.update({'army': 1.5})
    State.money -= 400


def random_events():
    negative_events = [village_fire, city_fire, flood, conspiracy, strike, plague, separatism, war, spy,
                       cruel_winter, pirates]
    positive_events = [discovery, road, hero, wonder_of_nature, forest_territory, city_state]
    if State.technologies.get('masonry') == 1:
        positive_events.append(brilliants)
    if State.technologies.get('rivalry') == 1:
        positive_events.append(tournament)
    choice(negative_events)
    choice(positive_events)


def output():
    print('Деньги: {} | Зерно: {} | Народ: {} | Смута: {} '
          '| Год: {} | Замля: {} | Еда: {} | Армия: {}'.format(State.money, 
                                                               State.food, State.people, State.distemper,
                                                               State.year, State.land, State.food, State.army))
    

def seed_own():
    print(SEED_OWN[0])
    am_to_seat = int(input())
    State.food -= am_to_seat
    print(SEED_OWN[1])
    am_to_give = int(input())
    State.food -= am_to_give
    if 1000 <= am_to_give < 2500 and State.people < 300:
        State.people = State.people * 1.05
    if 2500 <= am_to_give < 5000 and State.people < 300:
        State.people = State.people * 1.1
    if am_to_give >= 5000 and State.people < 300:
        State.people = State.people * 1.15
    if 1000 <= am_to_give < 2500 and State.people >= 300:
        State.people = State.people * 1.03
    if 2500 <= am_to_give < 5000 and State.people >= 300:
        State.people = State.people * 1.05
    if am_to_give >= 5000 and State.people >= 300:
        State.people = State.people * 1.08
    af_event_1 = SEED_OWN[2]
    af_event_2 = SEED_OWN[3]
    af_event_3 = SEED_OWN[4]
    af_event_4 = SEED_OWN[5]
    ev_all = [af_event_4, af_event_1, af_event_2, af_event_3]
    ev_r = choice(ev_all)
    if ev_r == af_event_1:
        State.food += am_to_seat * 0.75
    elif ev_r == af_event_2:
        State.food += am_to_seat * 2
    elif ev_r == af_event_3:
        State.food += am_to_seat * 1.5
    elif ev_r == af_event_4 and State.people > 300 and State.food < 5000:
        State.people = State.people * 0.85
        State.distemper += 5
        print(SEED_OWN[6])
        print(SEED_OWN[7])
    elif ev_r == af_event_4 and (State.food >= 5000 or State.people < 300):
        pass


def seed_sell():
    print(SEED_SELL[0])
    am_sell = int(input())
    if State.food < am_sell:
        while am_sell > State.food:
            print(SEED_SELL[1])
            am_sell = int(input())
        State.food -= am_sell
        State.money += am_sell * 2
    if State.food >= am_sell:
        State.food -= am_sell
        State.money += am_sell * 2


def seed_buy():
    print(SEED_BUY[0])
    am_buy = int(input())
    if State.money < am_buy * 2:
        while am_buy * 2 > State.money:
            print(SEED_BUY[1])
            am_buy = int(input())
        State.food += am_buy
        State.money -= am_buy * 2
    if State.money >= am_buy * 2:
        State.food += am_buy
        State.money -= am_buy * 2


def war():
    event = WAR[0]
    print(event)
    answ_w = input()
    if answ_w.upper() == WAR[1] and State.money >= 5000 and State.army >= 30:
        State.money -= 5000
        State.army -= 30
    elif answ_w.upper() == WAR[2]:
        pass
    elif answ_w.upper() == WAR[1] and (State.money < 5000 or State.army < 30):
        print(WAR[3])
    later_event(1, war_exodus)


def war_exodus():
        event_af1 = WAR_EXODUS[0]
        event_af2 = WAR_EXODUS[1]
        con_war = choice([event_af1, event_af2])
        print(con_war)
        if con_war == event_af1:
            print(WAR_EXODUS[2])
            print(WAR_EXODUS[3])
            State.distemper += 3
        if con_war == event_af2:
            print(WAR_EXODUS[4])
            State.money += 12000
            State.army += 25


def separatism():
    print(SEPARATISM[0])
    answr = input()
    evi_1 = SEPARATISM[1]
    evi_2 = SEPARATISM[2]
    if answr.upper() == SEPARATISM[3]:
        print(SEPARATISM[4])
        army = int(input())
        if State.army >= army:
            State.army -= army
        if State.army < army:
            while army > State.army:
                print(SEPARATISM[5])
                army = int(input())
            State.army -= army
        if army < 20:
            print(evi_2, SEPARATISM[6])
            State.land -= 30
            State.people -= 15
            State.army -= army
            State.distemper += 3
            print(SEPARATISM[7])
            print(SEPARATISM[8])
            print(SEPARATISM[9], army)
            print(SEPARATISM[10])
        if army >= 20:
            print(evi_1)
    if answr.upper() == SEPARATISM[11]:
        State.land -= 30
        State.people -= 15
        print(SEPARATISM[12])
        print(SEPARATISM[13])


def discovery():
    print(DISCOVERY[0])
    answer = input()
    if answer.upper() == DISCOVERY[1] and State.money >= 1000 and State.people >= 10:
        State.money -= 1000
        State.people -= 10
        print(DISCOVERY[2])
        print(DISCOVERY[3])
    if answer.upper() == DISCOVERY[4]:
        pass
    ev_1_ = DISCOVERY[5]
    ev_2_ = DISCOVERY[6]
    d_exodus = choice([ev_1_, ev_2_])
    if d_exodus == ev_1_:
        print(ev_1_)
        State.food += 420
        State.land += 40
        State.people += 10
        if State.distemper >= 10:
            State.distemper -= 10
            print(DISCOVERY[7])
        print(DISCOVERY[8])
        print(DISCOVERY[9])
    if d_exodus == ev_2_:
        print(DISCOVERY[10])


def spy():
    print(SPY[0])
    ans = input()
    if ans.upper() == SPY[1]:
        catch = SPY[2]
        lose = SPY[3]
        d_yes = choice([catch, lose])
        if d_yes == catch:
            print(catch)
            State.distemper -= 3
            print(SPY[4])
            print(SPY[5])
        if d_yes == lose:
            print(SPY[6])
    if ans.upper() == SPY[7]:
        lose_1 = SPY[8]
        bad_l = SPY[9]
        d_no = choice([bad_l, lose_1])
        if d_no == lose_1:
            print(lose_1)
            State.distemper += 13
            State.money -= 520
            print(SPY[10])
            print(SPY[11])


def husbrandy():
    print(HUSBRANDY[0])
    dision = int(input())
    if dision <= State.land:
        State.land -= dision
        State.food += dision * 10
        print(HUSBRANDY[1], dision)
        print(HUSBRANDY[2], dision * 10)
    if dision > State.land:
        while dision > State.land:
            dision = int(input())
        State.land -= dision
        State.food += dision * 10
        print(HUSBRANDY[3], dision)
        print(HUSBRANDY[4], dision * 10)


def wizard():
    print(WIZARD[0])
    chose = input()
    if chose.upper() == WIZARD[1]:
        print(WIZARD[2])
        print(WIZARD[3])
        play = input()
        if play.upper() == WIZARD[4]:
            print(WIZARD[5])
            ready = input()
            perm = True
            var = 0
            if ready.upper() == WIZARD[6]:
                guess = choice([WIZARD[7], WIZARD[8], WIZARD[9], WIZARD[10]])
                while perm:
                    print(WIZARD[11])
                    predict = input()
                    if predict.upper() == guess.upper():
                        var += 1
                        if var < 2:
                            print(WIZARD[12])
                            dici = input()
                            if dici.upper() == WIZARD[13]:
                                perm = False
                            if dici.upper() == WIZARD[14]:
                                perm = True
                        if var == 2:
                            perm = False
                    if predict.upper() != guess.upper():
                        print(WIZARD[15])
                        var = var * 0
                        dici = input()
                        if dici.upper() == WIZARD[16]:
                            perm = False
                            print(WIZARD[17])
                        if dici.upper() == WIZARD[18]:
                            perm = True
                if var == 2:
                    print(WIZARD[19])
            if ready.upper() == WIZARD[20]:
                print(WIZARD[21])


def fish_sell():
    print(FISH_SELL[0])
    fishsell = int(input(FISH_SELL[1]))
    if State.food < fishsell:
        while fishsell > State.food:
            print(FISH_SELL[2])
            fishsell = int(input())
        State.food -= fishsell
        State.money += fishsell * 2
        print(FISH_SELL[3], fishsell)
        print(FISH_SELL[4], fishsell * 2)
    if State.food >= fishsell:
        State.food -= fishsell
        State.money += fishsell * 2
        print(FISH_SELL[5], fishsell)
        print(FISH_SELL[6], fishsell * 2)


def restart():
    State.money = 1000
    State.food = 10000
    State.people = 200
    State.population_growing = 0.01
    State.distemper = 0
    State.army = 100
    State.year = 0
    State.land = 130


# Building function.
def building():
    available_buildings = []
    for obj in State.buildings.keys():
        if not State.buildings[obj]:
            available_buildings.append(obj)
    available_message = BUILDING[0]
    for obj in available_buildings:
        available_message += obj + ', '
    available_message = available_message[:-2]
    print(available_message)
    answer = input(BUILDING[1])
    while answer not in available_buildings:
        answer = input(BUILDING[2])
    later_event(1, res_changes(answer, '+1'))


# Resource changing function.
def res_changes(*args):
    for i in range(0, len(args), 2):
        res = args[i]
        value = args[i+1][0]
        change = args[i+1][1:]
        if res == 'land':
            if value == '+':
                State.land += int(change) * State.tech_effects['land']
            else:
                State.land -= int(change)
            print(f'{RES_CHANGES[0]} {value}{change}')
        elif res == 'people':
            if value == '+':
                State.people += int(change) * State.tech_effects['people']
            else:
                State.people -= int(change)
            print(f'{RES_CHANGES[1]} {value}{change}')
        elif res == 'distemper':
            if value == '+':
                State.distemper += int(change) * State.tech_effects['distemper']
            else:
                State.distemper -= int(change)
            print(f'{RES_CHANGES[2]} {value}{change}')
        elif res == 'food':
            if value == '+':
                State.food += int(change) * State.tech_effects['food']
            else:
                State.food -= int(change)
            print(f'{RES_CHANGES[3]} {value}{change}')
        elif res == 'money':
            if value == '+':
                State.money += int(change) * State.tech_effects['money']
            else:
                State.money -= int(change)
            print(f'{RES_CHANGES[4]} {value}{change}')
        elif res == 'army':
            if value == '+':
                State.army += int(change) * State.tech_effects['army']
            else:
                State.army -= int(change)
            print(f'{RES_CHANGES[5]} {value}{change}')
        elif res in State.buildings:
            if value == '+':
                State.buildings[res] += int(change)
            print(f'{RES_CHANGES[5]} {res}')


# Postponing event function.
def later_event(*args):
    for i in range(0, len(args), 2):
        try:
            event_list = Game.turns[Game.turn + args[i]]
            event_list.append(args[i+1])
            Game.turns.update({Game.turn + args[i]: event_list})
        except KeyError:
            event_list = [args[i+1]]
            Game.turns.update({Game.turn + args[i]: event_list})


# Getting answer function.
def give_answer(text, answers):
    answer = input(text + answers + '\n')
    while answer not in ['1', '2']:
        print(f'{GIVE_ANSWER} {answers}: ')
        answer = input(text + answers + '\n')
    return answer


# Percent resource changing function.
def percent_changes(resource, percent):
    return randint(resource * 1, resource * percent) / 100


def village_fire():
    print(VILLAGE_FIRE)
    res_changes('people', f'-{int(percent_changes(State.people, 5))}',
                'food', f'-{int(percent_changes(State.food, 5))}',
                'land', f'-{int(percent_changes(State.land, 3))}',
                'distemper', f'+{int(randint(2, 10))}')


def city_fire():
    print(CITY_FIRE)
    res_changes('people', f'-{int(percent_changes(State.people, 5))}',
                'money', f'-{int(percent_changes(State.money, 5))}',
                'distemper', f'+{int(randint(2, 10))}')


def flood():
    print(FLOOD)
    res_changes('people', f'-{int(percent_changes(State.people, 5))}',
                'food', f'-{int(percent_changes(State.food, 10))}',
                'land', f'+{int(percent_changes(State.land, 4))}',
                'distemper', f'+{int(randint(2, 10))}')


def conspiracy():
    text = CONSPIRACY[0]
    answers = CONSPIRACY[1]
    answer = give_answer(text, answers)
    if answer == '1':
        res_changes('money', f'-{int(State.money * 0.2)}')
    else:
        if not randint(0, 4):
            Game.life = False


def strike():
    text = STRIKE[0]
    answers = STRIKE[1]
    answer = give_answer(text, answers)
    if answer == '1':
        res_changes('money', '-100', 'food', '-50')
    else:
        res_changes('distemper', '+10')


def plague_after():
    State.people -= 10
    print(PLAGUE_AFTER)


def plague():
    print(PLAGUE)
    for i in range(4):
        later_event(i, plague_after)
    res_changes('people', '-50')


def new_world():
    print(NEW_WORLD)


def columbus_lose():
    print(COLUMBUS_LOSE)


def columbus_win():
    print(COLUMBUS_WIN)
    res_changes('money', '+2000', 'food', '+3000',
                'land', '+50', 'distemper', '-5')


def columbus():
    text = COLUMBUS[0]
    answers = COLUMBUS[1]
    answer = give_answer(text, answers)
    if answer == '2':
        choice(later_event(4, new_world), later_event(4, columbus_lose))
        pass
    else:
        choice(later_event(4, columbus_win), later_event(4, columbus_lose))


def brilliants():
    print(BRILLIANTS)
    res_changes('money', f'+{int(str(percent_changes(State.money, 20)))}')


def forest():
    State.money += 10
    print(FOREST)


def forest_territory():
    text = FOREST_TERRITORY[0]
    answers = FOREST_TERRITORY[1]
    answer = give_answer(text, answers)
    if answer == '2':
        res_changes('distemper', '+3')
        for i in range(10):
            later_event(i, forest)
    else:
        res_changes('land', '+20', 'distemper', '-2')


def road_trade():
    State.money += 100
    later_event(1, road_trade)


def road():
    print(ROAD)
    res_changes('money', '+100')
    later_event(1, road_trade)


def winter_day():
    State.food -= 100


def cruel_winter():
    print(CRUEL_WINTER[0])
    print(CRUEL_WINTER[1])
    res_changes('food', '-100')
    for i in range(1, randint(2, 5)):
        later_event(i, winter_day)


def tournament():
    print(TOURNAMENT[0])
    State.distemper *= 0.4
    print(TOURNAMENT[1])


def elephants():
    text = ELEPHANTS[0]
    answers = ELEPHANTS[1]
    answer = give_answer(text, answers)
    if answer == '1':
        print(ELEPHANTS[2])
        res_changes('money', '-300', 'army', '+200')


def hunt():
    print(HUNT)
    res_changes('food', f'+{int(200 * State.tech_effects["meat"])}')


def parade():
    print(PARADE)
    res_changes('army', '+300', 'money', '-500')


def child():
    print(CHILD)
    Game.prince = True
    res_changes('distemper', '-5')


def indian_success():
    print(INDIAN_SUCCESS)
    res_changes('money', '+4000')


def india():
    if State.army >= 50:
        text = INDIA[0]
        answers = INDIA[1]
        answer = give_answer(text, answers)
        if answer == '1':
            res_changes('army', '-50')
            later_event(5, indian_success)
        else:
            pass
    else:
        pass


def fishing():
    answer = int(input(FISHING))
    res_changes('money', f'-{int(40 * answer)}', 'food', f'+{int(120 * answer)}')


def pirates():
    print(PIRATES)
    res_changes('money', f'-{int(0.3 * State.money)}', 'food', f'-{int(0.2 * State.food)}', 'distemper', '+3')


# def tornado():
#     to_destroy = []
#     for construction in State.buildings.keys():
#         if State.buildings[construction]:
#             to_destroy.append(construction)
#     destroyed = choice(to_destroy)
#     print(f'По вашим землям прошлось мощное торнадо, оно уничтожило: {destroyed}')
#     State.buildings[destroyed] = 0


def wonder_of_nature():
    wonders = {WONDERS[0]: ['money', '+400'], WONDERS[1]: ['food', '+2000'],
               WONDERS[2]: acknowledgement, WONDERS[3]: building,
               WONDERS[4]: ['money', '+500'], WONDERS[5]: ['distemper', '-10'],
               WONDERS[6]: ['distemper', '-10'], WONDERS[7]: ['army', '+50']}
    wonder = choice(list(wonders.keys()))
    print(f'{WONDERS[8]} {wonder}')
    if type(wonders[wonder]) == list:
        res_changes(wonders[wonder][0], wonders[wonder][1])
    else:
        wonders[wonder]()


def hero():
    heroes = HEROES
    new_hero = choice(heroes)
    print(f'{HERO} {new_hero}!')
    res_changes('army', f'+{int(State.army * 0.3)}')


def city_state():
    city_states = CITY_STATES
    new_city_state = choice(city_states)
    print(f'{CITY_STATE[0]} {new_city_state}! {CITY_STATE[1]}!')
    res_changes('land', '+20', 'people', '+10')


turn_counter = 1
life = True
while life is True:
    seed_own()
    seed_sell()
    seed_buy()
    random_events()
    if turn_counter % 2 == 1:
        if State.money >= 100:
            building()
            acknowledgement()
    random_events()
    if State.technologies.get('sailing') == 1:
        fishing()
        fish_sell()
    if State.technologies.get('cattle_breeding'):
        husbrandy()
    if State.technologies.get('hunting') == 1:
        hunt()
    if State.food / State.people <= 25 or State.people / State.land <= 2 or State.distemper >= 75:
        life = False
    else:
        pass
print(END)
exit()
