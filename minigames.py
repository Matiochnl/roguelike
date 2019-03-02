import random
import data_manager
import ui


def hotcold():
    print("Type a number ".upper() + "(1-100)")

    numbers = random.randint(1, 100)
    answer = 0
    listt = []
    while answer != numbers:
        try:
            answer = int(ui.get_input("Type a number:"))
            listt.append(answer)
            if answer == numbers:
                print(data_manager.load_ascii_art("ascii_art/congrats.txt"))
            elif answer < numbers:
                print("Type bigger number")
            elif answer > numbers:
                print("Type smaller number")
        except ValueError:
            print("Type number, not letter")
        if len(listt) == 20:
            print("Loser hahahah")
            break


def rock():
    t = ["Rock", "Paper", "Scissors"]
    computer = t[random.randint(0, 2)]
    how_many = []
    while len(how_many) != 3:
        player = ui.get_input("Rock, Paper, Scissors?").capitalize()
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
