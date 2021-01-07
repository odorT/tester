from string import ascii_letters
def string(a): #a=text
    condition=True
    global i
    for i in ascii_letters:
        if i.lower() not in a and i.upper() not in a:
            print("not pangram")
            condition=False
            break
    if condition:
        print("pangram")
text=input()
string(text)
