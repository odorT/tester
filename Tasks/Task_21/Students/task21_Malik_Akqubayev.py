def function(a):
    for i in a:
        b = sum(1 for i in a if i.isupper())
        c = sum(1 for i in a if i.islower())
    print(b)
    print(c)
a = input()
function(a)

