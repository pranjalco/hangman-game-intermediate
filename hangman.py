import random
import hangman_words
import hangman_art

"""
# Project: Hangman Game
### Description:
This is a Python-based Hangman game that allows users to guess a randomly chosen word by inputting letters. The game 
tracks the user's progress, showing the word with correctly guessed letters and displaying a visual representation 
of lives left.

Features:
    - Randomly selects a word from a predefined word list (`hangman_words.word_list`).
    - Displays the word as underscores (`_`) initially, with correctly guessed letters revealed as the game progresses.
    - Tracks the number of lives, which decrease with each incorrect guess.
    - Displays ASCII art for visual feedback based on the remaining lives (`hangman_art.stages`).
    - Prevents repeated guesses from being penalized.
    - Ends when the player either guesses the entire word or runs out of lives, with a win or lose message displayed.

This game provides a fun and interactive way to practice Python logic, loops, conditionals, and string manipulation.

# Level: Intermediate
Author: Pranjal Sarnaikpi
Date: 2024-12-02
"""

word_list = hangman_words.word_list
stages = hangman_art.stages

lives = 6
print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"----------------------------{lives}/6 LIVES LEFT----------------------------")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"This letter is already guessed, the letter is {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, it is not present in word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"The correct word is {chosen_word}!")
            print(f"----------------------------YOU LOSE----------------------------")

    if "_" not in display:
        game_over = True
        print("----------------------------YOU WIN----------------------------")

    print(stages[lives])
