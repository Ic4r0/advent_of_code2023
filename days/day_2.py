""" Day 2: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    h_position = 0
    depth = 0
    for direction, step in input_list:
        if direction == 'forward':
            h_position += step
        elif direction == 'down':
            depth += step
        elif direction == 'up':
            depth -= step

    return h_position * depth


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    h_position = 0
    depth = 0
    aim = 0
    for direction, step in input_list:
        if direction == 'forward':
            h_position += step
            depth += aim * step
        elif direction == 'down':
            aim += step
        elif direction == 'up':
            aim -= step

    return h_position * depth


def day_2(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 2nd day we want to execute

    :param selected_part: selected Advent of Code part of the 2nd day
    :param test: flag to use test input
    """
    directions = [line.split() for line in parse_by_line(2, int_list=False, is_test=test)]
    remapped_directions = [(splitted_direction[0], int(splitted_direction[1])) for splitted_direction in directions]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(remapped_directions)
        print('The result of 1st part of the 2nd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(remapped_directions)
        print('The result of 2nd part of the 2nd day of AoC is: ' + str(result_part_2))
