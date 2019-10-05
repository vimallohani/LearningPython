#Same program with for loop to add the digit of a number

num=input("Please input a number :")
sum=0
for i in range(len(num)):       #this will give 0 to len-1
    sum=sum+int(num[i])

print(f"Total is :{sum}")
