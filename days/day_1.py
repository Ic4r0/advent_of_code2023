""" Day 1: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from re import finditer


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    digits_list = [str(dig) for dig in list(map(lambda x: x, range(0, 10)))]
    numbers_list = []
    for row in input_list[:]:
        remapped_row = map(lambda x: (x if x in digits_list else 0), row)
        filtered_row = filter(lambda x: (x != 0), remapped_row)
        joined_row = ''.join(filtered_row)
        numbers_list.append(int(joined_row[0] + joined_row[-1]))
    return sum(numbers_list)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    stringified_digit = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    digits_list = [str(dig) for dig in list(map(lambda x: x, range(0, 10)))]
    numbers_list = []
    for row in input_list[:]:
        numbers_idxs = []
        for idx, ch in enumerate(row):
            if ch in digits_list:
                numbers_idxs.append([ch, idx])
        for number in stringified_digit:
            for matched in finditer(number, row):
                numbers_idxs.append([str(stringified_digit[number]), matched.start()])
        numbers_idxs.sort(key=lambda x: x[1])
        numbers_list.append(int(numbers_idxs[0][0] + numbers_idxs[-1][0]))
    return sum(numbers_list)


def day_1(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 1st day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    input_list = parse_by_line(1, int_list=False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list)
        print('The result of 2nd part of the 1st day of AoC is: ' + str(result_part_2))
