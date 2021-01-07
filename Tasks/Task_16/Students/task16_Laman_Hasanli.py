lists = []
while True:
    l = input()
    if l:
        lists.append(l)
    else:
        break;

temp = []
for l in lists:
    if l not in temp:
        temp.append(l)

lists = temp

for l in lists:
    print(l)
