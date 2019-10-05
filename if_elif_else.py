#show ticket pricing
# 1 to 3 -> free
# 4 to 10 -> 150
# 11 to 60 -> 250
# above 60 -> 200
age=int(input("Please provide your age :"))
# print(age)
# if age>=1 and age<=3:
#     print("Ticket is free for you!!!")
# elif age>=4 and age<=10:
#     print("Ticket is 150 Rs!")
# elif age>=11 and age<=60:
#     print("Ticket is 250 Rs!")
# elif age>60:
#     print("Ticket is 200 Rs!")
# else:
#     print("Your age is not authenticated!!")
if 1<=age<=3:
    print("Ticket is free for you!!!")
elif 4<=age<=10:
    print("Ticket is 150 Rs!")
elif 11<=age<=60:
    print("Ticket is 250 Rs!")
elif age>60:
    print("Ticket is 200 Rs!")
else:
    print("Your age is not authenticated!!")