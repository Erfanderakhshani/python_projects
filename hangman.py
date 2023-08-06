import random
from hangman_words import words
import string
# You have to guess the word before you die
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word and ' ' in word:
        word = random.choice(words)

    return word.upper()

def hang_man():
    word = get_valid_word(words)
    word_letters = set(word)  # Each letter in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10
    # user input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Please guess letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in the word')
        elif user_letter in used_letters:
            print('You have already used this character, Please try again...')

        else:
            print('This is invalid character, Please try again...')

    if lives == 0:
        print('sorry you died, the word was ', word)
    else:
        print('congrats!!, you guess right and the word was ', word)
print(hang_man())