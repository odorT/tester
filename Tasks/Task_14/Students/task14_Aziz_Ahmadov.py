list1=input().split()
number=[]
for i in list1:
    number.append(len(i))
print(list1[number.index(max(number))])
print(number.index(max(number)))
