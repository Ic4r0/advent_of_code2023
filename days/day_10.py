""" Day 10: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def check_corrupted_line(line: str) -> int:
    """ Check if line is corrupted

    :param line: line to check
    :return: syntax error score if corrupted or 0
    """
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    corresponding_chunk = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    open_chunks = []
    for character in line:
        if character == '(' or character == '[' or character == '{' or character == '<':
            open_chunks.append(character)
        else:
            last_opened_chunk = open_chunks[-1]
            if corresponding_chunk[character] == last_opened_chunk:
                open_chunks.pop()
            else:
                return points[character]
    return 0


def complete_line(line: str) -> int:
    """ Complete line and return corresponding score

    :param line: line to complete
    :return: completion score
    """
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    corresponding_chunk = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    open_chunks = []
    for character in line:
        if character == '(' or character == '[' or character == '{' or character == '<':
            open_chunks.append(character)
        else:
            open_chunks.pop()
    completion = []
    for idx in range(len(open_chunks) - 1, -1, -1):
        completion.append(corresponding_chunk[open_chunks[idx]])
    score = 0
    for character in completion:
        score *= 5
        score += points[character]
    return score


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 10th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    scores = 0
    for line in input_list:
        scores += check_corrupted_line(line)
    return scores


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 10th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    idx_to_remove = []
    for idx, line in enumerate(input_list):
        if not check_corrupted_line(line):
            idx_to_remove.append(idx)
    incomplete_list = [line for idx, line in enumerate(input_list) if idx in idx_to_remove]
    scores = []
    for line in incomplete_list:
        scores.append(complete_line(line))
    scores.sort()
    return scores[len(scores)//2]


def day_10(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 10th day we want to execute

    :param selected_part: selected Advent of Code part of the 10th day
    :param test: flag to use test input
    """
    navigation_subsystem = parse_by_line(10, int_list=False, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(navigation_subsystem)
        print('The result of 1st part of the 10th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(navigation_subsystem)
        print('The result of 2nd part of the 10th day of AoC is: ' + str(result_part_2))
