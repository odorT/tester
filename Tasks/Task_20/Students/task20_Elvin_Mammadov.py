lst=[]
Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def sentence(a):
    for i in a:
        i=i.upper()
        lst.append(i)
    for n in lst:
        if n in Alphabet:
            Alphabet.remove(n)
        else:
            pass

sentence(input())

if Alphabet==[]:
    print('panagram')
else:
    print('not panagram')
