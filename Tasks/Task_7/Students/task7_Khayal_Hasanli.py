i = int(input())
n1 = i//1000
n2 = (i-(1000*n1))//100
n3 = (i-(1000*n1+100*n2))//10
n4 = i%10
f = n1*n2*n3*n4
print(f)
