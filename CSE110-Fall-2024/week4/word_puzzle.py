# created by Matthew Rosenthal
# I added a list of words to pull from for the secret word and pulls the word based of the random number generated
# it also tells you the length of the word to the user and I created a loop so the user can play again if they want to
from random import randint


words=['dispersion','divination','calvary','golgotha','atonement','mormon','scriptures','christ','temple','ordinance','family','genealogy','alma','benjamin','nephi','faith','repentance']

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
    i= randint(1,len(words))
    secret_word = words[i]
    print(i)
    attempts = 0  

    print("Your hint is:", ' _ ' * len(secret_word),'\n')
    print(f'The word is {len(secret_word)} letters long.\n')

    while True:
        guess=input('What is your guess?: ').lower()

        if len(guess) != len(secret_word):
            print(f"Sorry, the guess must have the same number of letters as the secret word.\n")
            continue

        if guess == secret_word:
            attempts += 1
            print('')
            print('Congratulation you got the correct word \n')
            break

        else:
            print('')
            print('sorry your guess is not correct, Please try again.\n ')
            print('Your Hint: ',get_hint(secret_word,guess),'\n')
            attempts += 1

    print(f'It took you: {attempts} guesses')
play_again='yes'
while True:
    
    if play_again == 'yes':
        word_puzzle()
        choice=str(input(('Do you want to play again? (yes/no): ')))
        play_again=choice.lower
    elif play_again == 'no':
        secret_word='null'
        break
    elif choice != 'yes' or choice != 'no':
        print (('Not a valid input please try again'))
        choice=str(input(('Do you want to play again? (yes/no): ')))
        play_again=choice.lower
        continue