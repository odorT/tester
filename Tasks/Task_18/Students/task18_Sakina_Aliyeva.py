def max_value (a, b, c):
    my_list = []
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    maximum = 0
    for i in my_list:
        if maximum<i:
            maximum=i
    return maximum

myInput = input().split()
a = int(myInput [0])
b = int(myInput [1])
c = int(myInput [2])
print(max_value (a,b,c))
