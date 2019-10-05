# Number guessing game 
# Make a variable winning_number : make it random
# ask user to guess a number and if he guess right then winning_number
# if user guess below print too low
# else guess too high

#generating a random number
import random

num=random.randint(1,100)

winning_number=int(input("Please guess a number :"))
print("defined number is :{}".format(num))
if winning_number==num:
    print("Yeh! You Win!!!!!!!!")
else:
    if winning_number>num:
        print("You guessed too high!!")
    else:
        print("You guessed too low!!")