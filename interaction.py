import minigames
import inventory


def interaction(new_hero_coordinates, level_map):
    result = False
    INTERACTION_ELEMENTS = ["W", "F", "C", "&", "D"]
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in INTERACTION_ELEMENTS:
        result = True
    return result


def handle_interaction(new_hero_coordinates, items, char_stats, inventory):
    if new_hero_coordinates == "W":
        loot = items.items.weapons()
        char_stats["ATC"] += loot[1]
        inventory.inventory.add_to_inventory(inventory, loot)
    elif new_hero_coordinates == "F":
        loot = items.items.food()
        if char_stats["HP"] < 100:
            char_stats["HP"] += loot[1]
        if char_stats["HP"] > 100:
            char_stats["HP"] = 100
    elif new_hero_coordinates == "C":
        loot = items.items.clotches()
        char_stats["DEF"] += loot[1]
        inventory.inventory.add_to_inventory(inventory, loot)
    elif new_hero_coordinates == "&":
        file_name = "ascii_art/mob.txt"
        minigames.hotcold()

    return inventory
