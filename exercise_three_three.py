#exercise sum of n natural number
#take n value from user
#find sum from 1 to n

n=float(input("Please enter a value :"))
print(n)
sum=0
while n>0:
    sum+=n
    n-=1

print("Total value={}".format(sum))