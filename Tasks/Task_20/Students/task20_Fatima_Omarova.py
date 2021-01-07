def func(s):
    if len(set([i.lower() for i in s if i.isalpha()])) >= 26:
        return 'pangram'
    else:
        return 'not pangram'


s = input()
print(func(s))
