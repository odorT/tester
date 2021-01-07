t= bool("TRUE")
mylist=[]
while t:
    element = input()
    t=bool(element)
    if t:
        mylist.append(element)

newlist=[]
for i in mylist:
    if i not in newlist:
        newlist.append(i)

print(newlist)
