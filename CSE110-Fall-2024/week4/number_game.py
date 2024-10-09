import random
print('Welcome to the Number Guessing Game\n')
print('Please pick a number between 1-100\n')
while True:
    number=random.randint(1,100)
    #print(number)
    guess=0
    run='yes'
    times=0
    while guess != number:
        guess=int(input('what is your guess?: '))
        times += 1
        if guess == number:
            print('Congratulations, you guessed the right number.')
            print((f'It took you {times} guesses'))
            
            run=input('Do you want to play again (yes/no): ').lower()

        elif guess < 1 or guess > 100:
            print ('your number is not in the range of available numbers')

        elif guess < number:
            print('Hint: The number is Higher.')

        elif guess > number:
            print('Hint: The number is Lower.')
    if run == 'no':
        break
    elif run=='yes':
        times=0