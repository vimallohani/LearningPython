#list : ordered collection of items
# we can store anything in list  int float string.....

a=[1,2,3,4,5]
print(a)

word=["raj", "Kumar",'Thakur']
print(word)

mixed=[1,2,3,'raju','chaha',4,6,None]
print(mixed)
#to access element of list
print(mixed[4])
print(mixed[3:5])
mixed[2]=3.0            #change element 3 with 3.0
print(mixed)            #[1, 2, 3.0, 'raju', 'chaha', 4, 6, None]
mixed[1:]=['one','two']
print(mixed)            #[1, 'one', 'two']

