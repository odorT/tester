#Task 21

import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
lowch = 0
upch = 0
word = input()

for i in word:
  if i in lower:
    lowch+=1
  elif i in upper:
    upch += 1

print(upch)
print(lowch)
