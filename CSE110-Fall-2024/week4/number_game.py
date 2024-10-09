import random
while True:
    number=random.randint(1,10)
    print(number)
    guess=0
    run='yes'
    while guess != number:
        guess=int(input('what is your guess?: '))

        if guess == number:
            print('Congratulations, you guessed the right number.')
            run=input('Do you want to play again (yes/no): ').lower()

        elif guess < 1 or guess > 10:
            print ('your number is not in the range of available numbers')

        elif guess < number:
            print('Hint: The number is Higher.')

        elif guess > number:
            print('Hint: The number is Lower.')
    if run == 'no':
        break
    