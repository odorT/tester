#Task 22

word = input().split("-")
wordlist = word
worlist = wordlist.sort()
order = ""
for i in wordlist:
  order+=i+"-"
print(order)
