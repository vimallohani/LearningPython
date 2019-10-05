#list inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]]            #3 items    and it is 2d list

print(matrix[0])                    #[1,2,3]
print(matrix[2])                    #[7,8,9]

''' print sublist
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]'''
for sublist in matrix:
    print(sublist)

#to get all elements

for sublist in matrix:
    for i in sublist:
        print(i)

#to get element 5
print(matrix[1][1])         #5

#to check the type of object
s="string"
print(type(s))
print(type(matrix))