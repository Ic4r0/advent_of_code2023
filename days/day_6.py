""" Day 6: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_single_line
from collections import Counter


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 6th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    days_limit = 80
    for _ in range(days_limit):
        temp_input_list = input_list[:]
        for idx, internal_timer in enumerate(input_list):
            if internal_timer > 0:
                temp_input_list[idx] -= 1
            else:
                temp_input_list[idx] = 6
                temp_input_list.append(8)
        input_list = temp_input_list[:]
    return len(input_list)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 6th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    days_limit = 256
    timers = Counter(input_list)
    for _ in range(days_limit):
        temp_timers = {idx: 0 for idx in range(9)}
        temp_timers[8] = timers.get(0, 0)
        temp_timers[7] = timers.get(8, 0)
        temp_timers[6] = timers.get(7, 0) + timers.get(0, 0)
        temp_timers[5] = timers.get(6, 0)
        temp_timers[4] = timers.get(5, 0)
        temp_timers[3] = timers.get(4, 0)
        temp_timers[2] = timers.get(3, 0)
        temp_timers[1] = timers.get(2, 0)
        temp_timers[0] = timers.get(1, 0)
        timers = temp_timers.copy()

    return sum(timers.values())


def day_6(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 6th day we want to execute

    :param selected_part: selected Advent of Code part of the 6th day
    :param test: flag to use test input
    """
    input_list = [int(elem) for elem in parse_single_line(6, is_test=test).split(',')]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list[:])
        print('The result of 1st part of the 6th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list[:])
        print('The result of 2nd part of the 6th day of AoC is: ' + str(result_part_2))
