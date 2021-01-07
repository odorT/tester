from math import *

four_digit_integer=int (input())
a= floor(four_digit_integer/1000)
b= floor(four_digit_integer/100)
b= b-a*10
c= floor(four_digit_integer/10)
c= c-(a*100+b*10)
d= floor(four_digit_integer)
d= d- (a*1000+ b*100+c*10)

print (a*b*c*d)
