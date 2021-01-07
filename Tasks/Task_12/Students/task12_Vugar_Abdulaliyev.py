#Task 12

A = int(input())
B = int(input())
C = int(input())

if C > B:
  for i in range(B, C+1):
    D = A * i
    print(D)
elif B > C:
  for i in range(C, B+1):
    D = A * i
    print(D)
