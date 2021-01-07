#Task 9

year = int(input())


if year%100==0 and year%400!=0:
  print("not leap year")
elif year%100==0 and year%400==0:
  print("leap year")
elif year%4==0 and year%100!=0:
  print("leap year")
else:
  print("not leap year")
