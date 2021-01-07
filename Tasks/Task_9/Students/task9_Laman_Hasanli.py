"""
Leap year: 
Any year that is divisible by 400 is a leap year.
Of the remaining years, any year that is divisible by 100 is not a leap year. 
Of the remaining years, any year that is divisible by 4 is a leap year. 
All other years are not leap years.

Write a program that reads a year (integer) from the user and
displays a message indicating whether it is a leap year.
"""
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
elif year % 100 == 0 :
    print("not leap year")
else:
    print("not leap year")
