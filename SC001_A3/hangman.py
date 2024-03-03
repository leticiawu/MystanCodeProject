"""
File: hangman.py
Name: Leticia
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the user has.
N_TURNS = 7


def main():
    """
    This program generates a random vocabulary,
    and the user guesses an alphabet. If the guessed
    alphabet is in the vocabulary, the program reveals its position(s).
    If not, the user lose one guess.(You have N_TURNS guesses.)
    The game ends when either all alphabets are guessed correctly (win)
    or when 7 guesses are used up (lose).
    """
    word = random_word()            # Generate a random word for the game
    display = "_" * len(word)       # Create a dashed representation matching the word's length
    wrong_guesses = N_TURNS         # Set initial wrong guesses to the maximum allowed (N_TURNS)
    console_hangman(wrong_guesses)
    print("The word looks like:", display)
    print("You have", N_TURNS, "wrong guesses left.")

    while wrong_guesses > 0:
        guess = input("Your guess: ").upper()

        if len(guess) != 1 or not guess.isalpha():  # Check if correct format
            one_more_time(guess)
            console_hangman(wrong_guesses)
        else:
            if guess in word:   # Check if the guessed letter (guess) is correct
                display = correct(guess, word, display)
                print("You are correct!")
                console_hangman(wrong_guesses)
                print("You have", wrong_guesses, "wrong guesses left.")
                print("The word looks like:", display)
            else:
                # Update n_turns
                wrong(guess, word)
                wrong_guesses -= 1
                print("There is no", guess, "'s word in the world.")
                console_hangman(wrong_guesses)  # visualise the wrong guesses with hangman figure
                print("The word looks like:", display)
                print("You have", wrong_guesses, "wrong guesses left.")

            # Check if to end the game
            if display == word:
                print("You win!!")
                print("The answer is:", word)
                break
    else:
        console_hangman(wrong_guesses)
    ending(wrong_guesses, word)


def correct(guess, word, display):
    ans = display
    for i in range(len(word)):
        ch = word[i]
        if guess == ch.upper():
            ans = ans[:i] + guess.upper() + ans[i + 1:]
    return ans


def wrong(guess, word):
    ans = ""
    for i in range(len(word)):
        ch = word[i]
        if guess != word[i]:
            ans += ch
    return ans


def one_more_time(guess):
    if len(guess) != 1 or not guess.isalpha():
        print("Illegal format.")


def console_hangman(wrong_guesses):
    """
    Display the hangman figure based on the number
    of incorrect guesses.

    Parameters: guess(int): The number of incorrect guesses remaining.

    Returns: None
    """
    if wrong_guesses == 7:
        print('========')
        print('|')
        print('|')
        print('|')
        print('|')
    elif wrong_guesses == 6:
        print('========')
        print('|   |')
        print('|')
        print('|')
        print('|')
    elif wrong_guesses == 5:
        print('========')
        print('|   |')
        print('|   O')
        print('|')
        print('|')
    elif wrong_guesses == 4:
        print('========')
        print('|   |')
        print('|   O')
        print('|   |')
        print('|')
    elif wrong_guesses == 3:
        print('========')
        print('|   |')
        print('|   O')
        print('| / |')
        print('|')
    elif wrong_guesses == 2:
        print('========')
        print('|   |')
        print('|   O')
        print('| / | \\')
        print('|')
    elif wrong_guesses == 1:
        print('========')
        print('|   |')
        print('|   O')
        print('| / | \\')
        print('|  /')
    else:
        print('========')
        print('|   |')
        print('|   O')
        print('| / | \\')
        print('|  / \\')


def ending(guess, word):
    """
    Shows when end of the game
    """
    if not guess == 0:
        print('')
        print('You win!!')
        print('')
        print('========')
        print('| Hurray')
        print('|   O')
        print('| \\ | /')
        print('|  / \\')
    else:
        print('You are completely hung :(')
    print('')
    print('The word was: ' + word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == "__main__":
    main()
