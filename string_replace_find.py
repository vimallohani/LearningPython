string='she is very beautiful and she is good dancer.'

print(string.replace(" ","_"))  # she_is_very_beautiful_and_she_is_good_dancer.

#to replace only first is to was
print(string.replace("is","was",1))   #2 will replace both but 1 will replace only first one

######find
print(string.find("is")) #4 : it will give index of first character where string found

print(string.find("is",1))  #4 : start from first postion


#Q : If i have to find the position of 2nd "is" but we dont know the what is the postion of first "is"
print(string.find("is",(string.find("is"))+1))   #30