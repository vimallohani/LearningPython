#Dry principle says do not repeat same lines.
#This is better version of exercise_three_eight_guessing_game

import random
rand=random.randint(1,100)
counter=1
gameover=False                  #just to make logic for a gammer point of view
while not gameover:
    num=int(input("Please guess a number between 1 and 100 :"))
    if num== rand:
        print(f"You win: Total guess : {counter}")
        gameover=True
        break
    else:                                   #now this below code is not repeating line
        if num>rand:
            print("Too high") 
        else:
            print("Too low")
        counter+=1
        continue