""" Day 3: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from collections import Counter


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    gamma_rate_bin = ''
    epsilon_rate_bin = ''
    line_length = len(input_list[0])
    for bit in range(line_length):
        column_list = [row[bit] for row in input_list]
        counter = Counter(column_list)
        if counter['0'] > counter['1']:
            gamma_rate_bin += '0'
            epsilon_rate_bin += '1'
        else:
            gamma_rate_bin += '1'
            epsilon_rate_bin += '0'
    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate = int(epsilon_rate_bin, 2)

    return gamma_rate * epsilon_rate


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    oxygen_generator_rating_list = input_list[:]
    co2_scrubber_rating_list = input_list[:]
    oxygen_generator_rating_bin = ''
    co2_scrubber_rating_bin = ''
    line_length = len(input_list[0])
    for bit in range(line_length):
        column_list = [row[bit] for row in oxygen_generator_rating_list]
        counter = Counter(column_list)
        if counter['0'] > counter['1']:
            oxygen_generator_rating_list = [row for row in oxygen_generator_rating_list if row[bit] == '0']
        else:
            oxygen_generator_rating_list = [row for row in oxygen_generator_rating_list if row[bit] == '1']
        if len(oxygen_generator_rating_list) == 1:
            oxygen_generator_rating_bin = oxygen_generator_rating_list[0]
            break
    for bit in range(line_length):
        column_list = [row[bit] for row in co2_scrubber_rating_list]
        counter = Counter(column_list)
        if counter['0'] > counter['1']:
            co2_scrubber_rating_list = [row for row in co2_scrubber_rating_list if row[bit] == '1']
        else:
            co2_scrubber_rating_list = [row for row in co2_scrubber_rating_list if row[bit] == '0']
        if len(co2_scrubber_rating_list) == 1:
            co2_scrubber_rating_bin = co2_scrubber_rating_list[0]
            break

    if oxygen_generator_rating_bin and co2_scrubber_rating_bin:
        oxygen_generator_rating = int(oxygen_generator_rating_bin, 2)
        co2_scrubber_rating = int(co2_scrubber_rating_bin, 2)
        return oxygen_generator_rating * co2_scrubber_rating
    else:
        return -1


def day_3(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 3rd day we want to execute

    :param selected_part: selected Advent of Code part of the 3rd day
    :param test: flag to use test input
    """
    diagnostic_report = parse_by_line(3, int_list=False, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(diagnostic_report)
        print('The result of 1st part of the 3rd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(diagnostic_report)
        print('The result of 2nd part of the 3rd day of AoC is: ' + str(result_part_2))
