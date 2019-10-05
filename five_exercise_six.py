# create a function which accept a list you need to find how many list inside list
#[1,2,3,[1,2],["4,5,6"]]-------->2

def listcount(l):
    s=type(l)
    i=0
    for x in l:
        if type(x)==list:
            i+=1
    return i


num=[1,2,3,[1,2],["4,5,6"],['a','x']]
print(listcount(num))