from random import *



print("welcome to the number game \n \n  ")

#chosing level 
choosen_level = input("please choose a level(easy , medium , hard)"
      "\nin easy the number is between (1,15)"
      "\nin medium the number is between (1,50)"
      "\nin hard the number is between (1,100)\n : ")

if choosen_level == "easy":
    secret_number = randint(1,15)
elif choosen_level == "medium":
    secret_number = randint(1,50)
elif choosen_level == "hard":
    secret_number = randint(1,100)
else:pass

first_try = int(input("enter your first try"))
if first_try == secret_number :
    print("YOU WIN!")
elif first_try != secret_number :
    print("its not true")
    # a simple hint for each mistake
    if choosen_level == "easy":
        if secret_number > 7 : print("the number is bigger than 7")
        else:
             print("the number is smaller than 7")
    elif choosen_level == "medium":
        if secret_number > 13:
                print("the number is bigger than 13")
        else:
                print("the number is smaller than 13")
    elif choosen_level== "hard":
        if secret_number > 50:
            print("the number is bigger than 50")
        else: print("the number is smaller than 50")
    secend_try  = int(input("enter your 2nd try: "))
    if secend_try == secret_number :
        print("YOU WIN!")
    else:
        print("its not true!")
        if secret_number % 2 == 0:
            print("the number is even")
        else:
            print("the number is odd")
        last_try = int(input("enter your last try"))
        if last_try == secret_number:
            print("YOU WIN!")
        else:
            print("YOU LOSE :( \n the number was {}".format(secret_number))
            



