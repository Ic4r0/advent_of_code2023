""" Day 8: Haunted Wasteland

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from itertools import cycle
from math import lcm


# modules
def part_1(instructions: list, mappings: dict) -> int:
    """ Code for the 1st part of the 8th day of Advent of Code

    :param instructions: steps instructions
    :param mappings: mappings for steps
    :return: numeric result
    """
    current_position = 'AAA'
    steps = 0
    while current_position != 'ZZZ':
        current_instruction = instructions[steps % len(instructions)]
        left, right = mappings[current_position]
        if current_instruction == 'L':
            current_position = left
        else:
            current_position = right
        steps += 1
    return steps


def part_2(instructions: list, mappings: dict) -> int:
    """ Code for the 2nd part of the 8th day of Advent of Code

    :param instructions: steps instructions
    :param mappings: mappings for steps
    :return: numeric result
    """
    positions = [way for way in mappings if way.endswith('A')]
    totals = [0] * len(positions)
    for i, pos in enumerate(positions):
        c = cycle(int(instr == 'R') for instr in instructions)
        while not pos.endswith('Z'):
            totals[i] += 1
            pos = mappings[pos][next(c)]
    return lcm(*totals)


def day_8(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 8th day we want to execute

    :param selected_part: selected Advent of Code part of the 8th day
    :param test: flag to use test input
    """

    input_list = parse_by_line(8, int_list=False, is_test=test)
    instructions = list(input_list[0])
    mappings = dict()
    for line in input_list[2:]:
        start, left_right_tuple = line.split(' = ')
        left, right = left_right_tuple[1:-1].split(', ')
        mappings[start] = (left, right)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(instructions, mappings)
        print('The result of 1st part of the 8th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(instructions, mappings)
        print('The result of 2nd part of the 8th day of AoC is: ' + str(result_part_2))
