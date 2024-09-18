
def fahrenheit_to_celsius(f):
   celsius = (f-32)*5/9
   return celsius

print ('This function converts Fahrenheit to Celsius')
F = float(input('Please enter the temperature in Fahrenheit: '))
temp = fahrenheit_to_celsius(F)
f_temp = f'{temp:.1f}'
print('The temperature in Celsius is: ', f_temp,' degrees.')