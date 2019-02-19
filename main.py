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
        available_message = 'Доступны для изучения: '
        for obj in available_technologies:
            available_message += obj + ', '
        available_message = available_message[:-2]
        print(available_message)
        answer = input('Выберите технологию для изучения: ')
        while answer not in available_technologies:
            answer = input('Введите корректное название ремесла: ')
        later_event(2, res_changes(answer, '+1'))
    if turn_counter > 4:
        for obj in State.technologies.keys():
            if not State.technologies[obj]:
                available_technologies.append(obj)
        available_message = 'Доступны для изучения: '
        for obj in available_technologies:
            available_message += obj + ', '
        available_message = available_message[:-2]
        print(available_message)
        answer = input('Выберите технологию для изучения: ')
        while answer not in available_technologies:
            answer = input('Введите корректное название ремесла: ')
        later_event(2, res_changes(answer, '+1'))
        later_event(2, answer)

# TODO
# Building functions.


def moulin_rouge():
    print('Увеселительное кабарэ для молодых и взрослых бизнес-информатиков и бизнес-информатичек, где можно отдохнуть и телом и душой!')
    res_changes('people', f'+{int((percent_changes(State.people, 3)))}'
                'distemper', f'-{int(percent_changes(State.distemper, 30))}'
                'money', f'-500')
def church():
    print('Церковь построена, милорд!')
    res_changes('distemper', f'-{(percent_changes(State.distemper, 50))}'
                'money', f'-2000')

def accounting_chamber():
    print('Теперь у вас есть счетная палата.')
    res_changes('money', f'+{int(percent_changes(State.money, 35))}')

def windmill():
    print('Мельница готова, король!')
    res_changes('food', f'+{int(percent_changes(State.food, 20))}')
    res_changes('money', f'-{int(percent_changes(State.money, 50))}')

def barracks():
    print('Казармы готовы, Ваше Величество')
    res_changes('money', f'-600')
    res_changes('army', f'+{int(percent_changes(State.army, 35))}')


# TODO
#Technologies functions.
def cattle_breeding():
    print('Вы изучили скотоводство, теперь вы будете получать больше еды')
    State.tech_effects.update({'food': 1.25})
    State.money -= 400

def agriculture():
    print('Вы изучили земеледелие, теперь вы будете получать больше еды.')
    State.tech_effects.update({'food': 1.25})
    State.money -= 400
def sailing():
    print('Вы изучили мореходство. Теперь вы можете ловить рыбу и торговать ей! У вас также появились военные корабли.')
    State.tech_effects.update({'food': 1.25})
    State.tech_effects.update({'army': 1.15})
    State.money -= 400
def hunting():
    print('Вы познали искусство охоты. Бизнес информатики будут добывать для вас мясо!')
    State.tech_effects.update({'food': 2})
    State.money -= 400
def warfare():
    print('Вы постигли новых высот в военном деле, поздравляю мой государь!')
    State.buildings.update({'Казармы': 0})
    State.tech_effects.update({'army': 1.33})
    State.money -= 400
def religion():
    print('Вы приняли религию, теперь можете построить церковь. Это существенно сократит протестные настроения в стране.')
    State.buildings.update({'Church': 0})
    State.money -= 400
def masonry():
    print('Вы изучили каменную кладку. Вам доступны новые постройки и ресурсы.')
    State.buildings.update({'The Great Wall': 0})
    State.money -= 400
def rivalry():
    print('Честь, отвага и благородие отныне не чужды бизнес информатикам. Ожидайте турниры в вашу честь!')
    State.tech_effects.update({'army': 1.5})
    State.money -= 400


#TODO
#Cycle functions.

def random_events():
    negative_events = [village_fire, city_fire, flood, conspiracy, strike, plague, separatism, war, spy,
                       cruel_winter, pirates, tornado]
    positive_events = [discovery, road, hero, wonder_of_nature, forest_territory, city_state]
    if State.technologies.get('masonry') == 1:
        positive_events.append(brilliants)
    if State.technologies.get('rivalry') == 1:
        positive_events.append(tournament)
    choice(negative_events)
    choice(positive_events)


# TODO
# Events functions. (Anton)
def output():
    print('Деньги: {} | Зерно: {} | Народ: {} | Смута: {} '
          '| Год: {} | Замля: {} | Еда: {} | Армия: {}'.format(State.money, 
                                                               State.food, State.people, State.distemper,
                                                               State.year, State.land, State.food, State.army))
    


def seed_own():
    print('Король, сколько зерна песеять?')
    am_to_seat = int(input())
    State.food -= am_to_seat
    print('Король, сколько зерна раздать людям?')
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
    af_event_1 = 'Год был не урожайным, мы  выростили мало.'
    af_event_2 = 'Просто замечательный сезон, мы вырастили в двое больше!'
    af_event_3 = 'Хороший урожай, милорд.'
    af_event_4 = 'Ужасный урожай, милорд. Мы не вырастили ничего!'
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
        print('Такими темпами в стране начнется голод!')
        print('Смута + 5')
    elif ev_r == af_event_4 and (State.food >= 5000 or State.people < 300):
        pass


def seed_sell():
    print('Король, соседнее государство хочет купить зерно(2 золотых за зернышко). Сколько продать?')
    am_sell = int(input())
    if State.food < am_sell:
        while am_sell > State.food:
            print('Не хватает зерна.')
            am_sell = int(input())
        State.food -= am_sell
        State.money += am_sell * 2
    if State.food >= am_sell:
        State.food -= am_sell
        State.money += am_sell * 2


def seed_buy():
    print('Король, соседнее государство готово продать зерно(2 золотых за зернышко). Сколько купить?')
    am_buy = int(input())
    if State.money < am_buy * 2:
        while am_buy * 2 > State.money:
            print('Не хватает денег.')
            am_buy = int(input())
        State.food += am_buy
        State.money -= am_buy * 2
    if State.money >= am_buy * 2:
        State.food += am_buy
        State.money -= am_buy * 2


def war():
    event = 'Король Испании развязал войну на Севере.Он просит Вас принять участие в ней на его стороне. '\
           'Желаете принять участие? (30 солдат, 5 000 золотых).В случае победы Испания обещает вам 12 000 золотых.'
    print(event)
    answ_w = input()
    if answ_w.upper() == 'ДА' and State.money >= 5000 and State.army >= 30:
        State.money -= 5000
        State.army -= 30
    elif answ_w.upper() == 'НЕТ':
        pass
    elif answ_w.upper() == 'ДА' and (State.money < 5000 or State.army < 30):
        print('Король, у Вас недостаточно ресурсов.')
    later_event(1, war_exodus)


def war_exodus():
        event_af1 = 'Испанский Король проиграл войну.'
        event_af2 = 'Испания побеждает в войне!!!'
        con_war = choice([event_af1, event_af2])
        print(con_war)
        if con_war == event_af1:
            print('Нашему государству ничего не достанется, Кололь.')
            print('Смута + 3')
            State.distemper += 3
        if con_war == event_af2:
            print('В казну поступили обещанные 12 000 золотых. Из 100 солдат выжило только 25.')
            State.money += 12000
            State.army += 25


def separatism():
    print('Король, Северное графство выступило против Вас и хочет отделиться? Отправить войска?')
    answr = input()
    evi_1 = 'Восстание подавлено!'
    evi_2 = 'Нам не удалось подавить сепаратистов...'
    if answr.upper() == 'ДА':
        print('Сколько людей отправить?')
        army = int(input())
        if State.army >= army:
            State.army -= army
        if State.army < army:
            while army > State.army:
                print('Не хватает солдат.')
                army = int(input())
            State.army -= army
        if army < 20:
            print(evi_2, 'Ни один солдат не вернулся.')
            State.land -= 30
            State.people -= 15
            State.army -= army
            State.distemper += 3
            print('Замля - 30')
            print('Народ - 15')
            print('Army - ', army)
            print('Смута + 3')
        if army >= 20:
            print(evi_1)
    if answr.upper() == 'НЕТ':
        State.land -= 30
        State.people -= 15
        print('Замля - 30')
        print('Народ - 15')


def discovery():
    print('Король, наши ученые предлагают отправить экспедицию на Юг(10 человек). Дадите свое согласие и'
          ' средства(1 000 золотых)')
    answer = input()
    if answer.upper() == 'ДА' and State.money >= 1000 and State.people >= 10:
        State.money -= 1000
        State.people -= 10
        print('Деньги - 1 000')
        print('Народ - 10')
    if answer.upper() == 'НЕТ':
        pass
    ev_1_ = 'Король, экспедиционный корпус вернулся с открытиями и ресурсами!'
    ev_2_ = 'Король, нмикто не вернулся из экспедиции.'
    d_exodus = choice([ev_1_, ev_2_])
    if d_exodus == ev_1_:
        print(ev_1_)
        State.food += 420
        State.land += 40
        State.people += 10
        if State.distemper >= 10:
            State.distemper -= 10
            print("Смута - 10")
        print('Зерно + 420')
        print('Замля + 40')
    if d_exodus == ev_2_:
        print('Король, экспедиционый корпус не вернулся')


def spy():
    print('Король, до нас доли слухи, что в стране есть шпионы. Усилить гарнизон? (320 золотых?)')
    ans = input()
    if ans.upper() == 'ДА':
        catch = "Шпион пойман! Мы смогли предовратить диверсию!"
        lose = 'Слухи остаются слухами.'
        d_yes = choice([catch, lose])
        if d_yes == catch:
            print(catch)
            State.distemper -= 3
            print('Смута - 3')
            print('Деньги - 320')
        if d_yes == lose:
            print('Деньги - 320')
    if ans.upper() == 'НЕТ':
        lose_1 = 'Слухи оказались правдой. Шпион ограбил казну и убил несколько придворных.'
        bad_l = 'Слухи остаются слухами.'
        d_no = choice([bad_l, lose_1])
        if d_no == lose_1:
            print(lose_1)
            State.distemper += 13
            State.money -= 520
            print('Смута + 13')
            print('Деньги - 520')


def husbrandy():
    print('Король, сколько земли выделить для выпаски скота?')
    dision = int(input())
    if dision <= State.land:
        State.land -= dision
        State.food += dision * 10
        print('Замля -', dision)
        print('Еда + ', dision * 10)
    if dision > State.land:
        while dision > State.land:
            dision = int(input())
        State.land -= dision
        State.food += dision * 10
        print('Замля -', dision)
        print('Еда + ', dision * 10)


def wizard():
    print("Король, у входа в дворец стоит странник. Он называет себя чародеем и просит встречи с Вашим высочеством. "
          "Нам впустить его?")
    chose = input()
    if chose.upper() == 'ДА':
        print('Чародей: Здравствуйте Король, давайте сыграем  в одну игру?')
        print('*Ваш ответ Король*:')
        play = input()
        if play.upper() == 'ДА':
            print('Чародей: Я загадываю одно слово из: Дракон, Рыцарь, Меч, Огонь. А вы должни отгадать. \n '
                  'Если победите подряд два раза, одним щелчком пальцев  решу ваши проблемы в стране, но за каждый '
                  'проигрыш отдаете мне 50 золотых. Вы готовы? \n (Введите да или нет)')
            ready = input()
            perm = True
            var = 0
            if ready.upper() == 'ДА':
                guess = choice(['Дракон', 'Рыцарь', 'Меч', 'Огонь'])
                while perm:
                    print('Я загадал. Ваш ответ.')
                    predict = input()
                    if predict.upper() == guess.upper():
                        var += 1
                        if var < 2:
                            print('Правильно. Идем дальше?')
                            dici = input()
                            if dici.upper() == 'НЕТ':
                                perm = False
                            if dici.upper() == 'ДА':
                                perm = True
                        if var == 2:
                            perm = False
                    if predict.upper() != guess.upper():
                        print('Увы, вы ошиблись. Идем дальше?')
                        var = var * 0
                        dici= input()
                        if dici.upper() == 'НЕТ':
                            perm = False
                            print('До встречи, Король.')
                        if dici.upper() == 'ДА':
                            perm = True
                if var == 2:
                    print('Кажется вы победили, Король. Вот Ваш приз.')
            if ready.upper() == 'НЕТ':
                print('До встречи, Король.')


def fish_sell():
    print('Король, царь соседнего госудаоства готов купить у нас немного рыбы. (2 ве золотых за штуку.')
    fishsell = int(input('Сколько рыбы прождать?:'))
    if State.food < fishsell:
        while fishsell > State.food:
            print('Не хватает рыбы. Введите другое значение.')
            fishsell = int(input())
        State.food -= fishsell
        State.money += fishsell * 2
        print('Еда -', fishsell)
        print('Деньги +', fishsell * 2)
    if State.food >= fishsell:
        State.food -= fishsell
        State.money += fishsell * 2
        print('Еда -', fishsell)
        print('Деньги +', fishsell * 2)

# TODO
# Game restart function.
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
    available_message = 'Вы можете построить: '
    for obj in available_buildings:
        available_message += obj + ', '
    available_message = available_message[:-2]
    print(available_message)
    answer = input('Введите название постройки: ')
    while answer not in available_buildings:
        answer = input('Введите корректное название постройки: ')
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
        elif res in State.buildings:
            if value == '+':
                State.buildings[res] += int(change)
            print(f'Вы построили: {res}')


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
        print(f'Мой король, не могли бы вы повторить {answers}: ')
        answer = input(text + answers + '\n')
    return answer


# Percent resource changing function.
def percent_changes(resource, percent):
    return randint(resource * 1, resource * percent) / 100


def village_fire():
    print('Король, в одной из наших деревень произошёл пожар! Погибли жители, сгорела земля и часть зерна!')
    res_changes('people', f'-{int(percent_changes(State.people, 5))}',
                'food', f'-{int(percent_changes(State.food, 5))}',
                'land', f'-{int(percent_changes(State.land, 3))}',
                'distemper', f'+{int(randint(2, 10))}')


def city_fire():
    print('Король, в одном из наших городов произошёл пожар! Погибли жители, сгорела часть денег!')
    res_changes('people', f'-{int(percent_changes(State.people, 5))}',
                'money', f'-{int(percent_changes(State.money, 5))}',
                'distemper', f'+{int(randint(2, 10))}')


def flood():
    print('Король, произошло наводнение! Вода смыла наши посевы и унесла жизни нескольких сельчан!')
    res_changes('people', f'-{int(percent_changes(State.people, 5))}',
                'food', f'-{int(percent_changes(State.food, 10))}',
                'land', f'+{int(percent_changes(State.land, 4))}',
                'distemper', f'+{int(randint(2, 10))}')


def conspiracy():
    text = 'Король, против вас готовится заговор. '
    answers = 'Мы можем нанять шпиона(1), который отловит всех заговорщиков, или ждать, пока они сделают первый шаг(2)'
    answer = give_answer(text, answers)
    if answer == '1':
        res_changes('money', f'-{int(State.money * 0.2)}')
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
        later_event(i, plague_after)
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
        choice(later_event(4, new_world), later_event(4, columbus_lose))
        pass
    else:
        choice(later_event(4, columbus_win), later_event(4, columbus_lose))


def brilliants():
    print('Ваши подданые нашли пещеру с бриллиантами!')
    res_changes('money', f'+{int(str(percent_changes(State.money, 20)))}')


def forest():
    State.money += 10
    print('Деньги: +10 (Лес)')


def forest_territory():
    text = 'Сельчане просят ваше разрешение на срубку леса, чтобы построить себе новые дома '
    answers = '(1 - дать разрешение, 2 - оставить лес) '
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
    print('Наши рабочие построили Золотой путь!(+100 к золоту каждый ход)')
    res_changes('money', '+100')
    later_event(1, road_trade)


def winter_day():
    State.food -= 100


def cruel_winter():
    print('Началась зима')
    print('Мы будем терять 100 единиц зерна каждый ход до её окончания')
    res_changes('food', '-100')
    for i in range(1, randint(2, 5)):
        later_event(i, winter_day)


def tournament():
    print('Начался ежегодный рыцарский турнир в вашу честь! Это большой праздник для всего вашего королевства!')
    State.distemper *= 0.4
    print('Смута сбрасывается до 40% от текущей')


def expo():
    print('Учёные всех королевств решили провести научную выставку в нашей столице.')
    State.buildings['universities'] += 1


def elephants():
    text = 'Торговец из Кении предлагает вам купить африканских слонов за 200 монет. '
    answers = '(1 - купить, 2 - и коней хватит) '
    answer = give_answer(text, answers)
    if answer == '1':
        print('Отличные слоны!')
        res_changes('money', '-300', 'army', '+200')


def hunt():
    print('Охота:')
    res_changes('food', f'+{int(200 * State.tech_effects["meat"])}')


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
        answers = '(1) - отправить войнов. (2) - отказаться от предложения. '
        answer = give_answer(text, answers)
        if answer == '1':
            res_changes('army', '-50')
            later_event(5, indian_success)
        else:
            pass
    else:
        pass


def fishing():
    answer = int(input('Рыбалка (1 лодка: -40 золота, +120 еды) (Сколько лодок вы хотите купить): '))
    res_changes('money', f'-{int(40 * answer)}', 'food', f'+{int(120 * answer)}')


def pirates():
    print('Пираты напали на наши торговые суда!')
    res_changes('money', f'-{int(0.3 * State.money)}', 'food', f'-{int(0.2 * State.food)}', 'distemper', '+3')


def tornado():
    to_destroy = []
    for construction in State.buildings.keys():
        if State.buildings[construction]:
            to_destroy.append(construction)
    destroyed = choice(to_destroy)
    print(f'По вашим землям прошлось мощное торнадо, оно уничтожило: {destroyed}')
    State.buildings[destroyed] = 0


def wonder_of_nature():
    wonders = {'"Большое плато"': ['money', '+400'], 'озеро "Виктория"': ['food', '+2000'],
               '"Большой барьерный риф"': 'acknoledgment', '"Копи царя Соломона"': building,
               '"Эльдорадо"': ['money', '+500'], '"Источник молодости"': ['distemper', '-10'],
               '"Гибралтар"': ['distemper', '-10'], 'гора "Фудзиями"': ['army', '+50']}
    wonder = choice(list(wonders.keys()))
    print(f'Вы обнарушили чудо природы: {wonder}')
    if type(wonders[wonder]) == list:
        res_changes(wonders[wonder][0], wonders[wonder][1])
    else:
        wonders[wonder]()


def hero():
    heroes = ['Чингисхан', 'Тамерлан', 'Наполеон', 'Юлий Цезарь', 'Георгий Жуков', 'Александр Невский']
    new_hero = choice(heroes)
    print(f'У вас в армии появляется великий полководец {new_hero}!')
    res_changes('army', f'+{int(State.army * 0.3)}')


def city_state():
    city_states = ['Сингапур', 'Монако', 'Ватикан', 'Гонконг', 'Макао']
    new_city_state = choice(city_states)
    print(f'Вы нашли город-государство {new_city_state}! Его жители присягают вам на веру!')
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
print('Ваше правление не назовешь успешным, народ бизнес-информатиков не хочет более видеть столь беспомощного правителя...')
exit()
