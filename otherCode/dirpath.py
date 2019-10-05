import os
l='E:\Pictures'
for path in os.listdir(l):
    print(path)
    cpath=os.path.join(l,path)
    print (cpath)
