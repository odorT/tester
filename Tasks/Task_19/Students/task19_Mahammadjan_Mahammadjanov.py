number_list = ["0","1","2","3","4","5","6","7","8","9"]

def pwd_checker(password):
    uppr = 0
    lwr = 0
    nmbr = 0
    for i in password:
        if i in number_list:
            nmbr += 1
        elif i.upper() == i:
            uppr += 1
        elif i.lower() == i:
            lwr += 1
        

    if uppr and lwr and nmbr:
        return "strong"
    elif uppr and lwr or uppr and nmbr or lwr and nmbr:
        return "moderate"
    else:
        return "weak"
    

print(pwd_checker(input()))

