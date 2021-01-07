import string

low = [l for l in string.ascii_lowercase]
up = [u for u in string.ascii_uppercase]

l = 0
u = 0

def up_low(s):
    global u, l
    for i in s:
        if i in low:
            l+=1
        if i in up:
            u+=1
    print(u)
    print(l)

s = input()
up_low(s)
