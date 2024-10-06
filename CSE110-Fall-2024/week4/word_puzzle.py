
secret_word = 'scriptures'
num_letters=len(secret_word)


guess_hint=('')

print ('Welcome to The Word Guess Game\n')
while guess != secret_word:
    print ('')
    guess=input('What is your guess?')