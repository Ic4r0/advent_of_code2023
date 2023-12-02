""" Day 2: Cube Conundrum

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from math import prod


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    max_red = 12
    max_green = 13
    max_blue = 14
    valid_games = []
    for idx, game in enumerate(input_list):
        valid_sets = []
        for single_set in game:
            current_state = {'red': max_red, 'green': max_green, 'blue': max_blue}
            for number, color in single_set:
                current_state[color] -= int(number)
            if all([val >= 0 for val in current_state.values()]):
                valid_sets.append(idx + 1)
        if len(valid_sets) == len(game):
            valid_games.append(valid_sets[0])
    return sum(valid_games)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    summed_powers = []
    for game in input_list:
        required_colors = {'red': 0, 'green': 0, 'blue': 0}
        for single_set in game:
            for number, color in single_set:
                if int(number) > required_colors[color]:
                    required_colors[color] = int(number)
        summed_powers.append(prod(required_colors.values()))
    return sum(summed_powers)


def day_2(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 2nd day we want to execute

    :param selected_part: selected Advent of Code part of the 2nd day
    :param test: flag to use test input
    """
    games_records = [line.split(': ')[1] for line in parse_by_line(2, int_list=False, is_test=test)]
    games = []
    for line in games_records:
        single_game = []
        sets = line.split('; ')
        for single_set in sets:
            cubes = single_set.split(', ')
            number_and_color = [val.split(' ') for val in cubes]
            single_game.append(number_and_color)
        games.append(single_game)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(games)
        print('The result of 1st part of the 2nd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(games)
        print('The result of 2nd part of the 2nd day of AoC is: ' + str(result_part_2))
