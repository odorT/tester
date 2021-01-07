def max_finder():
    x = input().split()
    x = [int(y) for y in x]
    x.sort()
    return x[2]


print(max_finder())
