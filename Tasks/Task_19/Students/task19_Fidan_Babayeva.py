def myfunc(s):
    result = 1
    for i in s:
        if i in "abcdefghijklmnopqrstuvwxyz":
            result *= 2
        elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result *= 3
        elif i in "0123456789":
            result *= 5
    if result % 2 == 0 and result % 3 == 0 and result % 5 == 0:
        strength = "strong"
    elif result % 2 == 0 and result % 3 == 0 and result % 5 != 0:
        strength = "moderate"
    elif result % 2 == 0 and result % 5 == 0 and result % 3 != 0:
        strength = "moderate"
    elif result % 3 == 0 and result % 5 == 0 and result % 2 != 0:
         strength = "moderate"
    else:
        strength = "weak"
    return strength
s = input()
print(myfunc(s))

        
    
    
