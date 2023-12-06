""" Day 5: If You Give A Seed A Fertilizer

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
import sys


# modules
def empty_row(row: str) -> bool:
    """ Check if a row of the input list is empty

    :param row: row from input list
    :return: is empty
    """
    string_to_check = row.split()
    return len(string_to_check) == 0


def part_1(seeds: list, mapping: dict) -> int:
    """ Code for the 1st part of the 5th day of Advent of Code

    :param seeds: seeds
    :param mapping: mapping from seed to location
    :return: numeric result
    """
    locations = []
    for seed in seeds:
        current_value = seed
        for mapping_key in mapping:
            needed_mapping = list(filter(lambda x: (x[0] <= current_value < x[0] + x[2]), mapping[mapping_key]))
            if len(needed_mapping) > 0:
                source, destination, _ = needed_mapping[0]
                current_value = destination + current_value - source
        locations.append(current_value)
    return min(locations)


def map_seed(s, m):
    source_start, destination_start, _ = m
    return destination_start + s - source_start


def map_seed_range(seed_range, map_ranges):
    seed_ranges = []
    seed_start, seed_end = seed_range[0], seed_range[1]

    for m in map_ranges:
        source_start, source_end = m[0], m[0] + m[2] - 1

        overlap_start = max(seed_start, source_start)
        overlap_end = min(seed_end, source_end)

        # if overlap exists
        if overlap_start <= overlap_end:
            # keep the seed range before ovelap untouched
            if seed_start <= overlap_start - 1:
                seed_ranges.append((seed_start, overlap_start - 1))

            # map range
            seed_ranges.append((map_seed(overlap_start, m), map_seed(overlap_end, m)))

            # cut off already mapped seed ranges
            if overlap_end + 1 <= seed_end:
                seed_start = overlap_end + 1
            else:
                # empty seed range left
                seed_start = sys.maxsize
                break

    # if we have some seed range left
    if seed_start <= seed_end:
        seed_ranges.append((seed_start, seed_end))

    return seed_ranges


def part_2(seeds: list, mapping: dict) -> int:
    """ Code for the 2nd part of the 5th day of Advent of Code

    :param seeds: seeds
    :param mapping: mapping from seed to location
    :return: numeric result
    """
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    return 0


def day_5(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 5th day we want to execute

    :param selected_part: selected Advent of Code part of the 5th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(5, int_list=False, is_test=test)
    seeds = [int(seed) for seed in input_list[0].split()[1:]]
    row_idx = 2
    section = 0
    # { section_number: [(source, destination, range), ...], ... }
    seed_to_location_map = {}
    while row_idx < len(input_list):
        # skip description row
        row_idx += 1
        seed_to_location_map[section] = []
        while row_idx < len(input_list) and not empty_row(input_list[row_idx]):
            destination, source, range_val = [int(val) for val in input_list[row_idx].split()]
            new_mapping = (source, destination, range_val)
            seed_to_location_map[section].append(new_mapping)
            row_idx += 1
        section += 1
        row_idx += 1

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(seeds, seed_to_location_map)
        print('The result of 1st part of the 5th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(seeds, seed_to_location_map)
        print('The result of 2nd part of the 5th day of AoC is: ' + str(result_part_2))
