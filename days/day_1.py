""" Day 1: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    increases = [1 if idx != 0 and input_list[idx] > input_list[idx - 1] else 0 for idx in range(len(input_list))]
    return sum(increases)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    modified_input = [sum(input_list[idx:idx+3]) for idx in range(len(input_list) - 2)]
    increases = [
        1 if idx != 0 and modified_input[idx] > modified_input[idx - 1] else 0 for idx in range(len(modified_input))
    ]
    return sum(increases)


def day_1(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 1st day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    depth_measurement_increases = parse_by_line(1, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(depth_measurement_increases)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(depth_measurement_increases)
        print('The result of 2nd part of the 1st day of AoC is: ' + str(result_part_2))
