my=[]
while True:
    s=input()
    if s in my:
        continue
    if s=="":
        break
    my.append(s)
for i in my:
    print(i)
