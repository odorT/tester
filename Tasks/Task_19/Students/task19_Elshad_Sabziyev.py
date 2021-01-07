import string

def pass_checker(password):

    pass_length = len(password)

    a=0
    b=0
    c=0
    
    for char in password:
        if char in string.digits:
            a+=1

    for char in password:
        if char in string.ascii_lowercase:
            b+=1

    for char in password:
        if char in string.ascii_uppercase:
            c+=1
            
    if a == pass_length or b == pass_length or c == pass_length:
        print('weak')

    elif (a + b == pass_length) or (a + c == pass_length) or (c + b == pass_length):
        print('moderate')
    else: print('strong')

password = input()
pass_checker(password)
