#Task 19

import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
numbers = ['0','1','2','3','4','5','6','7','8','9']

password = str(input())
low = False
upper = False
num = False

for i in password:
  if i in lowercase:
    low = True
  elif i in uppercase:
    upper = True
  elif i in numbers:
    num = True

if low == True and upper == False and num == False :
  print("weak")
elif upper == True and low == False and num == False:
  print("weak") 
elif num == True and upper == False and low == False:
  print("weak")
elif low == True and upper == True and num == False:
  print("moderate")
elif low == True and upper == False and num == True:
  print("moderate")
elif low == False and upper == True and num == True:
  print("moderate")
elif low == True and upper == True and num == True:
  print("strong")
