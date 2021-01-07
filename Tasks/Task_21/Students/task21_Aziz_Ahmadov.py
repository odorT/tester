def count(l): #l=letter
    up=0
    low=0
    for i in l:
        for x in i:
            if x==x.upper():
                up+=1
            else:
                low+=1
    print(up)
    print(low)
text=input().split()
count(text)
