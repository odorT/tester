import string
chars_lwr=string.ascii_lowercase

def pangram_checker(text):
    count = 0
    duplicate = []
    for i in text:
        if i.lower() in chars_lwr and i.lower() not in duplicate:
            duplicate.append(i.lower())
            count += 1
        else:
            pass

    if count == 26:
        return "pangram"
    else:
        return "not pangram"
    
print(pangram_checker(input()))




        