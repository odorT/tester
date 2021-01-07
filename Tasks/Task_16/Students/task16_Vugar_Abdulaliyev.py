#Task16

wordlist = []
word = ""
n = 0

while 0 <= n <= 100:
  word = input()
  n += 1
  if word not in wordlist:
    wordlist.append(word)
  if word == "":
    break

b = len(wordlist)

for i in range(b):
  print(wordlist[i])
