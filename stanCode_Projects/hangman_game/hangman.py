"""
File: hangman.py
Name: Josephine
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This program will set a word, and the user can guess that word(one letter each turn).
    1. Turn the letter which gave by the user into uppercase letter.
    2. If the letter is in the word, the note will update. If not, the guessing chance will -1.
    3. Keep guessing until the chance becomes 0 or the user complete the whole word.
    """
    answer = random_word()
    guess = ''
    turns = N_TURNS
    # Print the '-' which = the amount of letters in the word.
    for i in range(len(answer)):
        guess += '-'
    # If the users do not get the correct answer and still have chances to guess, they can keep guessing.
    while N_TURNS >= 0 and guess != answer:
        print('The word looks like: ' + guess)
        print('You have ' + str(turns) + ' guess(es) left.')
        input_ch = input('Your guess: ')
        # When the users type in the wrong format, they should try until correct.
        while input_ch.isalpha() is False or len(input_ch) != 1:
            print('Illegal format.')
            input_ch = input('Your guess: ')
        input_ch = input_ch.upper()
        # If the user guess the correct letter.
        if answer.find(input_ch) != -1:
            guess2 = ''
            for j in range(len(answer)):
                if guess[j].isalpha():
                    guess2 += guess[j]
                elif answer[j] == input_ch:
                    guess2 += input_ch
                else:
                    guess2 += '-'
            guess = guess2
            print('You are correct!')
        # If the user guess the wrong letter.
        else:
            turns -= 1
            print('There is no ' + input_ch + "'s in the word.")
    # Print the result(win or lose).
    if guess == answer:
        print('You win!')
    else:
        print('You are completely hung :(')
    print('The word was: ' + answer)


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


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
