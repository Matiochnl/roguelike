import ui
import os
# TODO get rid off print functions


def statistic():
    stats = {'hp': 10, 'exp': 0, 'def': 1, 'atc': 1, 'lvl': 1}
    return stats


def add_character_stats(statistic):
    stats = statistic()
    ui.print_character_statistics(stats)
    points = 5
    while points > 0:
        stat_to_add = input("Enter 'H', 'h', 'D', 'd' or 'A', 'a' to add statistic: ")
        if stat_to_add in ["h", "H"]:
            stats["hp"] += 2
        elif stat_to_add in ["D", "d"]:
            stats["def"] += 1
        elif stat_to_add in ["A", "a"]:
            stats["atc"] += 1
        points -= 1
        os.system("clear")
        ui.print_character_statistics(stats)
        print("Start movement to play")
    return stats
