""" Day 1: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# ['0', '1', ..., '9']
DIGITS_LIST = [str(dig) for dig in list(range(0, 10))]
# Stringified digit to be replaced with a similar string with the corresponding number inside it (needed for
# overlapping stringified digits)
STRINGIFIED_DIGITS = {
    'one': 'o1e',
    'two': 't2o',
    'three': 'th3ee',
    'four': 'fo4r',
    'five': 'fi5e',
    'six': 's6x',
    'seven': 'se7en',
    'eight': 'ei8ht',
    'nine': 'ni9e'
}


# modules
def digit_extractor(row: str) -> str:
    """ Method to extract the numeric part of each row

    :param row: row of the input list
    :return: string containing all the digits of row
    """
    remapped_row = map(lambda x: (x if x in DIGITS_LIST else 0), row)
    filtered_row = filter(lambda x: (x != 0), remapped_row)
    return ''.join(filtered_row)


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    numbers_list = []
    for row in input_list[:]:
        joined_row = digit_extractor(row)
        numbers_list.append(int(joined_row[0] + joined_row[-1]))
    return sum(numbers_list)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    numbers_list = []
    for row in input_list[:]:
        for str_number in STRINGIFIED_DIGITS:
            row = row.replace(str_number, STRINGIFIED_DIGITS[str_number])
        joined_row = digit_extractor(row)
        numbers_list.append(int(joined_row[0] + joined_row[-1]))
    return sum(numbers_list)


def day_1(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 1st day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    input_list = parse_by_line(1, int_list=False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list)
        print('The result of 2nd part of the 1st day of AoC is: ' + str(result_part_2))
