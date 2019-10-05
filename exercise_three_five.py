# Ask name from user.
# find the occorance of each character and count 
# for vimal Lohani    v:1 i:2 m:1.........
# actual solution is at last my solution is leangthy
name=input("Please provide your full name :")

i=j=0
k=len(name)
print(k)
count=1
val=''
while i<k:
    val=name[i]
    j=i+1
    # print(val)
    # print(f"value of i:{i} and j :{j} and val is {val} and k is {k}")
    while j<k:
        if(val==name[j]):
            count+=1
        j+=1
        # print(f"value of j :{j}")

    j=0
    # i+=1
    # print(name)
    print(f"val {val} : {count}")
    count=1
    name=name.replace(val,"")
    k=len(name.replace(val,""))
    val=""

