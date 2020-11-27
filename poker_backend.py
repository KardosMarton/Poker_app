#!usr/bin/python3

import yaml
import random


NR = 0


def read_yaml(yaml_file):
    with open(yaml_file) as fl:
        return yaml.safe_load(fl)


CARDS = read_yaml("cards.yaml")


def choose_one_from_cards():
    return CARDS.pop(random.randint(1, 52))


def add_random_to_list(number_list):
    random_number = random.randint(1, 52)
    if random_number not in number_list:
        number_list.append(random_number)
    else:
        add_random_to_list(number_list)


cards_ordered_list = []
for i in range(1, 52):
    add_random_to_list(cards_ordered_list)

print(cards_ordered_list)


def mix_cards():
    global cards_ordered_list, NR
    cards_ordered_list = []
    NR = 0
    for y in range(1, 52):
        add_random_to_list(cards_ordered_list)
    print(cards_ordered_list)


def get_next_card():
    global NR
    print("NR={}, cards_ordered_list[{}]={}".format(NR, NR, cards_ordered_list[NR]))
    return_value = CARDS.get(cards_ordered_list[NR])
    NR = NR + 1
    return return_value


def card_text_format(card_dictionary_value):
    return "{} of {} {}".format(card_dictionary_value["number"],
                                card_dictionary_value["color"],
                                card_dictionary_value["form"])
