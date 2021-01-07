def myfunc(a):
    return result
a = input()
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in a or chr(ord(i) - 32) in a:
        result = "pangram"
    else:
        result = " not pangram"
print(myfunc(a))
