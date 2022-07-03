import random
import time
time.sleep(1)
#card = random.randint(1, 21)
#FUTUR UPDATE PSEUDO
#METTRE MODE SOLITAIRE AVEC UNE I.A1
#MODE RESEAU CONTRE DES IA


player = input("how many player are playing :")

#partie de 1 personnes

if player == "1":

    if player == "1":

        time.sleep(1)
        print("you must be 2 to play")
        ia = str(input("Do you wanna play solo [y/n]:"))
        if ia == "n":

            while ia == "n":
                print("you must be 2 to play")
                time.sleep(1)
                ia = str(input("Do you wanna play solo [y/n]:"))

                if ia == "n":
                    player = input("how many player are playing :")
                    time.sleep(1)
                else:
                    input()

                time.sleep(1)

        if ia == "y":
            print("downloading IA please wait")
            time.sleep(1)
            print("starting IA ...")
            time.sleep(1)
            print("let's choose the difficulty :")
            time.sleep(1)
            print("1 easy")
            time.sleep(1)
            print("2 medium")
            time.sleep(1)
            print("3 hard")
            time.sleep(1)
            difficulty = int(input("enter the difficulty :"))

            if difficulty == "1":
                time.sleep(1)
                print("you choose easy ")
                difficulty = 1

            if difficulty == "2":
                time.sleep(1)
                print("you choose medium")
                difficulty = 2

            if difficulty == "3":
                time.sleep(1)
                print("you choose hard")
                difficulty = 3

#PREMIER TIRAGE

    number_player1 = random.randint(1, 21)
    IA_player1 = random.randint(1, 21)
    time.sleep(1)
    print("player 1 have ", number_player1)
    time.sleep(2)
    print("IA have", IA_player1)
    time.sleep(2)

#DEUXIEME TIRAGE IA

    print("IA goes first")
    time.sleep(2)

#IA rejoue car <15

    if IA_player1 < 15:
        IA_player1 = IA_player1 + random.randint(1, 21)
        time.sleep(1)
        print("IA have", IA_player1,)

#IA ne rejoue pas >15

    if IA_player1 > 15:
        print("IA dont play again too risky")
        time.sleep(2)

    if IA_player1 > 21:
        time.sleep(1)
        print("IA loose let's see if you do it better")

    else:
        time.sleep(1)
        print("IA finish with", IA_player1,)

#DEUXIEME TOUR JOUEUR

    print("your turn")
    time.sleep(2)

    print("you have", number_player1,)
    time.sleep(1)
    answer = str(input("do you wanna try to take another card [y/n] :"))

    if answer == "y":
        number_player1 = random.randint(1, 21) + number_player1
        time.sleep(1)
        print("you have now", number_player1,)

    if number_player1 > 21:
        time.sleep(1)
        print("sorry you have more than 21")
        time.sleep(1)
        print("you loose")

    if number_player1 < 21:
        time.sleep(1)
        print("gg you you finish with", number_player1)

    if answer == "n":
        time.sleep(1)
        if number_player1 > 21:
            time.sleep(1)
            print("sorry you have more than 21")
            time.sleep(1)
            print("you loose")

        if number_player1 < 21:
            time.sleep(1)
            print("gg you you finish with", number_player1)

    if IA_player1 < 21 and number_player1 < 21:

        if IA_player1 < number_player1:
            time.sleep(1)
            print("gg you win the game")
            input()

        if IA_player1 > number_player1:
            time.sleep(1)
            print("sorry you didn't win the match")
            input()

        if IA_player1 == number_player1:
            time.sleep(1)
            print("there an egality you must go to goulag now")




############################################################################################################################################################################
############################################################################################################################################################################

if player == "2":
    psd_1 = input("enter player one name :")
    psd_2 = input("enter player two name :")

    if psd_2 == psd_1:

        while psd_2 == psd_1:

            print("the two name can't be the same :")
            psd_1 = input("enter player one name :")
            psd_2 = input("enter player two name :")

    else:
        print("")

    number_player1 = random.randint(1, 21)
    number_player2 = random.randint(1, 21)
    time.sleep(1)
    print("player 1 have ", number_player1)
    time.sleep(1)
    print("player 2 have", number_player2)

############################################################################################################################################################################
############################################################################################################################################################################

    time.sleep(1)
    print("turn to 1")
    time.sleep(1)
    print(psd_1, "you have ", number_player1)
    time.sleep(1)
    second_try_1 = str(input("do you wanna take a second card [y/n]:"))

    if second_try_1 == "y":
        number2_player1 = random.randint(1, 21)
        final_number1 = number2_player1 + number_player1
        time.sleep(1)
        print("you have",final_number1)

        if final_number1 > 21:
            difference = final_number1 - 21
            time.sleep(1)
            print("sorry you have",final_number1 ,"more than 21")
            win2 = 2

        if final_number1 < 21:
            time.sleep(1)
            print("gg ", psd_1," you still in course")
            win1 = 1
############################################################################################################################################################################
############################################################################################################################################################################

    time.sleep(1)
    print("turn to 2")
    time.sleep(1)
    print(psd_2, "you have ", number_player2)
    second_try_2 = str(input("do you wanna take a second card [y/n]:"))


    if second_try_2 == "y":
        number2_player2 = random.randint(1, 21)
        final_number2 = number2_player2 + number_player2
        time.sleep(1)
        print("you have", final_number2)

        if final_number2 > 21:
            difference2 = final_number2 - 21
            time.sleep(1)
            print("sorry you have", difference2, "more than 21")
            win2 = 0

        if final_number2 < 21:
            time.sleep(1)
            print("gg", psd_2, "you finish with", final_number2)
            win2 = 1

    if  final_number2 > final_number1 > 21:
        print("gg", psd_1,"you just win")

    if final_number1 > final_number2 > 21:
        print("gg", psd_2, "you win")

    if final_number1 == final_number2:
        print("equality there's no winner")

############################################################################################################################################################################
############################################################################################################################################################################

if player == "3":

    psd_1 = input("enter player one name :")
    psd_2 = input("enter player two name :")
    psd_3 = input("enter player three name :")

    if psd_2 == psd_3 or psd_2 == psd_1 or psd_1 == psd_3:

        while psd_2 == psd_3 or psd_2 == psd_1 or psd_1 == psd_3:

            print("the three name can't be the same :")
            psd_1 = input("enter player one name :")
            psd_2 = input("enter player two name :")
            psd_3 = input("enter player three name :")

    else:
        print("")

    number_player1 = random.randint(1, 21)
    number_player2 = random.randint(1, 21)
    number_player3 = random.randint(1, 21)
    print("player 1 have ", number_player1)
    time.sleep(1)
    print("player 2 have", number_player2)
    time.sleep(1)
    print("player 3 have", number_player3)

    time.sleep(1)
    print("turn to 1")
    time.sleep(1)
    print(psd_1, "you have ", number_player1)
    time.sleep(1)
    second_try_1 = str(input("do you wanna take a second card [y/n]:"))

    if second_try_1 == "y":
        number2_player1 = random.randint(1, 21)
        final_number1 = number2_player1 + number_player1
        time.sleep(1)
        print("you have",final_number1)

        if final_number1 > 21:
            difference = final_number1 - 21
            time.sleep(1)
            print("sorry you have",final_number1 ,"more than 21")
            win2 = 2

        if final_number1 < 21:
            time.sleep(1)
            print("gg ", psd_1," you still in course")
            win1 = 1
############################################################################################################################################################################
############################################################################################################################################################################

    time.sleep(1)
    print("turn to 2")
    time.sleep(1)
    print(psd_2, "you have ", number_player2)
    second_try_2 = str(input("do you wanna take a second card [y/n]:"))


    if second_try_2 == "y":
        number2_player2 = random.randint(1, 21)
        final_number2 = number2_player2 + number_player2
        time.sleep(1)
        print("you have", final_number2)

        if final_number2 > 21:
            difference2 = final_number2 - 21
            time.sleep(1)
            print("sorry you have", difference2, "more than 21")
            win2 = 0

        if final_number2 < 21:
            time.sleep(1)
            print("gg", psd_2, "you finish with", final_number2)
            win2 = 1

############################################################################################################################################################################
############################################################################################################################################################################


    time.sleep(1)
    print("turn to 3")
    time.sleep(1)
    print(psd_3, "you have ", number_player3)
    time.sleep(1)
    second_try_1 = str(input("do you wanna take a second card [y/n]:"))

    if second_try_1 == "y":
        number2_player3 = random.randint(1, 21)
        final_number3 = number2_player3 + number_player3
        time.sleep(1)
        print("you have", final_number1)

        if final_number3 > 21:
            difference = final_number3 - 21
            time.sleep(1)
            print("sorry you have", final_number3, "more than 21")
            win2 = 2

        if final_number3 < 21:
            time.sleep(1)
            print("gg ", psd_3, " you still in course")
            win1 = 1


    if  final_number2 > final_number1 > 21:
        print("gg", psd_1,"you just win")

    if final_number1 > final_number2 > 21:
        print("gg", psd_2, "you win")

    if final_number3 < final_number2 > 21:

        if final_number3 > final_number1 < 21:
            print("gg", psd_3,"you win !")

        else:
            print("coming soon")

    if final_number1 == final_number2:
        print("equality there's no winner")


############################################################################################################################################################################
############################################################################################################################################################################

if player == "4":

    psd_1 = input("enter player one name :")
    psd_2 = input("enter player two name :")
    psd_3 = input("enter player three name :")
    psd_4 = input("enter player four name :")

    if psd_2 == psd_3 or psd_2 == psd_1 or psd_1 == psd_3 or psd_4 == psd_1 or psd_4 == psd_3 or psd_4 == psd_2:

        while psd_2 == psd_3 or psd_2 == psd_1 or psd_1 == psd_3 or psd_4 == psd_1 or psd_4 == psd_3 or psd_4 == psd_2:

            print("the three name can't be the same :")
            psd_1 = input("enter player one name :")
            psd_2 = input("enter player two name :")
            psd_3 = input("enter player three name :")
            psd_4 = input("enter player four name :")
    else:
        print("")

    number_player1 = random.randint(1, 21)
    number_player2 = random.randint(1, 21)
    number_player3 = random.randint(1, 21)
    number_player4 = random.randint(1, 21)
    print("player 1 have ", number_player1)
    time.sleep(1)
    print("player 2 have", number_player2)
    time.sleep(1)
    print("player 3 have", number_player3)
    time.sleep(1)
    print("player 4 have", number_player4)

    print("turn to 1")
    time.sleep(1)
    print(psd_1, "you have ", number_player1)
    time.sleep(1)
    second_try_1 = str(input("do you wanna take a second card [y/n]:"))

    if second_try_1 == "y":
        number2_player1 = random.randint(1, 21)
        final_number1 = number2_player1 + number_player1
        time.sleep(1)
        print("you have",final_number1)

        if final_number1 > 21:
            difference = final_number1 - 21
            time.sleep(1)
            print("sorry you have",final_number1 ,"more than 21")
            win2 = 2

        if final_number1 < 21:
            time.sleep(1)
            print("gg ", psd_1," you still in course")
            win1 = 1
############################################################################################################################################################################
############################################################################################################################################################################

    time.sleep(1)
    print("turn to 2")
    time.sleep(1)
    print(psd_2, "you have ", number_player2)
    second_try_2 = str(input("do you wanna take a second card [y/n]:"))


    if second_try_2 == "y":
        number2_player2 = random.randint(1, 21)
        final_number2 = number2_player2 + number_player2
        time.sleep(1)
        print("you have", final_number2)

        if final_number2 > 21:
            difference2 = final_number2 - 21
            time.sleep(1)
            print("sorry you have", difference2, "more than 21")
            win2 = 0

        if final_number2 < 21:
            time.sleep(1)
            print("gg", psd_2, "you finish with", final_number2)
            win2 = 1

############################################################################################################################################################################
############################################################################################################################################################################


    time.sleep(1)
    print("turn to 3")
    time.sleep(1)
    print(psd_3, "you have ", number_player3)
    time.sleep(1)
    second_try_1 = str(input("do you wanna take a second card [y/n]:"))

    if second_try_1 == "y":
        number2_player3 = random.randint(1, 21)
        final_number3 = number2_player3 + number_player3
        time.sleep(1)
        print("you have", final_number1)

        if final_number3 > 21:
            difference = final_number3 - 21
            time.sleep(1)
            print("sorry you have", final_number3, "more than 21")
            win2 = 2

        if final_number3 < 21:
            time.sleep(1)
            print("gg ", psd_3, " you still in course")
            win1 = 1

############################################################################################################################################################################
############################################################################################################################################################################


    time.sleep(1)
    print("turn to 4")
    time.sleep(1)
    print(psd_4, "you have ", number_player4)
    time.sleep(1)
    second_try_4 = str(input("do you wanna take a second card [y/n]:"))

    if second_try_4 == "y":
        number2_player4 = random.randint(1, 21)
        final_number4 = number2_player4 + number_player4
        time.sleep(1)
        print("you have", final_number1)

        if final_number4 > 21:
            difference = final_number4 - 21
            time.sleep(1)
            print("sorry you have", final_number4, "more than 21")
            win2 = 2

        if final_number4 < 21:
            time.sleep(1)
            print("gg ", psd_4, " you still in course")
            win1 = 1


    if  final_number2 > final_number1 > 21:
        print("gg", psd_1,"you just win")

    if final_number1 > final_number2 > 21:
        print("gg", psd_2, "you win")

    if final_number3 < final_number2 > 21:

        if final_number3 > final_number1 < 21:
            print("gg", psd_3,"you win !")

        else:
            print("coming soon")

    if final_number1 == final_number2:
        print("equality there's no winner")



else:
    print("")