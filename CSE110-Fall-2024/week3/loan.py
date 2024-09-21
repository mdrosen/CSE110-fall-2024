
print('Please enter a value between 1 - 10 for the following Questions:')
while True:
    try:
        size=int(input('How large is the loan? '))
        if 1 <= size <= 10:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    try:
        credit=int(input('How good is your credit history? '))
        if 1 <= credit <= 10:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
        
while True:
    try:
        income=int(input('How high is your income? '))
        if 1 <= income <= 10:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    try:
        down=int(input('How large is your down payment? '))
        if 1 <= down <= 10:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


if size >= 5:
    if credit>=7:
        if income>=7:
            print('yes')
    elif credit>=7 or income>=7:
        if down>=5:
            print('yes')
        else: print('no')
else:
    if credit<4:
        print ('no')
    elif income>=7 or down>=7:
        print('yes')
    elif income>=4 and down>=4:
        print ('yes')
    else: print ('no')

