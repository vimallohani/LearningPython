#create function and reverse it
#there are three methods which work same
def rev1(l):
    return(l[::-1])

def rev2(l):
    r=[]
    lnt=len(l)
    for i in range(lnt):
        r.append(l.pop())
    return r

def rev3(l):
    l.reverse()
    return l



num=[1,2,3,4,5]
st=['a','b','c','d','e']
print(rev1(num))
print(rev2(st))
print(rev3(num))