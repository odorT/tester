""" 
You are given 3 integer numbers – A, B, and C. You should print the
multiplication table for the number A in the range of [B, C].
"""
A = int(input())
B = int(input())
C = int(input())
for i in range(B, C + 1):
    print(A * i)
