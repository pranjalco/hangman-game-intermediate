# Hangman Game

## Description
### Description:
This is a Python-based Hangman game that allows users to guess a randomly chosen word by inputting letters. The game tracks the user's progress, showing the word with correctly guessed letters and displaying a visual representation of lives left.
This game provides a fun and interactive way to practice Python logic, loops, conditionals, and string manipulation.

## Level
- **Level**: Intermediate
- **Skills:** Python, String Manipulation, Loops, Random Module, Conditionals, Lists, ASCII Art
- **Domain:** Game Development, Python Programming, Beginner Projects

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 2024-12-02

## Features
- Randomly selects a word from a predefined word list (`hangman_words.word_list`).
- Displays the word as underscores (`_`) initially, with correctly guessed letters revealed as the game progresses.
- Tracks the number of lives, which decrease with each incorrect guess.
- Displays ASCII art for visual feedback based on the remaining lives (`hangman_art.stages`).
- Prevents repeated guesses from being penalized.
- Ends when the player either guesses the entire word or runs out of lives, with a win or lose message displayed.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/hangman-game-intermediate.git

2. Navigate to the project directory:
   ```bash
   cd hangman-game-intermediate

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `hangman.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python hangman.py
     ```
   - **By Double-Clicking**: You can double-click `hangman.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

