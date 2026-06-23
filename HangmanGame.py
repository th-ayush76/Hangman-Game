# Author: Ayush
# Project: Hangman Game
# Description: A simple text-based Hangman game for internship task

import random

# Predefined word list - Space Theme
WORDS = ["galaxy", "rocket", "saturn", "nebula", "comet"]

# Hangman ASCII art stages (6 = start, 0 = game over)
HANGMAN_STAGES = [
    """
   -----
   |   |
   |   O
   |  /|\\
   |  / \\
   |
""",
    """
   -----
   |   |
   |   O
   |  /|\\
   |  /
   |
""",
    """
   -----
   |   |
   |   O
   |  /|\\
   |
   |
""",
    """
   -----
   |   |
   |   O
   |  /|
   |
   |
""",
    """
   -----
   |   |
   |   O
   |   |
   |
   |
""",
    """
   -----
   |   |
   |   O
   |
   |
   |
""",
    """
   -----
   |   |
   |
   |
   |
   |
""",
]

def display_state(word, guessed_letters, wrong_guesses):
    """Display the current game state."""
    print(HANGMAN_STAGES[6 - wrong_guesses])

    display_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )
    print(f"  Word: {display_word}")
    print(f"  Wrong guesses left: {6 - wrong_guesses}")

    wrong_letters = [l for l in guessed_letters if l not in word]
    if wrong_letters:
        print(f"  Incorrect letters: {', '.join(sorted(wrong_letters))}")
    print()

def play_hangman():
    """Main game function."""
    print("=" * 40)
    print("       Welcome to Hangman!")
    print("         Made by Ayush")
    print("       Theme: Outer Space 🚀")
    print("=" * 40)

    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong:
        display_state(word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 You won! The word was: '{word}'")
            break

        guess = input("  Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠️  Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print(f"  ⚠️  You already guessed '{guess}'. Try another.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅ Nice! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            remaining = max_wrong - wrong_guesses
            print(f"  ❌ Wrong! '{guess}' is not in the word. {remaining} guess(es) left.\n")

    else:
        display_state(word, guessed_letters, wrong_guesses)
        print(f"💀 Game over! The word was: '{word}'")

    print()
    again = input("Play again? (y/n): ").strip().lower()
    if again == "y":
        print()
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye! 👋")

# Entry point
if __name__ == "__main__":
    play_hangman()