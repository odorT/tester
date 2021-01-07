def func(a, b, c):
    m = max(a, b, c)
    return m


x = input().split(' ')
a = int(x[0])
b = int(x[1])
c = int(x[2])
print(func(a, b, c))
