import os
import data_manager
import ui
import movement

HERO_COORDINATES = [3, 11]


def start_engine(level_map, stats, inventory):
    hero_coordinates = HERO_COORDINATES
    level_map = data_manager.get_maps_from_file("maps/level1.txt")
    level_map = movement.place_hero_new_pos(level_map, hero_coordinates)
    ui.print_level_map(level_map, stats, inventory)
    get_char = ""
    while get_char != "q":
        get_char = movement.get_char_in_terminal()
        new_hero_coordinates = movement.handle_coordinates(get_char, hero_coordinates)
        level_map = movement.map_with_updated_hero_pos(get_char, level_map, hero_coordinates, new_hero_coordinates)
        hero_coordinates = new_hero_coordinates
        os.system("clear")
        ui.print_level_map(level_map, stats, inventory)
