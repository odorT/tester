a = int(input())
a1 = str(a)
uzunluq = len(a1)

k = uzunluq % 3

dovrlerin_sayi = 0
for i in a1:
    dovrlerin_sayi += 1
    print(i, end = "")
    
    if dovrlerin_sayi == uzunluq:
        print(end  = "")
    elif dovrlerin_sayi % 3 ==k:
        print(end = ",")