n=input()
t=len(n)
t-=1
a=t//2
i=0
flag=0
while i<=t:
    if n[i]!=n[t-i]:
        print("not polindrome")
        flag=1
        break
    i+=1
if flag==0:
    print("polindrome")
