import os

import data_manager
import ui
import movement
import items_to_gather
import interaction

HERO_COORDINATES = [3, 11]


def get_character_at_position(level_map, new_hero_coordinates):
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    character = level_map[y_position][x_position]
    return character


def start_engine(char_stats, inventory):

    get_char = ""
    hero_coordinates = HERO_COORDINATES
    level_map = data_manager.get_maps_from_file("maps/level1.txt")
    level_map = movement.place_hero_new_pos(level_map, hero_coordinates)
    ui.print_level_map(level_map, char_stats, inventory)
    game_won = True
    while get_char != "q" and game_won:
        get_char = movement.get_char_in_terminal()
        new_hero_coordinates = movement.handle_coordinates(get_char, hero_coordinates)
        os.system("clear")
        if interaction.check_interaction(new_hero_coordinates, level_map):
            character = get_character_at_position(level_map, new_hero_coordinates)
            inventory = interaction.handle_interaction(character, items_to_gather, char_stats, inventory)

            if game_won != False:
                level_map = movement.map_with_updated_hero_pos(get_char, level_map, hero_coordinates, new_hero_coordinates)
                ui.print_level_map(level_map, char_stats, inventory)
        else:
            level_map = movement.map_with_updated_hero_pos(get_char, level_map, hero_coordinates, new_hero_coordinates)
            ui.print_level_map(level_map, char_stats, inventory)
            hero_coordinates = new_hero_coordinates
