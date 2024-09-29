
percentage = float(input('Please enter your grade percentage: '))
#temp= (f{temp.:2f})
if percentage>= 90:
    letter = 'A'
    print(f'Your letter grade is : {letter}')
elif percentage>=80:
    letter = 'B'
    #print('Your letter grade is : B')
    print(f'Your letter grade is : {letter}') 
elif percentage>=70:
    letter = 'C'
    #print('Your letter grade is : C')
    print(f'Your letter grade is : {letter}') 
elif percentage>=60:
    letter = 'D'
    #print('Your letter grade is : D')
    print(f'Your letter grade is : {letter}')
elif percentage < 60:
    letter = 'F'
    #print('Your letter grade is : F')
    print(f'Your letter grade is : {letter}')
else:
    print('not a valid number')
    
if percentage > 70:
    print ('Pass')
else:
    print ('Fail')
    
