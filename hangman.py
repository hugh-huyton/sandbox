import string, random

words = 'cuffs cuing culls cults cumin cupel cupid curbs curds cures panel pangs panic pansy pants papas papal papaw paper parch pards pared pares paris parks parka parry parse parts parte party pasha salaam salads salami salary saline saliva sallow salmon salons saloon salted saluki salute salved salver salves salvia salvos samara sambas samoan sampan sample sancta sanded sander sandal sanest sanity sansei santas  scabby scaled scales scalar scalds scalps scamps scampi scants scanty scared scares bigamy bigger bights bigots bigwig bijoux bikers biking bikini bilged bilges bilked billed billet billow binary binder binges bingos biomes biopsy biotic biotas biotin bipeds birdie births bisect bishop bisque melodies melodeon meltable meltdown membrane mementos memories memorial memoriam memorize menacing menhaden meninges meniscal meniscus mentally menthols mentions mephitic mephitis merchant merciful mercuric meridian tenanting tendering tenderize tenements tenebrous tennessee tenseness tensility tentacles tentative tentmaker tenuously teriyakis termagant terminals terminate terracing terrapins terrarium terrazzos redeposits redescribe redesigned redevelops redigested redirected rediscover redissolve redistrict'

wordlist = words.split()


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# helper functions

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            guessed = False
            break
        else:
            guessed = True

    return guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    correct_letters = []  # used to store the correct letters
    guessed_string = ""  # the value that is returned
    # if a guessed letter is in the secret word, then store that letter in the correct_letters list
    for char in letters_guessed:
        if char in secret_word:
            correct_letters.append(char)

    # for each letter in the secret word, if it's been guessed, display it in the guessed_string, otherwise display "_ "
    for char in secret_word:
        if char in correct_letters:
            guessed_string += char
        else:
            guessed_string += "_ "

    return guessed_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # first get all available letters in lowercase
    letters = string.ascii_lowercase
    unguessed = ""
    # for each item in letters, check if it's been guessed; if not, added to unguessed variable
    for char in letters:
        if char not in letters_guessed:
            unguessed += char
    return unguessed


# create to check if user put in a correct input
# check how many warnings left
def check_warnings(warnings_remaining, user_guess, duplicate_guesses, display):
    warnings_remaining -= 1
    # different print statement depending on if user entered a nonvalid input or a repeat letter
    if not user_guess.isalpha():
        print('Oops! That is not a valid letter. You have ' + str(warnings_remaining) + ' warnings left: ' + display)
    elif user_guess in duplicate_guesses:
        print('Oops! You\'ve already guessed that letter. You have ' + str(
            warnings_remaining) + ' warnings left. ' + display)
    print('-----------------')
    return warnings_remaining


# check how many guesses are left
def check_guesses(guesses_remaining, user_guess, duplicate_guesses, display):
    guesses_remaining -= 1
    # different print statement depending on if user entered a nonvalid input or a repeat letter
    if not user_guess.isalpha():
        print("Oops! That is not a valid letter. You have no warnings left so you lose one guess. " + display)
    elif user_guess in duplicate_guesses:
        print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ' + display)
    else:
        print('Oops! That letter is not in my word: ' + display)
    print('-----------------')
    return guesses_remaining


def hangman(secret_word):
    letters_guessed = []
    duplicate_guesses = []  # used to track any duplicate_guesses
    guesses_remaining = 6
    warnings_remaining = 3
    # display to show the guessed string - intialize blank so letters that are guessed the first time (not repeat) are not considered repeats
    display = '_ ' * len(secret_word)
    # calculate the number of unique letters in the word
    unique_letters = ''
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters += letter

    print('Welcome to the game Hangman!')
    print("I'm thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print('You have ' + str(warnings_remaining) + ' warnings left.')
    print('-----------------')

    while True:
        letters_left = get_available_letters(letters_guessed)
        print('You have ' + str(guesses_remaining) + ' guesses left.')
        print('Available letters: ' + letters_left)

        # ask user for his input
        user_guess = (input('Please guess a letter: ')).lower()

        # check what the user entered
        if not user_guess.isalpha():
            # if user did not enter a letter - first reduce warnings; if no warnings, reduce guesses
            if warnings_remaining > 0:
                warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
            elif guesses_remaining > 1:
                guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
            else:
                print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
                break
        # below code runs if the user entered a valid letter
        else:
            # add the guess to the letters guessed
            if user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
            # checks if the user guessed all the correct letters
            game_over = is_word_guessed(secret_word, letters_guessed)

            # break out of the loop if game_over is true (all letters are guessed correctly)
            if game_over:
                display = get_guessed_word(secret_word, letters_guessed)
                print('Good guess: ' + display)
                print('-----------------')
                print('Congratulations, you won!')
                total_score = guesses_remaining * len(unique_letters)
                print('Your total score for this game is: ' + str(total_score))
                break
            # else check if the guess has already been guessed
            elif user_guess in duplicate_guesses:
                if warnings_remaining > 0:
                    warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
                elif guesses_remaining > 1:
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
                # else check if the guess is in the word; if true:
            elif (not (user_guess in duplicate_guesses)) and user_guess in secret_word:
                display = get_guessed_word(secret_word, letters_guessed)
                print('Good guess: ' + display)
                print('-----------------')
            # else check if guess is in the word; if false:
            elif user_guess not in secret_word:
                if user_guess in ['a', 'e', 'i', 'o', 'u'] and guesses_remaining > 1:
                    # minus 2 guesses if it's a vowel, but the check_guesses function also subtract one guess
                    guesses_remaining = guesses_remaining - 1
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
                elif guesses_remaining > 1:
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
                else:
                    print('Oops! That letter is not in my word: ' + display)
                    print('-----------------')
                    print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
                    break
        duplicate_guesses.append(user_guess)


secret_word = choose_word(wordlist)






