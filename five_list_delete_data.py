num=[0,1,2,3,4,5,6,7]

num.pop()   # if no argument then delete last data ie 7    index
print(num)      #[0, 1, 2, 3, 4, 5, 6]

num.pop(2)
print(num)      #[0, 1, 3, 4, 5, 6]

#delete operator del
del num[1]      #deleted first index data
print(num)      #[0, 3, 4, 5, 6]

#remove operator : if we dont know particular data is at which index
#It will throw an error if data will be not in list
#if there will be two same element it will drop only first element not second
num.remove(5)   #deleted data 5
print(num)      #[0, 3, 4, 6]