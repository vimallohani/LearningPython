#input name from user and a character with comma separated
# find the length of name and in next line total count of character #case insensitive

a,b=input("Please provide your username and letter separated by comma : ").split(",")
print(f"length of provided name is :{len(a)}")
print(f"count of {b} is {a.upper().count(b.upper())}")





#test print above statement and {test} in between 
print(f"count {{test}} of {b} is {a.upper().count(b.upper())}")