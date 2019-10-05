#create function that take an input as list
#find the common elements [[1,2,3,4],[1,2,6,7,4]]------->[1,2,4]

def fun_common(l):
    common=[]
    for i in l[0]:
        if i in l[1]:
            common.append(i)
    return common

common=[[1,2,3,4],[1,2,6,7,4]]
print(fun_common(common))

