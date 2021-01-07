#Task15

n = int(input())
d = n
b = ""


while 10**100>n>0:
  n = d
  n %= 1000
  b = "," + str(n) + str(b)
  d //= 1000
  if n == 0:
    b = str(b).replace(",", "", 2)
    b = str(b).replace("0", "", 1)
    print(b)
    break
