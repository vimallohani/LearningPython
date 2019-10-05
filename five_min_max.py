#min and max function in list
#find the greatest difference function

n=[5,60,2]
print(max(n))
print(min(n))

def greatest_diff(l):
    return max(l)-min(l)

print(greatest_diff(n))