x=[[1,2],[3,4],[5,6]]
print(x)

y=zip(*x)
for i in y:
    print(i)






matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)] 
for row in matrix: 
    print(row) 
print("\n") 
t_matrix = zip(*matrix) 
for row in t_matrix: 
    print (row )
