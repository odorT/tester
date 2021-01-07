a = input()
x = 0
y = 0
for i in a: 
          
    # For lower letters 
    if (ord(i) >= 97 and
        ord(i) <= 122): 
        x += 1
  
    # For upper letters 
    elif (ord(i) >= 65 and
            ord(i) <= 90): 
        y += 1
print(y)
print(x)
