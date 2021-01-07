"""
Write a program that takes a positive integer and
counts the total number of digits in a number.
"""
num = int(input())
digit = 0
while(num > 0):
    num = num // 10  
    digit += 1
print(digit)
