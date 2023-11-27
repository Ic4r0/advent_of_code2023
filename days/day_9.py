""" Day 9: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def get_low_points(input_list: list) -> list:
    """ Get list of low points

    :param input_list: input list
    :return: list of low points
    """
    low_points = []
    for y in range(len(input_list)):
        for x in range(len(input_list[y])):
            current_coords = (y, x)     # (row, column)
            current_value = input_list[y][x]

            north_value = input_list[y-1][x] if y-1 in range(len(input_list)) else 10
            south_value = input_list[y+1][x] if y+1 in range(len(input_list)) else 10
            west_value = input_list[y][x-1] if x-1 in range(len(input_list[y])) else 10
            east_value = input_list[y][x+1] if x+1 in range(len(input_list[y])) else 10

            if current_value < min(north_value, south_value, west_value, east_value):
                low_points.append([current_coords, current_value])

    return low_points


def compute_basin_size(input_list: list, current_coords: tuple) -> int:
    """ Compute basin size

    :param input_list: input list
    :param current_coords: current coordinates
    :return: size of basin
    """
    if current_coords not in input_list:
        return 0
    basin_size = 1
    y, x = current_coords
    next_coords = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    input_list.remove(current_coords)
    for new_coords in next_coords:
        basin_size += compute_basin_size(input_list, new_coords)

    return basin_size


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 9th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    low_points = get_low_points(input_list)
    return sum(value + 1 for _, value in low_points)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 9th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    low_points = get_low_points(input_list)
    horizontal_max = len(input_list[0])
    vertical_max = len(input_list)
    grid_with_no_9 = [(y, x) for x in range(horizontal_max) for y in range(vertical_max) if input_list[y][x] < 9]
    basin_sizes = []
    for coords, _ in low_points:
        size = compute_basin_size(grid_with_no_9, coords)
        basin_sizes.append(size)
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def day_9(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 9th day we want to execute

    :param selected_part: selected Advent of Code part of the 9th day
    :param test: flag to use test input
    """
    input_list = [[int(number) for number in list(line)] for line in parse_by_line(9, int_list=False, is_test=test)]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list)
        print('The result of 1st part of the 9th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list)
        print('The result of 2nd part of the 9th day of AoC is: ' + str(result_part_2))
