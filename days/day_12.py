""" Day 12: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from collections import defaultdict, deque


# modules
def compute_paths(caves: dict) -> list:
    """ Compute distinct paths

    :param caves: caves connections
    :return: list [count skip duplicates, count no skip duplicates]
    """
    counts = []
    for skip_duplicates in True, False:
        count, search = 0, deque((child, set(), False) for child in caves['start'])

        while search:
            parent, lowers, duplicate = search.popleft()

            if parent == 'end':
                count += 1
                continue
            elif parent.islower():
                if parent in lowers:
                    if skip_duplicates or duplicate:
                        continue
                    else:
                        duplicate = True
                lowers.add(parent)

            search.extend((child, set(lowers), duplicate) for child in caves[parent] if child != 'start')

        counts.append(count)
    return counts


def part_1(caves: dict) -> int:
    """ Code for the 1st part of the 12th day of Advent of Code

    :param caves: caves connections
    :return: numeric result
    """
    counts = compute_paths(caves)
    return counts[0]


def part_2(caves: dict) -> int:
    """ Code for the 2nd part of the 12th day of Advent of Code

    :param caves: caves connections
    :return: numeric result
    """
    counts = compute_paths(caves)
    return counts[1]


def day_12(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 12th day we want to execute

    :param selected_part: selected Advent of Code part of the 12th day
    :param test: flag to use test input
    """
    caves = defaultdict(list)

    for line in parse_by_line(12, int_list=False, is_test=test):
        a, b = line.split("-")
        caves[a].append(b)
        caves[b].append(a)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(caves)
        print('The result of 1st part of the 12th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(caves)
        print('The result of 2nd part of the 12th day of AoC is: ' + str(result_part_2))
