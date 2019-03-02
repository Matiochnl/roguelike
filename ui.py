import os
hero_position = [3, 11]


def get_input(question):
    answer = input(question)

    return answer


def print_gane_instructions():
    print("Press W A S D to move | #-wall, B-bush, R-river, @-hero, &-enemy, F-food, D-next level, W-weapon, C-clothes")


def main_menu_options():
    print("""\n\nHammer of Justice:
(1). Play game
(2). How to play
(3). Highscore board
(4). Credits
(5). Exit""")
    answer = get_input("\nChoose option: ")
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
