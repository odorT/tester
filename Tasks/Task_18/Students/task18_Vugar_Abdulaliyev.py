#Task 18

a = input().split()
c = 0
for i in a:
  if int(i) > c:
    c = int(i)
print(c)
