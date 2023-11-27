""" Day 8: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 8th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    output_list = [outputs for _, outputs in input_list]
    unique_number_segments = [2, 4, 3, 7]
    return sum(sum(1 for number in numbers if len(number) in unique_number_segments) for numbers in output_list)


def decode_digits(input_list: list) -> dict:
    """ Utils to decode which letters correspond to which number

    :param input_list: input list
    :return: dict containing the value of the digits
    """
    digit_1 = sort_letters([letters for letters in input_list if len(letters) == 2][0])
    digit_2 = ''
    digit_3 = ''
    digit_4 = sort_letters([letters for letters in input_list if len(letters) == 4][0])
    digit_5 = ''
    digit_6 = ''
    digit_7 = sort_letters([letters for letters in input_list if len(letters) == 3][0])
    digit_8 = sort_letters([letters for letters in input_list if len(letters) == 7][0])
    digit_9 = ''
    digit_0 = ''
    digits_2_3_5 = [letters for letters in input_list if len(letters) == 5]
    digits_0_6_9 = [letters for letters in input_list if len(letters) == 6]

    for digit in digits_0_6_9:
        sorted_digit = sort_letters(digit)
        if fully_contains(list(sorted_digit), list(digit_4)):
            digit_9 = sorted_digit
        elif fully_contains(list(sorted_digit), list(remove_substring(digit_8, digit_1))):
            digit_6 = sorted_digit
        else:
            digit_0 = sorted_digit

    for digit in digits_2_3_5:
        sorted_digit = sort_letters(digit)
        if fully_contains(list(sorted_digit), list(digit_7)):
            digit_3 = sorted_digit
        elif fully_contains(list(sorted_digit), list(remove_substring(digit_8, digit_4))):
            digit_2 = sorted_digit
        else:
            digit_5 = sorted_digit

    return {
        digit_1: 1,
        digit_2: 2,
        digit_3: 3,
        digit_4: 4,
        digit_5: 5,
        digit_6: 6,
        digit_7: 7,
        digit_8: 8,
        digit_9: 9,
        digit_0: 0,
    }


def sort_letters(letters: str) -> str:
    """ Sort input string

    :param letters: input string
    :return: sorted string
    """
    sorted_string = list(letters)
    sorted_string.sort()
    return ''.join(sorted_string)


def fully_contains(parent_list: list, sublist: list) -> bool:
    """ Check if sublist is fully contained in parent_list

    :param parent_list: current list
    :param sublist: sublist to compare
    :return: check result
    """
    return all(elem in parent_list for elem in sublist)


def remove_substring(parent_string: str, substring: str) -> str:
    """ Remove each character of substring from parent_string

    :param parent_string: current string
    :param substring: substring to remove
    :return: new string
    """
    new_string = parent_string
    for character in substring:
        new_string = new_string.replace(character, '')
    return new_string


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 8th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    result = 0
    for inputs, outputs in input_list:
        digits_dict = decode_digits(inputs)
        output_number = 0
        for idx, digit in enumerate(outputs):
            sorted_digit = list(digit)
            sorted_digit.sort()
            sorted_digit = ''.join(sorted_digit)
            if idx == 0:
                output_number += 1000 * digits_dict[sorted_digit]
            elif idx == 1:
                output_number += 100 * digits_dict[sorted_digit]
            elif idx == 2:
                output_number += 10 * digits_dict[sorted_digit]
            elif idx == 3:
                output_number += digits_dict[sorted_digit]
        result += output_number

    return result


def day_8(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 8th day we want to execute

    :param selected_part: selected Advent of Code part of the 8th day
    :param test: flag to use test input
    """
    input_list = [
        [
            split_part.strip().split() for split_part in elem.split('|')
        ] for elem in parse_by_line(8, int_list=False, is_test=test)
    ]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list)
        print('The result of 1st part of the 8th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list)
        print('The result of 2nd part of the 8th day of AoC is: ' + str(result_part_2))
