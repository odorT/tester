uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase='abcdefghijklmnopqrstuvwxyz'
def func(word):
    upperresult=0
    lowerresult=0
    for i in word:
        if i in uppercase:
            upperresult+=1
        elif i in lowercase:
            lowerresult+=1
    print(upperresult)
    print(lowerresult)
func(input())
