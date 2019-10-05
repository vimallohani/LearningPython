#In python string is immutable

string="string"

#we can print different characters but we cant change it
print(string[1])   #t

# string[1]='T'   it will throw an error even replace method we can print change but we can not change 

string.replace('t',"T")               #will not do anything
print(string.replace('t',"T"))         #will print sTring
print(string)                           #string