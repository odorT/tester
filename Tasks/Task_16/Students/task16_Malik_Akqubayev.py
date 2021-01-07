list1 = []
word = input()
while word:
  if word not in list1:
    list1.append(word)

  word = input()
for word in list1:
  print(word)
