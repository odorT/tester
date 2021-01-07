my_list = list (input().split(" "))
check = 0
uzun = " "
for i in my_list:
   if len(i)>check:
       check = len(i)
       uzun = i
print (uzun)

for i in range(len(my_list)):
    if uzun == my_list [i]:
        print(i)
        
