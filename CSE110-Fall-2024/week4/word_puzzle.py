

def get_hint(secret_word, guess):
    """Generates a hint for the user's guess based on the secret word."""
    hint = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper()) 
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())  
        else:
            hint.append(' _ ')  
    return ''.join(hint)

def word_puzzle():
    print('')
    print ('Welcome to The Word Guess Game\n')
    secret_word = 'scriptures'
    trys=0  

    print("Your hint is:", ' _ ' * len(secret_word),'\n')
 
    while True:
        guess=input('What is your guess?: ').lower()

        if len(guess) != len(secret_word):
            print(f"Sorry, the guess must have the same number of letters as the secret word.\n")
            continue

        if guess == secret_word:
            trys += 1
            print('')
            print('Congratulation you got the correct word \n')
            break

        else:
            print('')
            print('sorry your guess is not correct, Please try again.\n ')
            print('Your Hint: ',get_hint(secret_word,guess),'\n')

    print(f'It took you: {trys} guesses')

word_puzzle()