#user_in >>> user input
def word_sorter(user_in):

    word_list=[word for word in user_in.split('-')]
    word_list.sort()
    final_word = ''
    for i in word_list:
        final_word = final_word + '-' + i
    print(final_word.strip('-'))

user_in = input()
word_sorter(user_in)
