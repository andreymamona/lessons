# Написать функцию, которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
# где на первом месте номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти
# (Hearts, Diamonds, Clubs, Spades).
import random
card_nominal = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
card_type = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_cost = [6, 7, 8, 9, 10, 2, 3, 4, 11]


def make_list_of_cards (c_nom, c_type, c_cost):
    tmp_list = []
    list_of_cards = {}
    for i in c_type:
        for j in c_nom:
            tmp_list.append(j+' '+i)
    for y in range(len(tmp_list)):
        if y < 9:
            t = y
        else: t = y % 9
        list_of_cards[tmp_list[y]] = c_cost[t]
    return list_of_cards


work_list = make_list_of_cards(card_nominal, card_type, card_cost)
print(work_list)
random.shuffle(work_list)
print(work_list)
