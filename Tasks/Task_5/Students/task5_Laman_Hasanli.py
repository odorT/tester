height = float(input())
weight = float(input())
# Compute the BMI
BMI = weight / height**2; #or BMI = weight / pow(height,2);
print(round(BMI, 2))
