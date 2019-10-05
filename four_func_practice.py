#create a function that take name as input and return last character
def last_char(name):
    print(name[-1])     #efficient is to use return statement
last_char("Hello")

# def odd_even(num):        #not efficient coding
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"

def odd_even(num):      #efficient coding
    if num%2==0:
        return "even"
    return "odd"

print(odd_even(15))

# def is_even(num):     #not efficient here
#     if num%2==0:
#         return True
#     return False

def is_even(num):
    return num%2==0

print(is_even(25))