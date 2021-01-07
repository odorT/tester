#value-added tax = 18%
#cashback = 10% of value-added tax
#cost of meal > float cost
#value-added tax > float tax (round 2)
#cashback > float back (round 2)
cost=float(input())
tax=cost*18/100
back=tax*10/100
print(round(tax, 2))
print(round(back, 2))
