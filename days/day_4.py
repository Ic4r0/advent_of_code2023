""" Day 4: Scratchcards

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 4th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    winning_points = 0
    for winning, my_numbers in input_list:
        found_numbers = []
        for number in my_numbers:
            if number in winning:
                found_numbers.append(number)
        if len(found_numbers) == 1:
            winning_points += 1
        elif len(found_numbers) > 1:
            winning_points += 2 ** (len(found_numbers) - 1)

    return winning_points


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 4th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    input_dict = {idx: [scratchcard] for idx, scratchcard in enumerate(input_list)}
    for idx, scratchcards_list in input_dict.items():
        found_numbers = 0
        winning, my_numbers = scratchcards_list[0]
        for number in my_numbers:
            if number in winning:
                found_numbers += 1
        for val in range(found_numbers):
            if idx + val + 1 in input_dict:
                scratchcard = input_dict[idx + val + 1][0]
                for _ in range(len(input_dict[idx])):
                    input_dict[idx + val + 1].append(scratchcard)
    results = list(map(lambda x: (len(x)), input_dict.values()))
    return sum(results)


def day_4(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 4th day we want to execute

    :param selected_part: selected Advent of Code part of the 4th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(4, int_list=False, is_test=test)
    separated_numbers = [
        [[int(val) for val in winning.split()], [int(val) for val in my_numbers.split()]]
        for winning, my_numbers in [line.split(': ')[1].split(' | ') for line in input_list]
    ]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(separated_numbers)
        print('The result of 1st part of the 4th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(separated_numbers)
        print('The result of 2nd part of the 4th day of AoC is: ' + str(result_part_2))
