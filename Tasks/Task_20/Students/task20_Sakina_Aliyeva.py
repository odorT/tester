def pangram(a):
    import string

    mySet = set ()
    for i in a:
        mySet.add (i)

    check=0
    for a in mySet:
        if a in string.ascii_lowercase:
            check +=1

    if check == 26:
        print("pangram")
    else:
        print("not pangram")
        
pangram(input())
