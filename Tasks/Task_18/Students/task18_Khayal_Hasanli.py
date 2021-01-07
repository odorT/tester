def max_v(a, b, c):
    maxx=a
    if maxx<b:
        maxx=b
    if maxx<c:
        maxx=c
        
    return maxx

num1, num2, num3 = map(int, input().split())
print(max_v(num1, num2, num3))
