name='Harshit'

#center method is used to apply delemeter at front and end. but start from end
# end ->start->end->start......

print(name.center(9,"*"))   #*Harshit*               here 9=length of name (7)+two starts(2)
print(name.center(8,"*"))   #Harshit* 
print(name.center(12,"*"))   #**Harshit***



#Q: Input name from user and add **** from starting and ending postion
val=input("Please provide your name :")
print(val.center(len(val)+8,"*"))