# Ask name from user.
# find the occorance of each character and count 
# for vimal Lohani    v:1 i:2 m:1.........
# actual solution is at last my solution is leangthy
name=input("Please provide your full name :")
lenth=len(name)
i=0
string=''
while i<lenth:
    if name[i] not in string:
        print(f"{name[i]} counts :{name.count(name[i])}")
        string=string+string+name[i]
    i+=1