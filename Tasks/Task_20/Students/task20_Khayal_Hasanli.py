c = 0
import string
l = [l for l in string.ascii_lowercase]


def pangram(sentence):
    global c
    for i in l:
       if i in sentence:
           c+=1
    if c>=26:
        print('pangram')
    else:
        print('not pangram')

s = input()
pangram(s.lower())
        
