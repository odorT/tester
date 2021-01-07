from math import*
num=input().split(' ')
a=int(num[0])
b=int(num[1])
c=int(num[2])
def max_num(t,y,u):
    print(max(t,max(y,u)))
max_num(a,b,c)
