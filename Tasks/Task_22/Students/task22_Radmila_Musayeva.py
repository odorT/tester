s=input()
def srt(s):
    a=s.split("-")
    t=""
    for i in sorted(a):
        t+=i
        t+="-"
    print(t[:-1])
srt(s)
