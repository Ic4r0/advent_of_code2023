""" Day 13: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from re import match


# modules
def pretty_print(points: list):
    x_max = max([x for x, _ in points]) + 1
    y_max = max([y for _, y in points]) + 1
    grid = [['.' for _ in range(x_max)] for _ in range(y_max)]
    for x, y in points:
        grid[y][x] = '#'
    for y in range(len(grid)):
        print(''.join(grid[y]))


def tuple_subtraction(tuple_1: tuple, tuple_2: tuple) -> tuple:
    result = []
    for idx in range(len(tuple_1)):
        result.append(tuple_1[idx] - tuple_2[idx])
    return tuple(result)


def fold(points: list, single_fold: tuple):
    """ Apply fold to points

    :param points: points coordinates list
    :param single_fold: fold to be done on points
    """
    axis, fold_value = single_fold
    if axis == 'x':
        base_offset = (1, 0)
        static_points = [(x, y) for x, y in points if x < fold_value]
        points_to_be_folded = [(x, y) for x, y in points if x > fold_value]
    else:
        base_offset = (0, 1)
        static_points = [(x, y) for x, y in points if y < fold_value]
        points_to_be_folded = [(x, y) for x, y in points if y > fold_value]
    for x, y in points_to_be_folded:
        abs_from_fold = abs(x - fold_value) if axis == 'x' else abs(y - fold_value)
        offset = tuple(2 * elem * abs_from_fold for elem in base_offset)
        static_points.append(tuple_subtraction((x, y), offset))
    return list(set(static_points))


def part_1(points: list, folds: list) -> int:
    """ Code for the 1st part of the 13th day of Advent of Code

    :param points: points coordinates list
    :param folds: folds list
    :return: numeric result
    """
    new_points = fold(points, folds[0])
    return len(new_points)


def part_2(points: list, folds: list) -> int:
    """ Code for the 2nd part of the 13th day of Advent of Code

    :param points: points coordinates list
    :param folds: folds list
    :return: numeric result
    """
    new_points = points[:]
    for single_fold in folds:
        new_points = fold(new_points, single_fold)

    pretty_print(new_points)
    return 0


def day_13(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 13th day we want to execute

    :param selected_part: selected Advent of Code part of the 13th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(13, int_list=False, is_test=test)
    idx_empty_line = [idx for idx, line in enumerate(input_list) if line == ''][0]

    points_coords = []
    for line in input_list[:idx_empty_line]:
        x, y = line.split(',')
        points_coords.append((int(x), int(y)))
    folds = []
    for line in input_list[idx_empty_line+1:]:
        m = match(r'fold along (x|y)=(\d+)', line)
        axis, idx = m.groups()
        folds.append((axis, int(idx)))

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(points_coords, folds)
        print('The result of 1st part of the 13th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(points_coords, folds)
        print('The result of 2nd part of the 13th day of AoC is: ' + str(result_part_2))
