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
    state.seed -= am_to_seat
    print('Король, сколько зерна раздать людям?')
    am_to_give = int(input())
    state.seed -= am_to_give
    if 1000 <= am_to_give < 2500 and state.people < 300:
        state.people = state.people * 1.05
    if 2500 <= am_to_give < 5000 and state.people < 300:
        state.people = state.people * 1.1
    if am_to_give >= 5000 and state.people < 300:
        state.people = state.people * 1.15
    if 1000 <= am_to_give < 2500 and state.people >= 300:
        state.people = state.people * 1.03
    if 2500 <= am_to_give < 5000 and state.people >= 300:
        state.people = state.people * 1.05
    if am_to_give >= 5000 and state.people >= 300:
        state.people = state.people * 1.08
    af_event_1 = 'Год был не урожайным, мы  выростили мало.'
    af_event_2 = 'Просто замечательный сезон, мы вырастили в двое больше!'
    af_event_3 = 'Хороший урожай, милорд.'
    af_event_4 = 'Ужасный урожай, милорд. Мы не вырастили ничего!'
    ev_all = []
    ev_all.append(af_event_4)
    ev_all.append(af_event_1)
    ev_all.append(af_event_2)
    ev_all.append(af_event_3)
    ev_r = random.choice(ev_all)
    if ev_r == af_event_1:
        print(af_event_1)
        state.seed += am_to_seat * 0.75
    elif ev_r == af_event_2:
        print(af_event_2)
        state.seed += am_to_seat * 2
    elif ev_r == af_event_3:
        print(af_event_3)
        state.seed += am_to_seat * 1.5
    elif ev_r == af_event_4 and state.people > 300 and state.seed < 5000:
        print(af_event_4)
        state.people = state.people * 0.85
        print('Такими темпами в стране начнется голод!')
    elif ev_r == af_event_4 and (state.seed >= 5000 or state.people < 300):
        print(af_event_4)
        pass
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(state.money,
                                                                                           state.seed, state.people,
                                                                                           state.distemper, state.year,
                                                                                           state.land))

    def seed_sell():
    print('Король, соседнее государство хочет купить зерно(2 буша за зернышко). Сколько продать?')
    am_sell = int(input())
    state.seed -= am_sell
    state.money += am_sell * 2
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(state.money,
                                                                                           state.seed, state.people,
                                                                                           state.distemper, state.year,
                                                                                           state.land))


def seed_buy():
    print('Король, соседнее государство готово продать зерно(2 буша за зернышко). Сколько купить?')
    am_buy = int(input())
    state.seed += am_buy
    state.money -= am_buy * 2
    print('Money: {} | Seed: {} | People: {} | Distemper: {} | Year: {} | Land: {}'.format(state.money,
                                                                                           state.seed, state.people,
                                                                                           state.distemper, state.year,
                                                                                           state.land))

# TODO
# Game life cycle.
