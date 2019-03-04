import ui
import os
# TODO get rid off print functions


def statistic():
    stats = {'hp': 10, 'exp': 0, 'def': 1, 'atc': 1, 'lvl': 1}
    return stats


def add_character_stats():
    os.system("clear")
    stats = statistic()
    points = 5
    while points > 0:
        ui.print_character_statistics(stats)
        stat_to_add = input("""Enter H to add HP points, D to add DEF point and A to add ATC piont to statistic: """)
        if stat_to_add in ["h", "H"]:
            stats["hp"] += 2
        elif stat_to_add in ["D", "d"]:
            stats["def"] += 1
        elif stat_to_add in ["A", "a"]:
            stats["atc"] += 1
        points -= 1
        
        os.system("clear")
        
        
    return stats
