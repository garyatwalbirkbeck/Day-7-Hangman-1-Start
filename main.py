#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random

chosen_word = random.choice(word_list)

len_chosen_word = len(chosen_word)
no_of_blanks = len_chosen_word
no_of_turns = len_chosen_word

list_dashes_chosen_word = []

for i in range(len_chosen_word):
    list_dashes_chosen_word.append("_")

print(f"The word you need to guess is : {list_dashes_chosen_word}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

while no_of_blanks != 0 and no_of_turns != 0:

    guess = input(f"Guess a letter: ").lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    for position in range(len_chosen_word):
        letter = chosen_word[position]
        if letter == guess:
            list_dashes_chosen_word[position] = letter
            no_of_blanks = no_of_blanks - 1
            no_of_turns = no_of_turns + 1

    print(list_dashes_chosen_word)
    no_of_turns = no_of_turns - 1
    print("You have " + str(no_of_turns) + " turns left")

if no_of_blanks == 0:
    print("You Win")
elif no_of_turns == 0:
    print("You Lose")
