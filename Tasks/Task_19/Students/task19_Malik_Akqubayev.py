def printStrongNess(input_string):
    n = len(input_string)
    hasLower = False
    hasUpper = False
    hasDigit = False
    normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    for i in range(n):
        if input_string[i].islower():
            hasLower = True
        if input_string[i].isupper():
            hasUpper = True
        if input_string[i].isdigit():
            hasDigit = True
    if hasLower and hasUpper and hasDigit:
        print("Strong") 
    elif (hasLower and hasUpper) or (hasLower and hasDigit) or (hasUpper and hasDigit):
        print("Moderate") 
    else:
        print("Weak") 

 

	
input_string = input()
	
printStrongNess(input_string) 


