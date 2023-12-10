""" Day 10: Pipe Maze

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


NEXT_MOVEMENT_BY_DIRECTION = {
    'd_|': [(1, 0), 'd'],
    'u_|': [(-1, 0), 'u'],
    'l_-': [(0, -1), 'l'],
    'r_-': [(0, 1), 'r'],
    'd_L': [(0, 1), 'r'],
    'l_L': [(-1, 0), 'u'],
    'd_J': [(0, -1), 'l'],
    'r_J': [(-1, 0), 'u'],
    'u_7': [(0, -1), 'l'],
    'r_7': [(1, 0), 'd'],
    'u_F': [(0, 1), 'r'],
    'l_F': [(1, 0), 'd']
}

DIRECTIONS = [[(0, -1), 'l'], [(-1, 0), 'u'], [(0, 1), 'r'], [(1, 0), 'd']]


# modules
def part_1(input_dict: dict) -> int:
    """ Code for the 1st part of the 10th day of Advent of Code

    :param input_dict: input dict
    :return: numeric result
    """
    starting_point = input_dict.get('S')    # coordinates tuple (line, column)
    steps = 0
    for direction_tuple, direction in DIRECTIONS:
        current_pos = tuple(map(sum, zip(starting_point, direction_tuple)))
        current_val = input_dict.get(current_pos, 0)
        steps = 1
        while current_val != 0 and current_val != 'S' and direction + '_' + current_val in NEXT_MOVEMENT_BY_DIRECTION:
            next_step, direction = NEXT_MOVEMENT_BY_DIRECTION.get(direction + '_' + current_val)
            current_pos = tuple(map(sum, zip(current_pos, next_step)))
            current_val = input_dict.get(current_pos, 0)
            steps += 1
        if current_val == 'S':
            break
    return steps // 2


def part_2(input_dict: dict) -> int:
    """ Code for the 2nd part of the 10th day of Advent of Code

    :param input_dict: input dict
    :return: numeric result
    """
    # Algorithm:
    # https://gamedev.stackexchange.com/questions/141460/how-can-i-fill-the-interior-of-a-closed-loop-on-a-tile-map
    return 0


def day_10(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 10th day we want to execute

    :param selected_part: selected Advent of Code part of the 10th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(10, int_list=False, is_test=test)
    input_dict = dict()
    for idx_line, line in enumerate(input_list):
        for idx_ch, ch in enumerate(line):
            ch_coordinates = (idx_line, idx_ch)
            if ch == 'S':
                input_dict[ch_coordinates] = ch
                input_dict[ch] = ch_coordinates
            elif ch != '.':
                input_dict[ch_coordinates] = ch

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_dict)
        print('The result of 1st part of the 10th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_dict)
        print('The result of 2nd part of the 10th day of AoC is: ' + str(result_part_2))
