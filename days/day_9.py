""" Day 9: Mirage Maintenance

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 9th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    final_difference_value = []
    for line in input_list:
        last_values = []
        to_be_subtracted = line[:]
        current_results = []
        idx_subtr = 0
        while idx_subtr + 1 < len(to_be_subtracted):
            minuend = to_be_subtracted[idx_subtr + 1]
            subtrahend = to_be_subtracted[idx_subtr]
            current_results.append(minuend - subtrahend)
            if idx_subtr + 2 < len(to_be_subtracted):
                idx_subtr += 1
            elif all(res == 0 for res in current_results):
                current_res = minuend
                last_values.reverse()
                for elem in last_values:
                    current_res += elem
                final_difference_value.append(current_res)
                idx_subtr += 2
            else:
                last_values.append(minuend)
                to_be_subtracted = current_results[:]
                current_results = []
                idx_subtr = 0
    return sum(final_difference_value)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 9th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    final_difference_value = []
    for line in input_list:
        first_values = [line[0]]
        to_be_subtracted = line[:]
        current_results = []
        idx_subtr = 0
        while idx_subtr + 1 < len(to_be_subtracted):
            minuend = to_be_subtracted[idx_subtr + 1]
            subtrahend = to_be_subtracted[idx_subtr]
            current_results.append(minuend - subtrahend)
            if idx_subtr + 2 < len(to_be_subtracted):
                idx_subtr += 1
            elif all(res == 0 for res in current_results):
                current_res = 0
                first_values.reverse()
                for elem in first_values:
                    current_res = elem - current_res
                final_difference_value.append(current_res)
                idx_subtr += 2
            else:
                first_values.append(current_results[0])
                to_be_subtracted = current_results[:]
                current_results = []
                idx_subtr = 0
    return sum(final_difference_value)


def day_9(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 9th day we want to execute

    :param selected_part: selected Advent of Code part of the 9th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(9, int_list=False, is_test=test)
    splitted = [line.split() for line in input_list]
    remapped = [[int(part) for part in separated_line] for separated_line in splitted]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(remapped)
        print('The result of 1st part of the 9th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(remapped)
        print('The result of 2nd part of the 9th day of AoC is: ' + str(result_part_2))
