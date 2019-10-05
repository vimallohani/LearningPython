#create a function that accept list which return a list where elements are square

def sqr(l):
    # print(lengthl)
    r=[]
    for element in l:
        # lengthe=len(element)
        print(element)
        r.append(element**2)
    return r


li=[1,2,3,4,5]
print(sqr(li))
