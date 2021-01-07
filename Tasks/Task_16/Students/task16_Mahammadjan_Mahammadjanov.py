n = 1
mylist = []
while n!=0:
    a = input()
    if a not in mylist and a != "":
        mylist.append(a)
    if a=="":
        n = 0
for i in mylist:
    print(i)