#take two input from a user and return the bigger one

def bigsmall(a,b):
    if a>b:
        return a
    else:
        return b

num1,num2=input("Please enter two numbers separated by comma").split(",")

print(f"bigger number is :{bigsmall(int(num1),int(num2))}")