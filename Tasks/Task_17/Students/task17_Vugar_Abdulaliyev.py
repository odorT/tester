#Task17

n = int(input())
c = 0
d = 0
for i in range(2, n+1):
  if n%i == 0:
    c = n/i
    d += c

if d == n:
  print(True)
else:
  print(False)
