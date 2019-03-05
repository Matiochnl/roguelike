import os

import data_manager
import ui
import movement
import items_to_gather
import interaction

HERO_COORDINATES = [[3, 11], [13, 11], [1, 1]]
END_POSITION = [[104, 11], [114, 11], [11, 7]]
MAPS = ['maps/level1.txt', 'maps/level2.txt', 'maps/level3.txt']


def get_character_at_position(level_map, new_hero_coordinates):
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    character = level_map[y_position][x_position]
    return character


def start_engine(char_stats, inventory, map_iterator):

    get_char = ""
    hero_coordinates = HERO_COORDINATES[map_iterator]
    level_map = data_manager.get_maps_from_file(MAPS[map_iterator])
    level_map = movement.place_hero_new_pos(level_map, hero_coordinates)
    ui.print_level_map(level_map, char_stats, inventory)
        
    game_won = True
    while get_char != "q" and game_won:
        get_char = movement.get_char_in_terminal()
        new_hero_coordinates = movement.handle_coordinates(get_char, hero_coordinates, MAPS[map_iterator])
        os.system("clear")
        if interaction.check_interaction(new_hero_coordinates, level_map):
            character = get_character_at_position(level_map, new_hero_coordinates)
            inventory = interaction.handle_interaction(character, items_to_gather, char_stats, inventory)
            if map_iterator == 2 and character == "D":
                os.system("clear")
                print("Boss")
                game_won == False
            if game_won != False and map_iterator < 2:
                level_map = movement.map_with_updated_hero_pos(get_char, level_map, hero_coordinates, new_hero_coordinates)
                ui.print_level_map(level_map, char_stats, inventory)
            if map_iterator < 2 and character == "D":
                map_iterator += 1
                level_map = data_manager.get_maps_from_file(MAPS[map_iterator])
                hero_coordinates = HERO_COORDINATES[map_iterator]   
        else:
            level_map = movement.map_with_updated_hero_pos(get_char, level_map, hero_coordinates, new_hero_coordinates)
            ui.print_level_map(level_map, char_stats, inventory)
            hero_coordinates = new_hero_coordinates
