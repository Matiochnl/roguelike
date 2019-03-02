import random


def hotcold():
    print("type a number ".upper() + "(1-100)")

    numbers = random.randint(1,100)
    #print(numbers)
    answer = 0
    listt = []
    while answer != numbers:
        try:
            answer = int(input("type a number:"))
            listt.append(answer)
            if answer == numbers:
                file = open("/home/mateusz/codecool/roguelike_v2/ascii_art/congrats.txt", 'r')
                print(file.read())
                file.close()
            elif answer < numbers:
                print("type bigger number")
            elif answer > numbers:
                print("type smaller number")
        except ValueError:
            print("type number , not letter")
        if len(listt) == 20:
            print("loser hahahah")
            break


def rock():
    t = ["Rock", "Paper", "Scissors"]
    computer = t[randint(0, 2)]
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
        computer = t[randint(0, 2)]
    if len(how_many) >= 3:
        if how_many.count("W") > how_many.count("L"):
            print("YOU WIN")
            file = open("/home/mateusz/codecool/roguelike_v2/ascii_art/congrats.txt", 'r')
            print(file.read())
            file.close()
            return True
        else:
            print("YOU LOSE")
            file = open("/home/mateusz/codecool/roguelike_v2/ascii_art/lose.txt", 'r')
            print(file.read())
            file.close()
            return False