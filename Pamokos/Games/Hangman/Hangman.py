import random
import os


with open("Words.txt", "r") as file:
    words = file.read().split()

with open("Drawings.txt", "r") as file:
    hangman_drawings = file.read().split('\n\n')

left_attempts = len(hangman_drawings) - 1
selected_word = random.choice(words).upper()
hidden_word = ["_"] * len(selected_word)
guessed_letters = []


def print_colored_text(text):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
    for c in text:
        color = random.choice(colors)
        print(f"{color}{c}\033[0m", end="")


def print_game_state():
    os.system('cls')  # if Windows else 'clear'
    print()
    print_colored_text(hangman_drawings[left_attempts])
    print()
    print('💜' * left_attempts + '💔' * (len(hangman_drawings) - left_attempts - 1))
    print('\033[36m')
    print("".join(hidden_word))
    print("\033[97m")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print("\033[35m", end="")
    print(f"Attempts left: {left_attempts}")
    print("\033[0m")


def get_user_input():
    while True:
        user_input = input("Guess a letter: ").upper()
        if len(user_input) == 1 and user_input.isalpha() and user_input not in guessed_letters:
            return user_input
        else:
            print("Invalid input or letter already guessed. Try again.")


while left_attempts > 0 and "_" in hidden_word:
    print_game_state()
    letter = get_user_input()
    guessed_letters.append(letter)

    if letter not in selected_word:
        left_attempts -= 1
    else:
        for i, char in enumerate(selected_word):
            if char == letter:
                hidden_word[i] = letter

print_game_state()
if "_" not in hidden_word:
    print("\033[92mCongratulations! You've guessed the word!\033[0m")
else:
    print("\033[91mGame Over! The word was:", selected_word, "\033[0m")

