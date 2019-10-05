# print each character of shweta
name="Shweta Pandey"
for i in range(len(name)):
    print(name[i])

#same working
for i in name:
    print(i)

#1234--->1+2+3+4
num=input("Enter few digit number: ")
j=0
for i in num:
    j+=int(i)
print(j)