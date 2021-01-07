#Height > float h
#Weight > float w
#Body Mass Index > float bmi (round 2)
h = float(input())
w = float(input())
bmi = w/(h**2)
print(round(bmi, 2))
