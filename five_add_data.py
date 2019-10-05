#some methods to add data to list
fruits=['mango','orange']
fruits.insert(1,'banana')
print(fruits)               #['mango', 'banana', 'orange']

fruits1=['grapes','guava']

fruitesTotal=fruits+fruits1
print(fruitesTotal)         #['mango', 'banana', 'orange', 'grapes', 'guava']

#extend method
fruits.extend(fruits1)
print(fruits)               #['mango', 'banana', 'orange', 'grapes', 'guava']

#difference between extend and append

fruits.append(fruits1)      # list inside list
print(fruits)               #['mango', 'banana', 'orange', 'grapes', 'guava', ['grapes', 'guava']]