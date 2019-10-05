#fabinachhi series

def fab(num):
    a=0
    b=1
    if num==1:
        print(a)
    elif num==2:
        print(a,b)
    else:
        print(a,b, end=" ")
        for i in range(num-2):
            c=a+b
            a=b
            b=c
            print(b, end=" ")


val=int(input("Please enter a series num to print a series of fibonachhi :"))
fab(val)