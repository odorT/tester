xs = []

while True:
    info = input()
    if info == "":
        break
    xs.append(info)

xs.reverse()
for i in xs:
    if xs.count(i):
        a = xs.count(i)
        for dovr in range(1,a):
            print(xs)
            xs.remove(i)
        
xs.reverse()



for i in xs:
    print(i)
