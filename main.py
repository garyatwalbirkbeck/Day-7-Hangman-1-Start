#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

import random

chosen_word = random.choice(word_list)

len_chosen_word = len(chosen_word)
no_of_blanks = len_chosen_word
no_of_turns = 6

list_dashes_chosen_word = []

for i in range(len_chosen_word):
    list_dashes_chosen_word.append("_")

print(f"The word you need to guess is : {list_dashes_chosen_word}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

end_of_game = False

while end_of_game != True and no_of_turns != 0:
    print("You have " + str(no_of_turns) + " turns left")
    print(stages[6 - no_of_turns])

    guess = input(f"Guess a letter: ").lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    for position in range(len_chosen_word):
        letter = chosen_word[position]
        if letter == guess:
            list_dashes_chosen_word[position] = letter
            no_of_turns = no_of_turns + 1

    print(list_dashes_chosen_word)
    no_of_turns = no_of_turns - 1

    if "_" not in list_dashes_chosen_word:
        end_of_game = True

if end_of_game == True:
    print("You Win")
elif no_of_turns == 0:
    print("You Lose")
