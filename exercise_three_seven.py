#get the name from the user and count each character with for loop


name=input("Please provide your full name : ")
string=''
for i in range(len(name)):
    if name[i] not in string:
        string=string+name[i]
        print(f"Count of {name[i]} :{name.count(name[i])}")

    