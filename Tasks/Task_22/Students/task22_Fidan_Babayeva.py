def myfunc(a):
    lst = [n for n in a.split('-')]
    lst.sort()
    print('-'.join(lst))
a = input()
myfunc(a)
