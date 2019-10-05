first=0
last=1
add=0
print (first,"\n", last)
for i in range(1,10):
    add=last+first
    first=last
    last=add
    print(add)

