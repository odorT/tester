#user_in >>> user input
def panagram_checker(user_in):

    user_in = user_in.lower()
    
    chars = 'abcdefghijklmnopqrstuvwxyz'

    for char in chars:
        if char not in user_in:
            a = 'not pangram'
            break
        else: a = 'pangram'
    print(a)
   
user_in = input()
panagram_checker(user_in)
