res=[]
while True:
    s=input().strip()
    if len(s)==0:
        break
    if s not in res:
        res.append(s)
for i in range(len(res)):
    print(res[i])
