# Exercise - watch coco
# ask user name and age
# if user name starts with 'a' & 'A' and age>10 then
# print you can watch coco else you can't watch coco


name,age=input("Hey! Please provide your name and age separated by comma :").split(",")
if name=="" or int(age)<1:
    print("Access denied!!")
elif (name[0]=='a' or name[0]=='A') and int(age)>10:
    print("You can watch coco")
else:
    print("You can't watch coco")