from words import words
import random
from hangmanpics import HANGMANPICS
print("Welcome to Dylan's Hangman Game\n")

wrong_guesses = 0
#print("Wrong guesses: " + str(wrong_guesses))

chosen_word = random.choice(words)
chosen_letters = list(chosen_word)

displayed_letters = list()
for letter in chosen_letters:
    displayed_letters.append('_')

word_length = len(chosen_word)

def display_letters():
    mystring = ''
    for letter in displayed_letters:
        mystring = mystring + letter
    print("Word: " + mystring)
    current_display = mystring
display_letters()

def user_lost():
    print("You lost, fucking loser. How does it feel u little bitch")

def user_won():
    print("Congratz, you won ye little shitbag")

while True:
    choice = input("\nChoose a letter: ")
    if choice in chosen_letters:
        print('\nWell done, you guessed correctly!')
        print(HANGMANPICS[0])
        i = 0
        for letter in chosen_letters:
            if letter == choice:
                displayed_letters[i] = choice
            i = i + 1

        current_display = ''
        for letter in displayed_letters:
            current_display = current_display + letter
        display_letters()
        if current_display == chosen_word:
            print("CORRECT!")
            user_won()
            break
    else:
        wrong_guesses = wrong_guesses +1
        print('WRONG, stupid ass bitch')
        #print(HANGMANPICS[])

    if wrong_guesses == 10:
        print("ur shit, you're out of guesses, the word was:", chosen_word)
        user_lost()
        break



