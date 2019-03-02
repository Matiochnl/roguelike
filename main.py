import os
import rogal
import highstore
import time


def main_menu():




    file = open("/home/szymon/codecool/PYTHON/roguelike_v2/ascii_art/castle1.txt", 'r')
    print(file.read())

    print("""
    1.create character and start a game
    2.highscores
    3.how to play
    4.authors
    5.exit""")


    answer = ""
    #os.system("clear")

    while answer != 4:
        answer = input("Type a number: ")

        if answer == '1':
            rogal.add_character_stats()
            rogal.get_player_position()
            start = time.time()
            rogal.controls()
            end = time.time()
            game_time = int(end) - int(start)
            highstore.print_score(rogal.stats, game_time)
            answer = ""

        if answer == '2':
            back = input("press anything to go back to main menu")
            answer = ""

        if answer == '3':
            file = open("/home/szymon/codecool/PYTHON/roguelike_v2/howtoplay.txt", 'r')
            print(file.read())
            back = input("press anything to go back to main menu")
            answer = ""


        if answer == '4':
            file = open("/home/szymon/codecool/PYTHON/roguelike_v2/ascii_art/Authors.txt", 'r')
            print(file.read())
            file.close()
            back = input("press anything to go back to main menu")
            answer = ""

        if answer == '5':
            quit()


def main():
    main_menu()


if __name__ == "__main__":
    main()
