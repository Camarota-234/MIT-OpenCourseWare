# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
  
    for letter in secret_word:
        if letter in letters_guessed:
            print(letter + " ", end='')
        else:
            print("_ ", end='')

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter

    return available  


def hangman(secret_word):
    warnings = 3
    letters_guessed = ""
    guesses_remaining = 6

    print("\nWelcome to the game Hangman! \nI am thinking of a word that is " + str(len(secret_word)) + " letters long.\n You have 3 warnings left. ")
    get_guessed_word(secret_word, letters_guessed)

    while guesses_remaining > 0:
        
        print("You have " + str(guesses_remaining) + " guesses left. \nAvailable letters: " + get_available_letters(letters_guessed) + "\n")
        current_guess = input("Please guess a letter: ")
        
        if str.isalpha(current_guess) and current_guess not in letters_guessed:
            current_guess = str.lower(current_guess)
            letters_guessed += current_guess
        
        elif str.isalpha(current_guess) and current_guess in letters_guessed and warnings > 0:
          warnings -= 1
          print("Oops! You've already guessed that letter. You have " + str(warnings) + " warnings left:")       

        elif str.isalpha(current_guess) and current_guess in letters_guessed and warnings == 0:
          print("Oops! You've already guessed that letter. You have no warnings left:")
          guesses_remaining -= 1

        elif warnings > 0:
          warnings -= 1
          print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left:")
          
        elif warnings == 0:
          print("Oops! That is not a valid letter. You have no warnings left:")
          guesses_remaining -= 1

        if current_guess in secret_word:
            print("\nGood guess! :", end='') 
            get_guessed_word(secret_word, letters_guessed)
            print("\n\n--------------------------------------------------\n")

        else:
            print("\nOops! That letter is not in my word:", end='')
            get_guessed_word(secret_word, letters_guessed)
            print("\n\n--------------------------------------------------\n")
            guesses_remaining -= 1
      
        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_remaining * len(secret_word)
            print("Congratulations, you won! \nYour total score for this game is: " + str(total_score))
            

            return True
    print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
    return False



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = ("pepino")
    # secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
