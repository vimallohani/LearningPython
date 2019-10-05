#and or operator

name,age=input("Please provide name and age separated by comma :").split(",")

if name=="vimal" and int(age)==28:
    print("Yes its you in 2018")
else:
    print("You are not vimal")
