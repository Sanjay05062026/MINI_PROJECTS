import random
from Hangman_Art import *
from WordLists import word_list
print(logo)
lives = 6

chosen_word = random.choice(word_list)

display = "_" * len(chosen_word)
game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    # Show lives and the word so far at the start of every round
    print(f"\n------------------- LIVES LEFT : {lives} -------------------")
    print(display)
    guess = input("Guess a letter\n").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please type a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue
    guessed_letters.append(guess)

    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the word. You lost a life")

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(stages[6 - lives])

    # Win / lose messages come last, after the final drawing
    if lives == 0:
        game_over = True
        print(f"The correct word is {chosen_word}")
        print(f"Letters you guessed: {', '.join(guessed_letters)}")
        print(lose_logo)
    elif "_" not in display:
        game_over = True
        print(display)
        print(win_logo)
