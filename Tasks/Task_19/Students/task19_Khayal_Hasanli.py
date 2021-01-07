import string
low_l = [l for l in string.ascii_lowercase]
upp_l = [l for l in string.ascii_uppercase]
digits = [l for l in string.digits]

l = 0
u = 0
d = 0

def p_check(pw):
    global l, u, d
    for c in pw:
        if c in low_l:
            l = 1
        if c in upp_l:
            u = 1
        if c in digits:
            d = 1
    if ((l==0 and u==0 and d==1) or (l==0 and d==0 and u==1) or (d==0 and u==0 and l==1)):
        print('weak')
    elif (l==u==d==1):
        print('strong')
    else:
        print('moderate')

password = input()
p_check(password)
        
