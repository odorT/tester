l = list()
while True:
    n = input()
    if(n==""):
        break
    if(n not in l):
        l.append(n)
for i in l:
    print(i)
