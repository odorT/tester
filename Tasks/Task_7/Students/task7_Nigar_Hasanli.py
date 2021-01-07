number = int(input())

last_digit = number % 10   # 4

x = number % 100
x = x - last_digit
third_digit = x/10   # 3


second_digit = number % 1000
y = second_digit % 100
second_digit = second_digit - y
second_digit = second_digit/100  # 2


z = number % 1000
first_digit = number - z
first_digit = first_digit / 1000

product = int(first_digit * second_digit * third_digit * last_digit)
print(product)








