import os
import time

import character_creation
import ui
import data_manager
import movement


def main_menu():
    answer = ""

    while not answer:
        os.system("clear")
        print(data_manager.load_ascii_art("ascii_art/castle.txt"))
        answer = ui.main_menu_options()

        if answer == '1':
            inventory = ["apple", "knife", "hatchet"]
            stats = character_creation.add_character_stats()
            level_map = data_manager.get_maps_from_file("maps/level1.txt")
            movement.move_hero(level_map, stats, inventory)
            back = input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '2':
            ui.print_game_instructions()
            back = input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '3':
            print(data_manager.load_ascii_art("howtoplay.txt"))
            back = input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '4':
            print(data_manager.load_ascii_art("authors.txt"))
            back = input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '5':
            quit()
        else:
            input("You must choose a valid option. Press Enter to go back to main menu.")
            answer = ""


def main():
    main_menu()


if __name__ == "__main__":
    main()
