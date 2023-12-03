""" Day 3: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from math import prod

# ['0', '1', ..., '9']
DIGITS_LIST = [str(dig) for dig in list(map(lambda x: x, range(0, 10)))]


# modules
def get_part_numbers(input_list: list) -> list:
    """ Code for the 1st part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: part numbers [(part number, row, start idx, end idx), ...]
    """
    part_numbers = []
    for line_idx, line in enumerate(input_list):
        curr_idx = 0
        max_idx = len(line)
        separated_line = list(line)
        while curr_idx < max_idx:
            if separated_line[curr_idx] in DIGITS_LIST:
                # [number, start_idx, end_idx]
                new_number = [separated_line[curr_idx], curr_idx, curr_idx]
                curr_idx += 1
                while curr_idx < max_idx and separated_line[curr_idx] in DIGITS_LIST:
                    new_number[0] += separated_line[curr_idx]
                    new_number[2] = curr_idx
                    curr_idx += 1
                around_str = ''
                number_value, number_min_idx, number_max_idx = new_number
                # line above new_number
                if line_idx - 1 >= 0:
                    around_str += input_list[line_idx - 1][
                                  max(0, number_min_idx - 1): min(max_idx - 1, number_max_idx + 2)
                                  ]
                # same line of new_number
                if number_min_idx > 0:
                    around_str += line[number_min_idx - 1]
                if number_max_idx < max_idx - 1:
                    around_str += line[number_max_idx + 1]
                # line below new_number
                if line_idx + 1 < len(input_list):
                    around_str += input_list[line_idx + 1][
                                  max(0, number_min_idx - 1): min(max_idx - 1, number_max_idx + 2)
                                  ]
                # check if part number
                filtered_around_str = list(filter(lambda x: (x not in DIGITS_LIST and x != '.'), list(around_str)))
                if len(filtered_around_str) > 0:
                    part_numbers.append((int(number_value), line_idx, number_min_idx, number_max_idx))
            curr_idx += 1
    return part_numbers


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    part_numbers = get_part_numbers(input_list)
    return sum([number for number, _, _, _ in part_numbers])


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    part_numbers = get_part_numbers(input_list)
    gears_ratios = []
    for line_idx, line in enumerate(input_list):
        for ch_idx in range(len(line)):
            if line[ch_idx] == '*':
                around_part_numbers = list(filter(lambda x: (
                    x[1] in list(range(line_idx - 1, line_idx + 2)) and x[2] - 1 <= ch_idx <= x[3] + 1
                ), part_numbers))
                if len(around_part_numbers) == 2:
                    gears_ratios.append(prod([number for number, _, _, _ in around_part_numbers]))
    return sum(gears_ratios)


def day_3(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 3rd day we want to execute

    :param selected_part: selected Advent of Code part of the 3rd day
    :param test: flag to use test input
    """
    engine_schematic = parse_by_line(3, int_list=False, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(engine_schematic)
        print('The result of 1st part of the 3rd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(engine_schematic)
        print('The result of 2nd part of the 3rd day of AoC is: ' + str(result_part_2))
