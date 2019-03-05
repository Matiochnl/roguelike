import ui
import os


def statistic():
    stats = {'HP': 75, 'EXP': 0, 'DEF': 1, 'ATC': 1, 'LVL': 1}
    return stats


def add_character_stats():
    os.system("clear")
    stats = statistic()
    points = 5
    while points > 0:
        ui.print_character_statistics(stats)
        stat_to_add = input("""Enter H to add HP points, D to add DEF point and A to add ATC piont to statistic: """)
        if stat_to_add in ["h", "H"]:
            stats["HP"] += 2
        elif stat_to_add in ["D", "d"]:
            stats["DEF"] += 1
        elif stat_to_add in ["A", "a"]:
            stats["ATC"] += 1
        points -= 1

        os.system("clear")

    return stats
