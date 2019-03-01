import ui


def add_character_stats():
    stats = {'hp': 10, 'exp': 0, 'def': 1, 'atc': 1, 'lvl': 1}
    print_character_statistics(stats)
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
        print_character_statistics(stats)
        print("Start movement to play")
    return stats

