# created by Matthew Rosenthal
# I added a list of words to pull from for the secret word and pulls the word based of the random number generated
# it also tells you the length of the word to the user and I created a loop so the user can play again if they want to
from random import randint
print('')
print ('Welcome to The Word Guess Game\n')
print ('Rules:')
print('''
1. An underscore _ indicates that the letter was not present in the secret word.
2. A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.
3. An uppercase letter indicates that the letter was present at that exact spot in the secret word. 
(In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)
''')

words=['dispersion','divination','calvary','golgotha','atonement','mormon','scriptures','christ','temple','ordinance','family','genealogy','alma','benjamin','nephi','faith','repentance']

def get_hint(secret_word, guess):
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
    i = randint(1,len(words))
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
    

word_puzzle()

def validate_yes_no(choice):
    choice = choice.lower()

    if choice == "yes":
        return True
    elif choice == "no":
        return False
    else:
        raise ValueError("Invalid input. Please enter either 'yes' or 'no'.")
    
while True:
    try:
        choice = validate_yes_no(input("Do you want to play again? (yes/no): "))

        if choice:
            word_puzzle()
        else:
            print('good bye')
            break
    except ValueError as e:
        print("Error:", e)
