""" Day 11: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from os import system
from time import sleep


# modules
def pretty_print(input_list: list):
    """ Pretty print the octopuses lights

    :param input_list: input list
    """
    sleep(0.2)
    system('cls||clear')
    list_to_print = [['#' if elem == 0 else '.' for elem in line] for line in input_list]
    for y in range(len(list_to_print)):
        print(''.join(list_to_print[y]))


def valid_coordinates(input_list: list, flashes_coords: list) -> list:
    """ Return list of coordinates affected by flashes

    :param input_list: input list
    :param flashes_coords: flashes coordinates list
    :return: coordinates list
    """
    coords = []
    x_max = len(input_list[0])
    y_max = len(input_list)
    for flash in flashes_coords:
        y, x = flash
        if 0 <= y-1 < y_max and 0 <= x-1 < x_max and input_list[y-1][x-1] != 0:
            coords.append((y-1, x-1))
        if 0 <= y-1 < y_max and input_list[y-1][x] != 0:
            coords.append((y-1, x))
        if 0 <= y-1 < y_max and 0 <= x+1 < x_max and input_list[y-1][x+1] != 0:
            coords.append((y-1, x+1))
        if 0 <= x-1 < x_max and input_list[y][x-1] != 0:
            coords.append((y, x-1))
        if 0 <= x+1 < x_max and input_list[y][x+1] != 0:
            coords.append((y, x+1))
        if 0 <= y+1 < y_max and 0 <= x-1 < x_max and input_list[y+1][x-1] != 0:
            coords.append((y+1, x-1))
        if 0 <= y+1 < y_max and input_list[y+1][x] != 0:
            coords.append((y+1, x))
        if 0 <= y+1 < y_max and 0 <= x+1 < x_max and input_list[y+1][x+1] != 0:
            coords.append((y+1, x+1))
    return coords


def compute_chain_flash(input_list: list, zeros_list: list) -> int:
    """ Verify if some other octopus flash in this step

    :param input_list: input list
    :param zeros_list: flashes list
    :return: new flashes
    """
    if len(zeros_list) == 0:
        return 0
    coords = valid_coordinates(input_list, zeros_list)
    new_zeros_list = []
    for single_coord in coords:
        y, x = single_coord
        is_zero_before = input_list[y][x] == 0
        input_list[y][x] = input_list[y][x] + 1 if 0 < input_list[y][x] < 9 else 0
        if input_list[y][x] == 0 and not is_zero_before:
            new_zeros_list.append(single_coord)
    return len(new_zeros_list) + compute_chain_flash(input_list, new_zeros_list)


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 11th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    n_steps = 100
    n_flashes = 0
    # pretty_print(input_list)
    for step in range(n_steps):
        input_list = [[0 if elem == 9 else elem + 1 for elem in line] for line in input_list]
        zeros = [(y, x) for x in range(len(input_list[0])) for y in range(len(input_list)) if input_list[y][x] == 0]
        n_flashes += len(zeros) + compute_chain_flash(input_list, zeros)
        # pretty_print(input_list)

    return n_flashes


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 11th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    n_steps = 0
    # pretty_print(input_list)
    while True:
        n_steps += 1
        input_list = [[0 if elem == 9 else elem + 1 for elem in line] for line in input_list]
        zeros = [(y, x) for x in range(len(input_list[0])) for y in range(len(input_list)) if input_list[y][x] == 0]
        n_flashes = len(zeros) + compute_chain_flash(input_list, zeros)
        # pretty_print(input_list)
        if n_flashes == len(input_list) * len(input_list[0]):
            break

    return n_steps


def day_11(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 11th day we want to execute

    :param selected_part: selected Advent of Code part of the 11th day
    :param test: flag to use test input
    """
    octopuses_energy_level = [
        [int(energy_level) for energy_level in line] for line in parse_by_line(11, int_list=False, is_test=test)
    ]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(octopuses_energy_level[:])
        print('The result of 1st part of the 11th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(octopuses_energy_level[:])
        print('The result of 2nd part of the 11th day of AoC is: ' + str(result_part_2))
