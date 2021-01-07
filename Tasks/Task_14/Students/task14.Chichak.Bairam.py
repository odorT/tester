def Convert(string): 
    li = list(string.split(" ")) 
    return li 
  

string3 = str(input())
list3 = Convert(string3)
count = 0
for i in list3:
  if len(i)>count:
    count = len(i)
    word = i

index = list3.index(word)
print(word)
print(index)