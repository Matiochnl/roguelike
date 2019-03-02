import os
import ui
import data_manager
import time


def main_menu():
    answer = ""

    while not answer:
        os.system("clear")
        print(data_manager.load_ascii_art("ascii_art/castle.txt"))
        answer = ui.main_menu_options()

        if answer == '1':
            back = ui.input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '2':
            back = ui.input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '3':
            print(data_manager.load_ascii_art("howtoplay.txt"))
            back = ui.input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '4':
            print(data_manager.load_ascii_art("authors.txt"))
            back = ui.input("Press Enter to go back to main menu.")
            answer = ""
        elif answer == '5':
            quit()
        else:
            ui.input("You must choose a valid option. Press Enter to go back to main menu.")
            answer = ""


def main():
    main_menu()


if __name__ == "__main__":
    main()
