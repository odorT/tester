def words(t): #t=text
    t.sort()
    s=''
    for i in t:
        s=s+i+'-'
    print(s[:-1])
text=input().split('-')
words(text)
