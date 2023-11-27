""" Day 7: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_single_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 7th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    min_value = min(input_list)
    max_value = max(input_list)

    positions_dict = {
        value: sum(
            abs(input_elem - value)
            for input_elem in input_list
        ) for value in range(min_value, max_value + 1)
    }

    return min(positions_dict.values())


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 7th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    min_value = min(input_list)
    max_value = max(input_list)

    positions_dict = {
        value: sum(
            sum(range(1, abs(input_elem - value) + 1))
            for input_elem in input_list
        ) for value in range(min_value, max_value + 1)
    }

    return min(positions_dict.values())


def day_7(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 7th day we want to execute

    :param selected_part: selected Advent of Code part of the 7th day
    :param test: flag to use test input
    """
    input_list = [int(elem) for elem in parse_single_line(7, is_test=test).split(',')]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list[:])
        print('The result of 1st part of the 7th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list[:])
        print('The result of 2nd part of the 7th day of AoC is: ' + str(result_part_2))
