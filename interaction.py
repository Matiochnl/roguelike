import minigames
import inv
import data_manager

def check_interaction(new_hero_coordinates, level_map):
    result = False
    INTERACTION_ELEMENTS = ["W", "F", "C", "&", "D"]
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in INTERACTION_ELEMENTS:
        result = True
    return result


def handle_interaction(character, items, char_stats, inventory):
    if character == "W":
        loot = items.weapons()
        char_stats["ATC"] += loot[1]
        inv.add_to_inventory(inventory, loot)
    elif character == "F":
        loot = items.food()
        if char_stats["HP"] < 100:
            char_stats["HP"] += loot[1]
        if char_stats["HP"] > 100:
            char_stats["HP"] = 100
    elif character == "C":
        loot = items.clothes()
        char_stats["DEF"] += loot[1]
        inv.add_to_inventory(inventory, loot)
    elif character == "&":
        print(data_manager.load_ascii_art("ascii_art/mob.txt"))
        minigames.hotcold()

    return inventory
