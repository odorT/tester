#Task14

n = input().split()


b = len(n)
c = 0
d = 0
for i in range(b):
  a = len(n[i])
  if a > c:
    c = a
    d = i

print(n[d])
print(d)


