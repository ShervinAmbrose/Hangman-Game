import random

word = open('word_list.txt').read().splitlines()


# Generates random word
def random_word_generator():
    random_word = random.choice(word)
    return random_word


# Checks twice if the random word is greater than 4 letters
def get_word():
    my_word = random_word_generator()
    if len(my_word) > 4:
        return my_word
    else:
        my_word = random_word_generator()
        if len(my_word) > 4:
            return my_word
        else:
            my_word = random_word_generator()
            return my_word


# Initialization
one_word_str = get_word().upper()
# one_word_str = 'MATTRESS'
answer_str = ('_' * len(one_word_str)).upper()
answer_lst = list(answer_str)
one_word_lst = list(one_word_str)
letters = len(answer_str)
user_input_lst = []
print('########## WELCOME TO THE HANGMAN GAME ##########')


# Selecting the no_of_tries
no_of_tries = 5
if len(one_word_str) == 5 or len(one_word_str) == 6:
    no_of_tries = 5
if len(one_word_str) == 7 or len(one_word_str) == 8:
    no_of_tries = 6
if len(one_word_str) == 9 or len(one_word_str) == 10:
    no_of_tries = 8
if len(one_word_str) == 11 or len(one_word_str) == 12:
    no_of_tries = 10
if len(one_word_str) == 13 or len(one_word_str) == 14:
    no_of_tries = 12
if len(one_word_str) == 15 or len(one_word_str) == 16:
    no_of_tries = 14
if len(one_word_str) == 17 or len(one_word_str) == 18:
    no_of_tries = 16
if len(one_word_str) == 19 or len(one_word_str) == 20:
    no_of_tries = 18
print('########## YOU HAVE ' + str(no_of_tries) + ' GUESSES ##########')
for k in answer_lst:
    print(k, end='  ')
print('')
print('It is a ' + str(len(one_word_str)) + ' letter word')
while no_of_tries > 0:
    # Checking the user input
    user_input = input('Guess a letter: ').upper()
    while user_input in user_input_lst or len(user_input) > 1 or not (user_input.isalpha()):
        if user_input in user_input_lst:
            print('You had already entered this letter')
        if len(user_input) > 1:
            print('Enter a single letter only')
        if not user_input.isalpha():
            print('Enter alphabets only')
        user_input = input('Please re-enter a letter: ').upper()
    user_input_lst.append(user_input)
    # Get the index position of the input
    index_user_input = [i for i, x in enumerate(one_word_lst) if x == user_input]
    length_index = len(index_user_input)
    # If index position present
    if length_index > 0:
        print(user_input + ' is present in the word')
        for i in range(length_index):
            answer_lst[index_user_input[i]] = user_input
            i -= 1
        for j in answer_lst:
            print(j, end='  ')
        print('')
        if no_of_tries > 1:
            print('' + str(no_of_tries) + ' guesses remaining')
        else:
            print('' + str(no_of_tries) + ' guess remaining')
        if answer_lst == one_word_lst:
            print('YOU WON!')
            print('Congratulations! you guessed the correct word')
            break
    else:
        print(user_input + ' is not present in the word')
        no_of_tries -= 1
        for j in answer_lst:
            print(j, end='  ')
        print('')
        if no_of_tries > 1:
            print('' + str(no_of_tries) + ' guesses remaining')
        if no_of_tries == 1:
            print('' + str(no_of_tries) + ' guess remaining')
    if no_of_tries == 0:
        print('Better luck next time!')
        print('The word was: ' + one_word_str)
        break
