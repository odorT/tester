def f(x): 
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in a: 
        if i in x.lower(): 
            return True
  
    return False
      
b = input()
if(f(b) == True): 
    print("pangram") 
else: 
    print("not pangram")
