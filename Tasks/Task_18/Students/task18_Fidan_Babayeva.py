def maximum(a, b, c):
    return n
list1 = input().split(" ")
a = int(list1[0])
b = int(list1[1])
c = int(list1[2])
if a > b and a > c:
    n = a
elif b > a and b > c:
    n = b
elif c > a and c > b:
    n = c

print(maximum(a, b, c))
