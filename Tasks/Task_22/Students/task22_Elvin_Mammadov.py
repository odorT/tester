a=input()
result=0
lst=[]
for i in a:
    if i=='-':
        lst.append(result)
    result+=1
index=0
lst1=[]
for i in lst:
    c=a[int(index):int(i)]
    index=i+1
    lst1.append(c)
lst1.append(a[int(lst[-1]+1):int(len(a))])
lst1.sort()
for i in lst1:
    if lst1.index(i)==len(lst1)-1:
        print(i)
    else:
        print(i,end='-')
