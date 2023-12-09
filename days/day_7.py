""" Day 7: Camel Cards

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from collections import Counter

CARDS = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A', '9': '9', '8': '8', '7': '7', '6': '6', '5': '5', '4': '4',
         '3': '3', '2': '2'}


# modules
def mapping_from_cards_to_alphabet(line: tuple, j_as_jokers: bool = False) -> tuple:
    """ Mapping from given line to alphabetic line to help sorted()

    :param j_as_jokers: boolean parameter for specific mapping for J
    :param line: line from input list
    :return: remapped line
    """
    cards, bid = line
    str_list = list(cards)
    remapped_line = []
    for ch in str_list:
        if ch == 'J' and j_as_jokers:
            remapped_line.append('1')
        else:
            remapped_line.append(CARDS[ch])
    return ''.join(remapped_line), bid


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 7th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    results = {
        # result: [(cards, bid), ...]
        'Five of a kind': [],
        'Four of a kind': [],
        'Full house': [],
        'Three of a kind': [],
        'Two pair': [],
        'One pair': [],
        'High card': [],
    }
    remapped_input_list = [mapping_from_cards_to_alphabet(line) for line in input_list]
    for hand in remapped_input_list:
        cards, _ = hand
        count = dict(Counter(cards))
        if 5 in count.values():
            current_point = 'Five of a kind'
        elif 4 in count.values():
            current_point = 'Four of a kind'
        elif 3 in count.values() and 2 in count.values():
            current_point = 'Full house'
        elif 3 in count.values():
            current_point = 'Three of a kind'
        elif 2 in count.values():
            number_of_pairs = list(filter(lambda x: (x == 2), count.values()))
            if len(number_of_pairs) == 2:
                current_point = 'Two pair'
            else:
                current_point = 'One pair'
        else:
            current_point = 'High card'
        results[current_point].append(hand)
        results[current_point] = sorted(results[current_point], key=lambda x: (x[0]))
    all_hands = []
    all_hands.extend(results['High card'])
    all_hands.extend(results['One pair'])
    all_hands.extend(results['Two pair'])
    all_hands.extend(results['Three of a kind'])
    all_hands.extend(results['Full house'])
    all_hands.extend(results['Four of a kind'])
    all_hands.extend(results['Five of a kind'])
    final_sum = 0
    for rank, hand in enumerate(all_hands):
        _, bid = hand
        final_sum += (rank + 1) * bid
    return final_sum


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 7th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    results = {
        # result: [(cards, bid), ...]
        'Five of a kind': [],
        'Four of a kind': [],
        'Full house': [],
        'Three of a kind': [],
        'Two pair': [],
        'One pair': [],
        'High card': [],
    }
    remapped_input_list = [mapping_from_cards_to_alphabet(line, True) for line in input_list]
    for hand in remapped_input_list:
        cards, _ = hand
        count = dict(Counter(cards))
        j_count = count.get('1', 0)
        if 5 in count.values():
            current_point = 'Five of a kind'
        elif 4 in count.values():
            if j_count > 0:
                current_point = 'Five of a kind'
            else:
                current_point = 'Four of a kind'
        elif 3 in count.values() and 2 in count.values():
            if j_count > 0:
                current_point = 'Five of a kind'
            else:
                current_point = 'Full house'
        elif 3 in count.values():
            if j_count > 1:
                current_point = 'Four of a kind'
            else:
                current_point = 'Three of a kind'
        elif 2 in count.values():
            number_of_pairs = list(filter(lambda x: (x == 2), count.values()))
            if len(number_of_pairs) == 2:
                if j_count == 1:
                    current_point = 'Full house'
                elif j_count == 2:
                    current_point = 'Four of a kind'
                else:
                    current_point = 'Two pair'
            else:
                if j_count > 0:
                    current_point = 'Three of a kind'
                else:
                    current_point = 'One pair'
        else:
            if j_count == 1:
                current_point = 'One pair'
            else:
                current_point = 'High card'
        results[current_point].append(hand)
        results[current_point] = sorted(results[current_point], key=lambda x: (x[0]))
    all_hands = []
    all_hands.extend(results['High card'])
    all_hands.extend(results['One pair'])
    all_hands.extend(results['Two pair'])
    all_hands.extend(results['Three of a kind'])
    all_hands.extend(results['Full house'])
    all_hands.extend(results['Four of a kind'])
    all_hands.extend(results['Five of a kind'])
    final_sum = 0
    for rank, hand in enumerate(all_hands):
        _, bid = hand
        final_sum += (rank + 1) * bid
    return final_sum


def day_7(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 7th day we want to execute

    :param selected_part: selected Advent of Code part of the 7th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(7, int_list=False, is_test=test)
    splitted = [line.split() for line in input_list]
    input_list = [(cards, int(bid)) for cards, bid in splitted]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list[:])
        print('The result of 1st part of the 7th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list[:])
        print('The result of 2nd part of the 7th day of AoC is: ' + str(result_part_2))
