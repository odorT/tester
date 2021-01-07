s=input()
my_dict={'q': 0, 'w': 0,'e': 0,'r': 0,'t': 0,'y': 0,'u': 0,'i': 0,'o': 0,'p': 0,'a': 0,'s': 0,'d': 0,'f': 0,'g': 0,'h': 0,'j': 0,'k': 0,'l': 0,'z': 0,'x': 0,'c': 0,'v': 0,'b': 0,'n': 0,'m': 0 }
def pangram(a):
    for i in a:
        if i==' ':
            continue
        if i.lower() in my_dict:
            my_dict[i.lower()]=1
    t=sum(my_dict.values())
    print(t)
    print(a)
    print(my_dict)
    if t==26:
        print("pangram")
    else:
        print("not pangram")
pangram(s)
