def max_number(*args):
    return max(args)


numlist = input().split(' ')

a= int(numlist[0])
b= int(numlist[1])
c= int(numlist[2])

print(max_number(a, b, c))
