import os
import data_manager
import ui


def get_char_in_terminal():
    """
    Get character from user in terminal, when he push the button.
    :return: char: keyboard character
    """
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char


def obstacles(new_hero_coordinates, level_map):

    result = True
    obstackles = ["#", "B", "R"]
    x_position = new_hero_coordinates[0]
    y_position = new_hero_coordinates[1]
    if level_map[y_position][x_position] in obstackles:
        result = False

    return result


def place_hero_new_pos(level_map, hero_coordinates):
    x_pos = hero_coordinates[0]
    y_pos = hero_coordinates[1]
    level_map[y_pos][x_pos] = "@"
    return level_map


def handle_coordinates(get_char, hero_coordinates, filename):

    result = hero_coordinates
    level_map = data_manager.get_maps_from_file(filename)
    new_hero_coordinates = new_hero_pos(get_char, hero_coordinates)
    if obstacles(new_hero_coordinates, level_map):
        result = new_hero_coordinates
    return result


def new_hero_pos(get_char, hero_coordinates):
    x_position = hero_coordinates[0]
    y_position = hero_coordinates[1]

    if get_char == "w":
        y_position -= 1
    elif get_char == "s":
        y_position += 1
    elif get_char == "a":
        x_position -= 1
    elif get_char == "d":
        x_position += 1
    return [x_position, y_position]


def map_with_updated_hero_pos(get_char, level_map, old_hero_coordinates, new_hero_coordinates):
    
    if get_char in ["w", "s", "a", "d"]:
        updated_hero_pos = hero_move(level_map, old_hero_coordinates, new_hero_coordinates)     
        return updated_hero_pos
    return level_map


def hero_move(level_map, old_hero_coordinates, new_hero_coordinates):
    
    delete_old_here_pos = delete_old_hero_position(level_map, old_hero_coordinates)
    updated_level_map = place_hero_new_pos(delete_old_here_pos, new_hero_coordinates)
    return updated_level_map


def delete_old_hero_position(level_map, old_hero_coordinates):

    x_position = old_hero_coordinates[0]
    y_position = old_hero_coordinates[1]
    level_map[y_position][x_position] = " "
    return level_map
