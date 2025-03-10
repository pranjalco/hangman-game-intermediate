import random
import hangman_words
import hangman_art

"""
# Hangman Game
This Python-based Hangman game lets users guess a random word letter by letter while tracking progress and lives visually.

## Author
Pranjal Sarnaik

## Features
- Random word selection from a predefined list.  
- Reveals correctly guessed letters progressively.  
- Tracks lives and reduces them for incorrect guesses.  
- Displays ASCII art based on remaining lives.  
- Prevents penalties for repeated guesses.  
- Ends with a win/lose message based on game outcome.  

## Tech Stack
Python | Random Module | String Manipulation | Loops | Conditionals | Lists | ASCII Art

## How to Run
1. Clone the repo:  
   ```bash  
   git clone https://github.com/pranjalco/hangman-game-intermediate.git

2. Run:
    ```bash  
   python hangman.py
"""

word_list = hangman_words.word_list
stages = hangman_art.stages

lives = 6
print(hangman_art.logo)

chosen_word = random.choice(word_list)

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
