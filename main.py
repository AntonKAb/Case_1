"""
CASE_1
Developers: Anufrienko K., Kabaev A., Lankevich S.
"""

# TODO
# Government object.
class state:
    money = 1000
    seed = 10000
    people = 200
    distemper = 0
    year = 0
    land = 130

# TODO
# Events functions.
def seed_own():
    print('Король, сколько зерна песеять?')
    am_to_seat = int(input())
    State.seed -= am_to_seat
    print('Король, сколько зерна раздать людям?')
    am_to_give = int(input())
    State.seed -= am_to_give
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
    ev_r = random.choice(ev_all)
    if ev_r == af_event_1:
        State.seed += am_to_seat * 0.75
    elif ev_r == af_event_2:
        State.seed += am_to_seat * 2
    elif ev_r == af_event_3:
        State.seed += am_to_seat * 1.5
    elif ev_r == af_event_4 and State.people > 300 and State.seed < 5000:
        State.people = State.people * 0.85
        State.distemper += 2
        print('Такими темпами в стране начнется голод!')
        print('Distemper + 2')
    elif ev_r == af_event_4 and (State.seed >= 5000 or State.people < 300):
        pass
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper, State.year,
                                                                                           State.land))


def seed_sell():
    print('Король, соседнее государство хочет купить зерно(2 золотых за зернышко). Сколько продать?')
    am_sell = int(input())
    if State.seed < am_sell:
        while am_sell > State.seed:
            print('Не хватает зерна.')
            am_sell = int(input())
        State.seed -= am_sell
        State.money += am_sell * 2
    if State.food >= am_sell:
        State.seed -= am_sell
        State.money += am_sell * 2

    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper, State.year,
                                                                                           State.land))


def seed_buy():
    print('Король, соседнее государство готово продать зерно(2 золотых за зернышко). Сколько купить?')
    am_buy = int(input())
    if State.money < am_buy * 2:
        while am_buy * 2 > State.money:
            print('Не хватает денег.')
            am_buy = int(input())
        State.seed += am_buy
        State.money -= am_buy * 2
    if State.money >= am_buy * 2:
        State.seed += am_buy
        State.money -= am_buy * 2
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper, State.year,
                                                                                           State.land))


def war():
    event = 'Король Испании развязал войну на Севере.Он просит Вас принять участие в ней на его стороне. '\
           'Желаете принять участие? (100 солдат, 5 000 золотых).В случае победы Испания обещает вам 12 000 золотых.'
    print(event)
    answ_w = input()
    if answ_w.upper() == 'ДА' and State.money >= 10000 and State.people >= 100:
        State.money -= 5000
        State.people -= 100
    elif answ_w.upper() == 'НЕТ':
        pass
    elif answ_w.upper() == 'ДА' and (State.money < 10000 or State.people < 100):
        print('Король, у Вас недостаточно ресурсов.')
        return answ_w
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper,
                                                                                           State.year,
                                                                                           State.land))


def war_exodus(answ_w):
        event_af1 = 'Испанский Король проиграл войну.'
        event_af2 = 'Испания побеждает в войне!!!'
        con_war = random.choice([event_af1, event_af2])
        print(con_war)
        if con_war == event_af1:
            print('Нашему государству ничего не достанется, Кололь.')
        if con_war == event_af2:
            print('В казну поступили обещанные 12 000 золотых. Из 100 солдат выжило только 25.')
            State.money += 12000
            State.people += 25
        print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper, State.year,
                                                                                           State.land))


def separatism():
    print('Король, Северное графство выступило против Вас и хочет отделиться? Отправить войска?')
    answr = input()
    evi_1 = 'Восстание подавлено!'
    evi_2 = 'Нам не удалось подавить сепаратистов...'
    if answr.upper() == 'ДА':
        print('Сколько людей отправить?')
        army = int(input())
        if State.people >= army:
            State.people -= army
        if State.people < army:
            while army > State.people:
                print('Не хватает людей.')
                army = int(input())
            State.people -= army
        if army < 20:
            print(evi_2, 'Ни один солдат не вернулся.')
            State.land -= 30
            State.people -= 20
            State.distemper += 3
            print('Land - 30')
            print('People - 20 -', army)
            print('Distemper + 3')
        if army >= 20:
            print(evi_1)
    if answr.upper() == 'НЕТ':
        State.land -= 30
        State.people -= 20
        print('Land - 30')
        print('People - 20')
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper, State.year,
                                                                                           State.land))


def discovery():
    print('Король, наши ученые предлагают отправить экспедицию на Юг(10 человек). Дадите свое согласие и'
          ' средства(1 000 золотых)')
    answer = input()
    if answer.upper() == 'ДА' and State.money >= 1000 and State.people >= 10:
        State.money -= 1000
        State.people -= 10
        print('Money - 1 000')
        print('People - 10')
    if answer.upper() == 'НЕТ':
        pass
    ev_1_ = 'Король, экспедиционный корпус вернулся с открытиями и ресурсами!'
    ev_2_ = 'Король, нмикто не вернулся из экспедиции.'
    d_exodus = random.choice([ev_1_, ev_2_])
    if d_exodus == ev_1_:
        print(ev_1_)
        State.seed += 420
        State.land += 40
        State.people += 10
        if State.distemper >= 3:
            State.distemper -= 3
            print("Distemper - 3")
        print('Seed + 420')
        print('Land + 40')
    if d_exodus == ev_2_:
        print('Король, экспедиционый корпус не вернулся')
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper, State.year,
                                                                                           State.land))


def spy():
    print('Король, до нас доли слухи, что в стране есть шпионы. Усилить гарнизон? (320 золотых?)')
    ans = input()
    if ans.upper() == 'ДА':
        catch = "Шпион пойман! Мы смогли предовратить диверсию!"
        lose = 'Слухи остаются слухами.'
        d_yes = random.choice([catch, lose])
        if d_yes == catch:
            print(catch)
            State.distemper -= 3
            print('Distemper - 3')
            print('Money - 320')
        if d_yes == lose:
            print('Money - 320')
    if ans.upper() == 'НЕТ':
        lose_1 = 'Слухи оказались правдой. Шпион ограбил казну и убил несколько придворных.'
        bad_l = 'Слухи остаются слухами.'
        d_no = random.choice([bad_l, lose_1])
        if d_no == lose_1:
            print(lose_1)
            State.distemper += 3
            State.money -= 520
            print('Distemper + 3')
            print('Money - 520')
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(State.money,
                                                                                           State.seed, State.people,
                                                                                           State.distemper, State.year,
                                                                                           State.land))


def husbrandy():
    print('Король, сколько земли выделить для выпаски скота?')
    dision = int(input())
    if dision <= State.land:
        State.land -= dision
        State.food += dision * 50
        print('Land -', dision)
        print('Food + ', dision * 50)
    if dision > State.land:
        while dision > State.land:
            dision = int(input())
        State.land -= dision
        State.food += dision * 50
        print('Land -', dision)
        print('Food + ', dision * 50)

# TODO
# Game life cycle.
