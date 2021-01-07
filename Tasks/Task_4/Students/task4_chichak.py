cost = float(input())

tax = round(cost * 18 / 100, 2)
cashback = round(tax * 10 / 100, 2)

print(tax)
print(cashback)