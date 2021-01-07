def hss(s):
    l = s.split('-')
    l.sort()
    n = ''

    for i in l:
        n+=i
        n+='-'

    n=n.strip('-')
    print(n)

s = input()
hss(s)
