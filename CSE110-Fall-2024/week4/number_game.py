import random


print('Welcome to the Number Guessing Game\n')
print('Please pick a number between 1-100\n')

while True:
    number = random.randint(1,100)
    #print(number)
    guess = 0
    run = 'yes'
    times = 0
    
    while guess != number:
        times += 1
        guess = input('what is your guess?: ')

        if guess.isdigit():
            
            guess = int(guess)

            if number == guess:
                print('Congratulations, you guessed the right number.\n')
                print((f'It took you {times} guesses\n'))

                run = input('Do you want to play again (yes/no): ').lower()
                
            elif guess < 1 or guess > 100:
                print ('your number is not in the range of available numbers\n')
            elif guess < number:
                print('Hint: The number is Higher.\n')

            elif guess > number:
                print('Hint: The number is Lower.\n')                

        else:
            print('Please enter a valid number')
            continue
    
    if run == 'no':
        break
    elif run =='yes':
        times = 0