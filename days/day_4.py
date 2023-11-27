""" Day 4: NA

Author: Ic4r0 - https://github.com/Ic4r0

Created: 27th November 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def check_row_column(board: list, drawn_numbers: list) -> bool:
    complete_line = False
    for row in board:
        if all(number in drawn_numbers for number in row):
            complete_line = True
            break
    if not complete_line:
        for column_idx in range(5):
            column = [row[column_idx] for row in board]
            if all(number in drawn_numbers for number in column):
                complete_line = True
                break
    return complete_line


def part_1(draws_list: list, boards_dict: dict) -> int:
    """ Code for the 1st part of the 4th day of Advent of Code

    :param draws_list: draws list
    :param boards_dict: dict containing all boards
    :return: numeric result
    """
    drawn = []
    bingo = False
    bingo_board = []
    for draw in draws_list:
        drawn.append(draw)
        for board_idx in boards_dict:
            bingo = check_row_column(boards_dict.get(board_idx), drawn)
            if bingo:
                bingo_board = boards_dict.get(board_idx)
                break
        if bingo:
            break

    return (sum(sum([elem for elem in row if elem not in drawn]) for row in bingo_board)) * drawn[-1]


def part_2(draws_list: list, boards_dict: dict) -> int:
    """ Code for the 2nd part of the 4th day of Advent of Code

    :param draws_list: draws list
    :param boards_dict: dict containing all boards
    :return: numeric result
    """
    drawn = []
    bingo = False
    bingo_board = []
    for draw in draws_list:
        drawn.append(draw)
        boards_to_delete = []
        for board_idx in boards_dict:
            bingo = check_row_column(boards_dict.get(board_idx), drawn)
            if bingo and len(boards_dict) == 1:
                bingo_board = boards_dict.get(board_idx)
                break
            elif bingo:
                bingo_board = boards_dict.get(board_idx)
                bingo = False
                boards_to_delete.append(board_idx)
        for board in boards_to_delete:
            del boards_dict[board]
        if bingo:
            break
    return (sum(sum([elem for elem in row if elem not in drawn]) for row in bingo_board)) * drawn[-1]


def day_4(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 4th day we want to execute

    :param selected_part: selected Advent of Code part of the 4th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(4, int_list=False, is_test=test)
    draws = [int(number) for number in input_list[0].split(',')]
    boards = dict()
    idx = 0
    n_board = 0
    boards_list = input_list[2:]
    while idx < len(boards_list):
        single_board = [[int(elem) for elem in row.split()] for row in boards_list[idx:idx+5]]
        boards[n_board] = single_board
        idx += 6
        n_board += 1

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(draws, boards)
        print('The result of 1st part of the 4th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(draws, boards)
        print('The result of 2nd part of the 4th day of AoC is: ' + str(result_part_2))
