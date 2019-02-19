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

def cattle_breeding():



# TODO
# Building functions.

def moulin_rouge():
    print('')
    res_changes('people', f'-{percent_changes(State.people, 3)}'
                'distemper', f'-{percent_changes(State.distemper, -20)}'
                'money', f'-{State.money, -2500}')
def church():
    price =
    print('')
    res_changes('distemper', f'-{percent_changes(State.distemper, -50)}'
                'money', f'-{percent_changes(State.money, 25)}')

def accounting_chamber():
    price =
    print('')
    res_changes('money', f'-{percent_changes(State.money, 35)}')

def windmill():
    price=
    print('')
    res_changes('seed', f'-{percent_changes(State.seed, 20)}')

def barracks():
    print('')

def

# TODO
#Technologies functions.
def

#TODO
#Cycle functions.
def random_events():
    negative_events = [village_fire(), city_fire(), flood(), conspiracy(), strike(), plague(), separatism(), war(), spy(),
                       cruel_winter(), pirates(), tornado()]
    positive_events = [discovery()]
    choice(negative_events)
    choice(positive_events)


# TODO
# Game life cycle.
turn_counter = 1

#Seed distribution.
seed_own()
seed_sell()
seed_buy()

#Random developments.
random_events()

#Building and cognition phase.
if turn_counter % 2 == 1:
    building()
    acknowledgement()

#Random developments.
random_events()

#Fishing activity.
if State.technologies.get('sailing') == 1:
    fishing()

#Hunting process.
if State.technologies.get('hunting') == 1:
    hunt()

