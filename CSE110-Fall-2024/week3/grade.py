temp = float(input('Please enter your grade percentage: '))
percentage = round(temp, 2)

grade_value = ""
if percentage%10>=7:
    grade_value='+'
elif percentage%10 >= 3:
    grade_value='-'
else:
    grade_value=''

if percentage >= 90:
    #print('Your letter grade is : A')
    if percentage > 97:
        letter =  "A"
    else: 
        letter = f'A{grade_value}'

elif percentage >= 80:
    letter = f'B{grade_value}'
    #print('Your letter grade is : B')

elif percentage >= 70:
    letter = f'C{grade_value}'
    #print('Your letter grade is : C')

elif percentage >= 60:
    letter = f'D{grade_value}'
    #print('Your letter grade is : D')

elif percentage < 60:
    letter = 'F'
    #print('Your letter grade is : F')

else:
    print('not a valid number')

print(f'Your letter grade is : {letter}') 
if percentage > 70:
    print ('Pass')
else:
    print ('Fail')