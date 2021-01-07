info = input()

sonraki_info = info
xs = []

dovrlerin_sayi = 0
herflerin_sayi = 0
sozlerin_sayi = 0

for i in info:
    herflerin_sayi += 1
    dovrlerin_sayi += 1
    if i  == " ":
        sozlerin_sayi += 1
        
        a = herflerin_sayi - 1
        herflerin_sayi = 0
   
        info1 = info[:a]
        info = info[a+1:]
        xs.append(info1)
    elif len(sonraki_info) == dovrlerin_sayi:
        xs.append(info)

ys = []

for sozler in xs:
    ys.append(len(sozler))
index_soz = ys.index(max(ys))
print(xs[index_soz])
print(index_soz)
