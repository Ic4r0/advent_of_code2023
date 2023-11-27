""" Day 5: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from re import match


# modules
def part_1(input_list: list, empty_grid: list) -> int:
    """ Code for the 1st part of the 5th day of Advent of Code

    :param input_list: input list
    :param empty_grid: empty grid matrix
    :return: numeric result
    """
    for point_1, point_2 in input_list:
        x1, y1 = point_1
        x2, y2 = point_2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                empty_grid[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                empty_grid[y1][x] += 1

    return sum(sum(1 if elem > 1 else 0 for elem in row) for row in empty_grid)


def part_2(input_list: list, empty_grid: list) -> int:
    """ Code for the 2nd part of the 5th day of Advent of Code

    :param input_list: input list
    :param empty_grid: empty grid matrix
    :return: numeric result
    """
    for point_1, point_2 in input_list:
        x1, y1 = point_1
        x2, y2 = point_2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                empty_grid[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                empty_grid[y1][x] += 1
        else:
            if x1 < x2:
                range_x = range(x1, x2 + 1)
            else:
                range_x = range(x1, x2 - 1, -1)
            if y1 < y2:
                range_y = range(y1, y2 + 1)
            else:
                range_y = range(y1, y2 - 1, -1)
            idx = 0
            while idx < len(range_x):
                empty_grid[range_y[idx]][range_x[idx]] += 1
                idx += 1

    return sum(sum(1 if elem > 1 else 0 for elem in row) for row in empty_grid)


def day_5(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 5th day we want to execute

    :param selected_part: selected Advent of Code part of the 5th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(5, int_list=False, is_test=test)
    max_x_value = 0
    max_y_value = 0
    vents_lines = []
    for row in input_list:
        matches = match(r'(\d+),(\d+) -> (\d+),(\d+)', row)
        x1, y1, x2, y2 = matches.groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        temp_max_x_value = max(x1, x2)
        if max_x_value < temp_max_x_value:
            max_x_value = temp_max_x_value
        temp_max_y_value = max(y1, y2)
        if max_y_value < temp_max_y_value:
            max_y_value = temp_max_y_value
        vents_lines.append([(x1, y1), (x2, y2)])

    matrix = [[0 for _ in range(max_x_value + 1)] for _ in range(max_y_value + 1)]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(vents_lines, matrix[:])
        print('The result of 1st part of the 5th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(vents_lines, matrix[:])
        print('The result of 2nd part of the 5th day of AoC is: ' + str(result_part_2))
