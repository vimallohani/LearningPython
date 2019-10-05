import random
no=int(input("How many passwords you want to generate : "))
len=int(input("Length of Passowrd : "))
pwd=''
str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
for j in range(no):
    for i in range(len):
        pwd+=random.choice(str)
    print(pwd)
    pwd=''

