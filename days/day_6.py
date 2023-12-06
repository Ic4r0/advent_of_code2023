""" Day 6: Wait For It

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from math import prod


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 6th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    different_ways_to_win = []
    for idx in range(len(input_list[0])):
        different_ways_to_win_current_race = 0
        time = input_list[0][idx]
        distance = input_list[1][idx]
        for pressing_time in range(time):
            remaining_time = time - pressing_time
            distance_reached = remaining_time * pressing_time
            if distance_reached > distance:
                different_ways_to_win_current_race += 1
        if different_ways_to_win_current_race != 0:
            different_ways_to_win.append(different_ways_to_win_current_race)
    return prod(different_ways_to_win)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 6th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    different_ways_to_win = 0
    time = int(''.join(str(elem) for elem in input_list[0]))
    distance = int(''.join(str(elem) for elem in input_list[1]))
    for pressing_time in range(time):
        remaining_time = time - pressing_time
        distance_reached = remaining_time * pressing_time
        if distance_reached > distance:
            different_ways_to_win += 1
    return different_ways_to_win


def day_6(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 6th day we want to execute

    :param selected_part: selected Advent of Code part of the 6th day
    :param test: flag to use test input
    """
    input_list = [
        [int(elem) for elem in line.split()[1:]] for line in parse_by_line(6, int_list=False, is_test=test)
    ]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list[:])
        print('The result of 1st part of the 6th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list[:])
        print('The result of 2nd part of the 6th day of AoC is: ' + str(result_part_2))
