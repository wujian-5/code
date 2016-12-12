# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(' ')
    print(len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


wordlist = loadWords()
secretWord = chooseWord(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    result = True
    for l in secretWord:
        if l not in lettersGuessed:
            result = False
    return result


def getGuessedWord(secretWord, lettersGuessed):
    result = ''
    for l in secretWord:
        if l in lettersGuessed:
            result = result + l
        else:
            result = result + '_ '
    return result


def getAvailableLetters(lettersGuessed):
    result = string.ascii_lowercase
    for l in lettersGuessed:
        result = result.replace(l, '')
    return result


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    number = len(secretWord)
    print('I am thinking of a word that is ' + str(number) + ' letters long.')
    lettersGuessed = []
    mistakesMade = 0
    while mistakesMade < 8:
        n = 8 - mistakesMade
        print('------------')
        print('You have ' + str(n) + ' guesses left')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ').lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " +
                  getGuessedWord(secretWord, lettersGuessed))
            continue
        else:
            lettersGuessed.append(letter)
            if letter in secretWord:
                print('Good guess: ' + getGuessedWord(
                    secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(
                    secretWord, lettersGuessed))
                mistakesMade += 1
                continue
        if isWordGuessed(secretWord, lettersGuessed) is True:
            print('------------')
            print('Congratulations, you won!')
            break
    if isWordGuessed(secretWord, lettersGuessed) is False:
        print('------------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord)


hangman(secretWord)
