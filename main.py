"""
CASE_1
Developers: Anufrienko K., Kabaev A., Lankevich S.
"""

from random import randint, choice


class Game:
    turn = 0
    turns = {}
    life = True
    prince = False


# TODO
# Government object.
class State(1000, 10000, 200, 0, 0, 130):
    money = 1000
    food = 10000
    people = 200
    population_growing = 0.01
    distemper = 0
    army = 100
    year = 0
    land = 130
    tech_effects = {'money': 1, 'food': 1, 'people': 1, 'army': 1, 'land': 1, 'distemper': 1, 'seed': 1, 'meat': 1}
    buildings = {'universities': 0, }


# TODO
# Events functions. (Anton)

# TODO

# Postponing event function.
def later_event(turn_to_it, func):
    try:
        event_list = Game.turns[Game.turn + turn_to_it]
        Game.turns.update({Game.turn + turn_to_it: event_list.append(func())})
    except KeyError:
        event_list = []
        Game.turns.update({Game.turn + turn_to_it: event_list.append(func())})


# Getting answer function.
def give_answer(text, answers):
    answer = input(text + answers + '\n')
    while answer not in ['1', '2']:
        print(f'Мой король, не могли бы вы повторить {answers}: ')
    return answer


# Percent resource changing function.
def percent_changes(resource, percent):
    return randint(resource * 1, resource * percent) / 100


# Small resource change
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
            print(f'Земля: {value}{change}')
        elif res == 'people':
            if value == '+':
                State.people += int(change) * State.tech_effects['people']
            else:
                State.people -= int(change)
            print(f'Жители: {value}{change}')
        elif res == 'distemper':
            if value == '+':
                State.distemper += int(change) * State.tech_effects['distemper']
            else:
                State.distemper -= int(change)
            print(f'Смута: {value}{change}')
        elif res == 'food':
            if value == '+':
                State.food += int(change) * State.tech_effects['food']
            else:
                State.food -= int(change)
            print(f'Зерно: {value}{change}')
        elif res == 'money':
            if value == '+':
                State.money += int(change) * State.tech_effects['money']
            else:
                State.money -= int(change)
            print(f'Деньги: {value}{change}')
        elif res == 'army':
            if value == '+':
                State.army += int(change) * State.tech_effects['army']
            else:
                State.army -= int(change)
            print(f'Армия: {value}{change}')


def village_fire():
    print('Король, в одной из наших деревень произошёл пожар! Погибли жители, сгорела земля и часть зерна!')
    res_changes('people', f'-{str(percent_changes(State.people, 3))}',
                'food', f'-{str(percent_changes(State.food, 5))}',
                'land', f'-{str(percent_changes(State.land, 3))}',
                'distemper', f'+{str(randint(2, 10))}')


def city_fire():
    print('Король, в одном из наших городов произошёл пожар! Погибли жители, сгорела часть денег!')
    res_changes('people', f'-{str(percent_changes(State.people, 5))}',
                'money', f'-{str(percent_changes(State.money, 5))}',
                'distemper', f'+{str(randint(2, 10))}')


def flood():
    print('Король, произошло наводнение! Вода смыла наши посевы и унесла жизни нескольких сельчан!')
    res_changes('people', f'-{percent_changes(State.people, 5)}', 'food', f'-{percent_changes(State.food, 10)}',
                'land', f'+{percent_changes(State.land, 4)}', 'distemper', f'+{randint(2, 10)}')


def conspiracy():
    text = 'Король, против вас готовится заговор. '
    answers = 'Мы можем нанять шпиона(1), который отловит всех заговорщиков, или ждать, пока они сделают первый шаг(2)'
    answer = give_answer(text, answers)
    if answer == '1':
        res_changes('money', f'-{State.money * 0.2}')
    else:
        if not randint(0, 4):
            Game.life = False


def strike():
    text = 'Рабочие устроили забастовку.'
    answers = 'Мы можем отдать им часть денег и зерна(1) или нам придется и дальше смотреть на этот беспредел (2)'
    answer = give_answer(text, answers)
    if answer == '1':
        res_changes('money', '-100', 'food', '-50')
    else:
        res_changes('distemper', '+10')


def plague_after():
    State.people -= 10
    print('Жители: -10 (Чума)')


def plague():
    print('На юге нашего царства появилась началась какая-то эпидемия,\
     никто из наших докторов ни разу не встречался с подобным!')
    for i in range(4):
        later_event(i, plague_after())
    res_changes('people', '-50')


def new_world():
    print('Где-то в дальных землях Колумб открывает Америку!')


def columbus_lose():
    print('Экспедиция Колумба попала в шторм, никто не выжил.')


def columbus_win():
    print('Колумб достиг Америки! Экспедиция закончилась успешно! И прошла она далеко не зря: ')
    res_changes('money', '+2000', 'food', '+3000',
                'land', '+50', 'distemper', '-5')


def columbus():
    text = 'Какой-то бродяга с улицы по имени Колумб собирает средства на экспедицию для\
     поиска нового пути в Индию, милорд.\n Он просит вас проспонсировать его,\
      ему нужно 50 золота: '
    answers = '(1 - дать; 2 - отказаться)'
    answer = give_answer(text, answers)
    if answer == '2':
        choice(later_event(4, new_world()), later_event(4, columbus_lose()))
        pass
    else:
        choice(later_event(4, columbus_win()), later_event(4, columbus_lose()))


def brilliants():
    print('Ваши подданые нашли пещеру с бриллиантами!')
    res_changes('money', f'+{str(percent_changes(State.money, 20))}')


def forest():
    State.money += 10
    print('Деньги: +10 (Лес)')


def forest_territory():
    text = 'Сельчане просят ваше разрешение на срубку леса, чтобы построить себе новые дома'
    answers = '(1 - дать разрешение, 2 - оставить лес)'
    answer = give_answer(text, answers)
    if answer == '2':
        res_changes('distemper', '+3')
        for i in range(10):
            later_event(i, forest())
    else:
        res_changes('land', '+20', 'distemper', '-2')


def road_trade():
    State.money += 100
    later_event(1, road_trade())


def road():
    print('Наши рабочие построили Золотой путь!(+100 к золоту каждый ход)')
    res_changes('money', '+100')
    later_event(1, road_trade())


def winter_day():
    State.food -= 100


def winter():
    print('Началась зима')
    print('Мы будем терять 100 единиц зерна каждый ход до её окончания')
    res_changes('food', '-100')
    for i in range(1, randint(2, 5)):
        later_event(i, winter_day())


def tournament():
    print('Начался ежегодный рыцарский турнир в вашу честь! Это большой праздник для всего вашего королевства!')
    State.distemper *= 0.4
    print('Смута сбрасывается до 40% от текущей')


def expo():
    print('Учёные всех королевств решили провести научную выставку в нашей столице.')
    State.buildings['universities'] += 1


def elephants():
    text = 'Торговец из Кении предлагает вам купить африканских слонов за 200 монет.'
    answers = '(1 - купить, 2 - и коней хватит)'
    answer = give_answer(text, answers)
    if answer == '1':
        print('Отличные слоны!')
        res_changes('money', '-300', 'army', '+200')


def hunt():
    print('Охота:')
    res_changes('food', f'+{200 * State.tech_effects["meat"]}')


def parade():
    print('Парад в столице')
    res_changes('army', '+300', 'money', '-500')


def child():
    print('Поздравляю с рождением принца, мой король!')
    Game.prince = True
    res_changes('distemper', '-5')


def indian_success():
    print('Вернулась экспедиция из Индии!!!')
    res_changes('money', '+4000')


def india():
    if State.army >= 50:
        text = 'Купцы хотят отправиться в Индию,\
         но для путешествия им нужно сопровождение,\
          они просят у вас часть армии (50 войнов). '
        answers = '(1) - отправить войнов. (2) - отказаться от предложения.'
        answer = give_answer(text, answers)
        if answer == '1':
            res_changes('army', '-50')
            later_event(5, indian_success())
        else:
            pass
    else:
        pass

# TODO
# Events functions. (Sergey)

# TODO
# Game life cycle.
