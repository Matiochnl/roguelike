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


def move_hero():
    old_coordinates = ui.hero_position
    new_pos = []
    level_map = data_manager.get_maps_from_file("maps/level1.txt")
    level_map[old_coordinates[1]][old_coordinates[0]] = "@"
    ui.show_map(level_map)
    obstackles = ["#", "B", "R"]
    
    while True:
        get_char = get_char_in_terminal()
        if get_char == "w":
            os.system("clear")
            level_map[old_coordinates[1]][old_coordinates[0]] = " "
            new_pos.insert(0, old_coordinates[0])
            new_pos.insert(1, old_coordinates[1] - 1)
            if level_map[new_pos[1]][new_pos[0]] not in obstackles:
                old_coordinates.insert(0, new_pos[0])
                old_coordinates.insert(1, new_pos[1])
                os.system("clear")
                level_map[new_pos[1]][new_pos[0]] = "@"
                ui.show_map(level_map)
            else:
                level_map[old_coordinates[1]][old_coordinates[0]] = "@"
                ui.show_map(level_map)

        elif get_char == "s":
            os.system("clear")
            level_map[old_coordinates[1]][old_coordinates[0]] = " "
            new_pos.insert(0, old_coordinates[0])
            new_pos.insert(1, old_coordinates[1] + 1)
            if level_map[new_pos[1]][new_pos[0]] not in obstackles:
                old_coordinates.insert(0, new_pos[0])
                old_coordinates.insert(1, new_pos[1])
                os.system("clear")
                level_map[new_pos[1]][new_pos[0]] = "@"
                ui.show_map(level_map)
            else:
                level_map[old_coordinates[1]][old_coordinates[0]] = "@"
                ui.show_map(level_map)
        elif get_char == "a":
            os.system("clear")
            level_map[old_coordinates[1]][old_coordinates[0]] = " "
            new_pos.insert(0, old_coordinates[0] - 1)
            new_pos.insert(1, old_coordinates[1])
            if level_map[new_pos[1]][new_pos[0]] not in obstackles:
                old_coordinates.insert(0, new_pos[0])
                old_coordinates.insert(1, new_pos[1])
                os.system("clear")
                level_map[new_pos[1]][new_pos[0]] = "@"
                ui.show_map(level_map)
            else:
                level_map[old_coordinates[1]][old_coordinates[0]] = "@"
                ui.show_map(level_map)
        elif get_char == "d":
            os.system("clear")
            level_map[old_coordinates[1]][old_coordinates[0]] = " "
            new_pos.insert(0, old_coordinates[0] + 1)
            new_pos.insert(1, old_coordinates[1])
            if level_map[new_pos[1]][new_pos[0]] not in obstackles:
                old_coordinates.insert(0, new_pos[0])
                old_coordinates.insert(1, new_pos[1])
                os.system("clear")
                level_map[new_pos[1]][new_pos[0]] = "@"
                ui.show_map(level_map)
            else:
                level_map[old_coordinates[1]][old_coordinates[0]] = "@"
                ui.show_map(level_map)

