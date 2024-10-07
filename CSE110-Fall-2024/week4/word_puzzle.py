print ('Welcome to The Word Guess Game\n')
secret_word = 'scriptures'
num_letters=len(secret_word)

s_word_letters_list = list(secret_word)
print (num_letters)

hidden = ' _ ' 

guess_hint= [hidden] * num_letters 

guess_hint_dis=(''.join(guess_hint))   

print(f'Hint: {guess_hint_dis}\n')

guess=''
loop_count=0
while guess != secret_word:

    guess=input('What is your guess? ')
    word=guess.lower
    
    loop_count = loop_count + 1
    print(f'you have made {loop_count} guesses')
    
    
    
    
    
    if word == secret_word:
        print('')
        print('congratulation you got the word correctly\n')
    else:
        print('')
        print('sorry your guess is not correct, Please try again.\n ')