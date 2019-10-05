#function inside function
# Take three inputs and return the greatest
# def greatest(a,b,c):
#     if c>a and c>b:
#         return c
#     else:
#         if a>b and a>c:
#             return a 
#         return b

# num1,num2,num3=input("Enter three numbers separated by comma :").split(",")
# print(f"{greatest(int(num1),int(num2),int(num3))}")
def bigsmall(a,b):
    if a>b:
        return a
    else:
        return b
def newgreatest(a,b,c):
    print(f"Bigger is {bigsmall(bigsmall(a,b),c)}")

newgreatest(10,150,99)