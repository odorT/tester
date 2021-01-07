n = int(input())
xs = []

for i in range(1, n+1 ):
    if n % i == 0:
        xs.append(i)

xs.pop(-1)

cem = 0

for bolen in xs:
    cem += bolen

if cem == n:
    print(True)
else:
    print(False)
