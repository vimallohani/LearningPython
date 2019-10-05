#count
#sort method
#sorted function
#reverse
#clear
#copy
fruits=['apple','mango','banana','guava','mango','banana']
print(fruits.count('banana'))             #2

fruits.sort()
print(fruits)
num=[19,15,18,5,9,7]
num.sort()          #it will sort the list
print(num)

#if you dont want to sort the list but just print sorted list
num=[19,15,18,5,9,7]
print(sorted(num))
print(num)

num.clear()         #it will empty the list
print(num)

num=[19,15,18,5,9,7]
num_copy=num.copy()
num_copy1=num
print(num_copy)
print(num_copy1)