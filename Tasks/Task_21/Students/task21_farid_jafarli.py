string=str(input())
def up_low(string):
    uppers = 0
    lowers = 0
    for char in string:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers +=1
    return uppers,lowers
print(up_low(string))
