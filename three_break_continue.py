
for i in range (11):
    if i==5:
        continue    # will not go down and i=6 continue execution
    if i==9:
        break       # at 9 it will break
    print(i)

    #below code will print 0 1 2 3 4 6 7 8