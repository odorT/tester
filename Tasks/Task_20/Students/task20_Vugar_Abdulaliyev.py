#Task 20

import string

alpha = list(string.ascii_lowercase)
word = input().lower()
word_list = []

for i in word:
  word_list.append(i)

check =  all(item in word_list for item in alpha)


if check is True:
  print("pangram")
else:
  print("not pangram")
