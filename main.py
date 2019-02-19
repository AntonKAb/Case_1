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
        later_event(2, answer)

# TODO
# Building functions.

def moulin_rouge():
    print('Увеселительное кабарэ для молодых и взрослых бизнес-информатиков и бизнес-информатичек, где можно отдохнуть и телом и душой!')
    res_changes('people', f'-{percent_changes(State.people, 3)}'
                'distemper', f'-{percent_changes(State.distemper, -20)}'
                'money', f'-{State.money, -500}')
def church():
    print('Церковь построена, милорд!')
    res_changes('distemper', f'-{percent_changes(State.distemper, -30)}'
                'money', f'-{percent_changes(State.money, -250)}')

def accounting_chamber():
    print('Теперь у вас есть счетная палата.')
    res_changes('money', f'-{percent_changes(State.money, 35)}')

def windmill():
    print('Мельница готова, король!')
    res_changes('seed', f'-{percent_changes(State.seed, 20)}')
    res_changes('money', f'-{percent_changes(State.money -50)}')
def barracks():
    print('')

def

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
    State.tech_effects.update({'army': 1.33})
    State.money -= 400
def religion():
    print('Вы приняли религию, теперь можете построить церковь. Это существенно сократит протестные настроения в стране.')
    State.buildings.update({'Church': 0})
    State.money -= 400
def masonry():
    print('Вы изучили каменную кладку. Вам доступны новые постройки и ресурсы.')
    State.buildings.update({'The Great Wall'})
    State.money -= 400
def rivalry():
    print('Честь, отвага и благородие отныне не чужды бизнес информатикам. Ожидайте турниры в вашу честь!')
    State.tech_effects.update({'army': 1.5})
    Start.money -= 400


#TODO
#Cycle functions.
def random_events():
    negative_events = [village_fire(), city_fire(), flood(), conspiracy(), strike(), plague(), separatism(), war(), spy(),
                       cruel_winter(), pirates(), tornado()]
    positive_events = [discovery(), road(), forest_territory()]
    if State.technologies.get('masonry') == 1:
        positive_events.append(brilliants)
    if State.technologies.get('rivalry') == 1:
        positive_events.append(tournament)
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
    if money >= 100:
    building()
    acknowledgement()

#Random developments.
random_events()

#Fishing activity.
if State.technologies.get('sailing') == 1:
    fishing()
    fish_sell()


#Hunting process.
if State.technologies.get('hunting') == 1:
    hunt()

