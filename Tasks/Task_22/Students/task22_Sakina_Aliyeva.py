def sorting (a):
    myList = []
    for i in a:
        myList.append(i)

    myList.sort()

    for i in range(len(myList)):
        if i==len(myList)-1:
            print(myList[i])
        else:
            print(myList[i], end='-')

sorting (input().split('-'))
