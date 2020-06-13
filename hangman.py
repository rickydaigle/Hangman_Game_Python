#!/usr/bin/env python3

import wordlist

def get_word():
    word = wordlist.get_random_word()
    return word.upper()

def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    print("Word:", add_spaces(displayed_word), "  Guesses:", num_guesses, "  Wrong:", num_wrong, "  Tried:", add_spaces(guessed_letters))

def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()

        if guess == "" or len(guess) > 1:
            print("Invalid entry. " + "Please enter one and only one letter.")
            continue
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

def play_game():
    word = get_word()

    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 10 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess

        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remaining_letters == 0:
        print("Congratulations! You got it in", num_guesses, "guesses.")
    else:
        print("Sorry, you lost.")
        print("The word was:", word)

def main():
    print("Play the H A N G M A N game")
    while True:
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
