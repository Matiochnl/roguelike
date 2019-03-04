import os

import data_manager


hero_position = [3, 11]


def print_game_instructions():
    print("Press W A S D to move | #-wall, B-bush, R-river, @-hero, &-enemy, F-food, D-next level, W-weapon, C-clothes")


def main_menu_options():
    print("""\n\nHammer of Justice:
(1). Play game
(2). How to play
(3). Highscore board
(4). Credits
(5). Exit""")
    answer = input("\nChoose option: ")
    return answer


def print_character_statistics(char_stats):
    string = "HP:{:}\tEXP:{:}\tDEF:{:}\tATC:{:}\tLVL:{:}"
    print(string.format(*char_stats.values()))


def print_inventory(inventory):
    print("Inventory:")
    string = "{}, " * len(inventory)
    print(string.format(*inventory))


def show_map(level_map):
    for line in level_map:
        print("".join(line))


def print_user_score(char_stats, play_time):
    final_score = str(int(char_stats["EXP"] * 3.14 * round(play_time, 2)))
    print(final_score)


def print_level_map(level_map, char_stats, inv):
    """
    Display map to user
    :param level_map: list of lists: map from text file or updated when program is running
    """
    print_character_statistics(char_stats)

    for line in level_map:
        print("".join(line))
