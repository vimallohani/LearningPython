#create a function that take a list and reverse each element
#["abc","gef"]-------------->["cba","feg"]

def revlist(l):
    r=[]
    for i in l:
        r.append(i[::-1])
    return r



testlist=["abc","def","ghi"]
print(revlist(testlist))
