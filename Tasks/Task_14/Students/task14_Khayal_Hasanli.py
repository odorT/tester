n = input()
l = n.split()
m = l[0]
for i in l:
    if(len(i)>len(m)):
        m = i
print(m)
print(l.index(m))
    
