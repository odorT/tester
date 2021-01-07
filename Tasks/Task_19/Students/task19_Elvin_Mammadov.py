uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
lst=[]
def password(password):
    for i in password:
        if i in uppercase:
            lst.append(1)
        elif i in lowercase:
            lst.append(2)
        else:
            lst.append(3)
    if 1 in lst:
        if 2 in lst:
            if 3 in lst:
                print("strong")
            else:
                print('moderate')
        elif 3 in lst:
            if 2 in lst:
                print("strong")
            else:
                print('moderate')
        else:
            print("weak")
    elif 2 in lst:
        if 1 in lst:
            if 3 in lst:
                print("strong")
            else:
                print('moderate')
        elif 3 in lst:
            if 1 in lst:
                print("strong")
            else:
                print('moderate')
        else:
            print("weak")
    else:
        print('weak')
password(input())
