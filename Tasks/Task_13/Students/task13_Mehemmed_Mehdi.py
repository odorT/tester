a  = int(input())

b = str(a)

k = -1
j = len(b)

for i in b:
    k += 1
    j -= 1

    if j == 0:
        print("palindrome")
        
    elif b[k] != b[j]:
        print("not palindrome")
        break
