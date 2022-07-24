from random import *


options = ["rock" , "paper" , "scissors"]
print("WELCOME TO THE GAME")
round_selected = int(input("how many round do you want to play? (tie did not count) : "))

round_counter = 0
player_round_counter = 0
computer_round_counter = 0


while round_counter < round_selected:

    player_selection = input("enter your choice (rock , paper or scissors) : ").lower()
    computer_selection = choice(options)

    print("you :" + player_selection + "\n"+ "computer : " + computer_selection)

    if computer_selection == "rock" and player_selection == "paper":
        print("you won the round!")
        round_counter += 1
        player_round_counter +=1
        print("your points : {}".format(player_round_counter))
        print("computer points :{}".format(computer_round_counter))

    elif computer_selection == "paper" and player_selection == "scissors" :
        print("you won the round!")
        round_counter += 1
        player_round_counter += 1
        print("your points : {}".format(player_round_counter))
        print("computer points :{}".format(computer_round_counter))

    elif computer_selection == "scissors" and player_selection=="rock" :
        print("you won the round!")
        round_counter += 1
        player_round_counter += 1
        print("your points : {}".format(player_round_counter))
        print("computer points :{}".format(computer_round_counter))

    elif computer_selection == "rock" and player_selection == "scissors":
        print("you lost the round!")
        round_counter += 1
        computer_round_counter += 1
        print("your points : {}".format(player_round_counter))
        print("computer points :{}".format(computer_round_counter))

    elif computer_selection == "paper" and player_selection == "rock":
        print("you lost the round!")
        round_counter += 1
        computer_round_counter += 1
        print("your points : {}".format(player_round_counter))
        print("computer points :{}".format(computer_round_counter))

    elif computer_selection == "scissors" and player_selection == "rock":
        print("you lost the round!")
        round_counter += 1
        computer_round_counter += 1
        print("your points : {}".format(player_round_counter))
        print("computer points :{}".format(computer_round_counter))

    else:
        print("tie!")
        print("your points : {}".format(player_round_counter))
        print("computer points :{}".format(computer_round_counter))

if player_round_counter > computer_round_counter :
    print("you win the game")
    print("your points :")
    print(player_round_counter)
    print("computer points :")
    print(computer_round_counter)

else :
    print("you lost the game")
    print("your points :")
    print(player_round_counter)
    print("computer points :")
    print(computer_round_counter)