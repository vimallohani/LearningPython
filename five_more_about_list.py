#generate list with the help of range function
num=list(range(1,11))
print(num)                      #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#something more about pop method
#pop method returns the value it pop
print(num.pop())                #10
print(num)                      #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#index method   : to find particular value location
print(num.index(6))             #5   by default it search for only first value
x=[1,2,3,4,1,6,7]
print(x.index(1,3,6))           #4    (value,start,end)

#pass list to a function
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(num))