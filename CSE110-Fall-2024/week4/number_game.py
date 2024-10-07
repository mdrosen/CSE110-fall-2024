import random


number=random.randint(1,10)
#print(number)
guess=0

while guess != number:
    guess=int(input('what is your guess?: '))

    if guess == number:
        print('Congraulations, you guessed the right number.')

    elif guess < 1 or guess > 10:
        print ('your number is not in the range of avalible numbers')

    elif guess < number:
        print('Hint: The number is Higher.')

    elif guess > number:
        print('Hint: The number is Lower.')
