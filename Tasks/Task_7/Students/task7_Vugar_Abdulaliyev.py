#task 7

from math import *


integer = int(input()) #1234

num1 = integer%10 
num2 = (integer%100 - num1) /10 
num4 = integer // 1000
num3 = integer//100 - num4 *10


print(num1 * num2 * num3 * num4)

