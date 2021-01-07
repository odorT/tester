a = input().split()

print(max(a, key=len))
print(a.index(max(a, key=len)))
