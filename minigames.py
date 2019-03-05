import random
import data_manager
import ui
import os
import engine


def hotcold(map_iterator, char_stats, character):
    

    numbers = random.randint(1, 100)
    print(numbers)
    answer = 0
    if character == "&":
        damage = 5
    else:
        damage = 10
    while answer != numbers and char_stats["HP"] > 0:
        ui.print_character_statistics(char_stats)
        print("Type a number ".upper() + "(1-100)")
        if character == "&":
            print(data_manager.load_ascii_art("ascii_art/mob.txt"))
        else:
            print(data_manager.load_ascii_art("ascii_art/finalbos.txt"))
        try:
            answer = int(input("Type a number:"))
            os.system("clear")
            if answer == numbers:
                print(data_manager.load_ascii_art("ascii_art/congrats.txt"))
            elif answer < numbers:
                print("Type bigger number")
                char_stats["HP"] = char_stats["HP"] - damage
            elif answer > numbers:
                print("Type smaller number")
                char_stats["HP"] = char_stats["HP"] - damage
        except ValueError:
            print("Type number, not letter")


def rock():
    t = ["Rock", "Paper", "Scissors"]
    computer = t[random.randint(0, 2)]
    how_many = []
    while len(how_many) != 3:
        player = input("Rock, Paper, Scissors?").capitalize()
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                how_many.append("L")
                print(how_many)
            else:
                print("You win!", player, "smashes", computer)
                how_many.append("W")
                print(how_many)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                how_many.append("L")
                print(how_many)
            else:
                print("You win!", player, "covers", computer)
                how_many.append("W")
                print(how_many)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                how_many.append("L")
                print(how_many)
            else:
                print("You win!", player, "cut", computer)
                how_many.append("W")
                print(how_many)
        else:
            print("That's not a valid play. Check your spelling!")
        computer = t[random.randint(0, 2)]
    if len(how_many) >= 3:
        if how_many.count("W") > how_many.count("L"):
            print(data_manager.load_ascii_art("ascii_art/congrats.txt"))
            return True
        else:
            prin(data_manager.load_ascii_art("ascii_art/lose.txt"))
            return False
