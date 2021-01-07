def func(s):
    ans_up = 0
    ans_lo = 0
    for i in s:
        if i.isalpha() and i.islower():
            ans_lo += 1
        elif i.isalpha() and i.isupper():
            ans_up += 1
    return ans_up, ans_lo


s = input()
a = func(s)
print(a[0], a[1], sep='\n')
