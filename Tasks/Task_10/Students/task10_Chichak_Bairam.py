#Task 10

side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

if side_1 == side_2 and side_2 == side_3 and side_1 == side_3:
  print("equilateral")
elif side_1 != side_2 and side_2 != side_3 and side_1 != side_3:
  print("scalene")
else:
  print("isosceles")