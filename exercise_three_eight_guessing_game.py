import random

rand=random.randint(1,100)
# print("Random no is {}".format(rand))
counter=1
while True:
# for i in range (100):
    num=int(input("Please guess a number between 1 and 100 :"))
    if num== rand:
        print(f"You win: Total guess : {counter}")
        break
    elif num>rand:
        print("Too high")
        counter+=1
        continue
    elif num<rand:
        print("Too low")
        counter+=1
        continue