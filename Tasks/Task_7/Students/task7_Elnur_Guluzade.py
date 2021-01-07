a = int(input("Type a four-digit integer:"))
x = (a%10)*(a//10%10)*(a//100%10)*(a//1000%10)
print("The product of the digits in number:", x)
