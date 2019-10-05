#odd even list
#create function that take list as input
# [1,2,3,4,5,6,7,8,9] ---------->[[1,3,5,7,9],[2,4,6,8]]

def fun_evenodd(l):
    r=[]
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    r.append(odd)                   # we can directly return [odd,even]
    r.append(even)
    return r

num=[1,2,3,4,5,6,7,8,9]
print(fun_evenodd(num))