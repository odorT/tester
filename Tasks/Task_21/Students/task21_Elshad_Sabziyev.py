#user_in >>> user input

import string

def case_counter(user_in):

    a=0
    b=0
    
    for char in user_in:
        if char in string.ascii_uppercase:
            a+=1

    for char in user_in:
        if char in string.ascii_lowercase:
            b+=1

    print(a)
    print(b)
    

user_in = input()
case_counter(user_in)
