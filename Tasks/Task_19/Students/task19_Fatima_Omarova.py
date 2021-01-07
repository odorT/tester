def func(s):
    a = any(i.isdigit() for i in s)
    b = any(i.isupper() for i in s)
    c = any(i.islower() for i in s)
    if a + b + c == 1:
        return 'weak'
    elif a + b + c == 2:
        return 'moderate'
    else:
        return 'strong'
s = input()
print(func(s))