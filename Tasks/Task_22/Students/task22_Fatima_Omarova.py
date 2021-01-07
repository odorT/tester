def func(s):
    c = [i for i in s.split('-')]
    c.sort()
    return '-'.join(c)


s = input()
print(func(s))
