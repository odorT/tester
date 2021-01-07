#print ("Please enter a 4-digit number")
num = int(input())

dig1 = num%10
rem = num//10
dig2 = rem%10
rem = rem //10
dig3 = rem%10
rem = rem//10
dig4=rem%10
product = dig1 * dig2 * dig3 * dig4
#print("The product of the digits of the number you have entered is",
print(product)
