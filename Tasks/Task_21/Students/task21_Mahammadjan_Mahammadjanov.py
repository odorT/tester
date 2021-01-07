def calculator(text):
    lwr = 0
    uppr = 0
    for i in text:
        if i.lower() == i and i != " ":
            lwr += 1
        if i.upper() == i and i != " ":
            uppr += 1
        
    return str(uppr)+"\n"+str(lwr)


print(calculator(input()))