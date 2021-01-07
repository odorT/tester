words = input().split()
my_dictionary = {}
for i in words:
    my_dictionary[i] = len(i)
keys = list(my_dictionary.keys())
values = list(my_dictionary.values())
x = max(my_dictionary.values())
n = values.index(x)
answer_word = keys[n]
print(answer_word)
print(n)