n = input().split()
longest = n[0]
for i in range(len(n)):
    if len(n[i]) > len(longest):
        longest = n[i]
print(longest)
print(i)

    
  
