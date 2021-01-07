#print ("Please, enter the cost of your meal:")
cost = int (input())
tax = cost *0.18
tax = round (tax, 2)
cashback = tax *0.1
cashback = round (cashback, 2)
#print ("The amount of your tax is:",)
print(tax)
#print ("The amount of your cashback is:",)
print(cashback)
