import os


def get_input(question):
    answer = input(question)

    return answer


def print_menu_option():
    print("""\n\nHammer of Justice:
(1). Play game
(2). How to play
(3). Highscore board
(4). Credits
(5). Exit""")
    answer = get_input("\nChoose option: ")
    return answer
