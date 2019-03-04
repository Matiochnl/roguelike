

def interaction(new_hero_coordinates, level_map):
    result = False
    INTERACTION_ELEMENTS = ["W", "F", "C", "&", "D"]
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in INTERACTION_ELEMENTS:
        result = True
    return result