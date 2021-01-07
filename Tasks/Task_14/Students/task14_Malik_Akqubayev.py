word_list = input().split

longest_string = ""
for word in word_list:
    if (len(word)) > len(longest_string):
        longest_string = word
print(longest_word)
print(word_list.index(longest_string))
        
    
