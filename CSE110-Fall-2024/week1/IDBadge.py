print('please enter the info to create id card')

first_name = input('first name: ')

last_name = input('last name: ') 

email_address = input('email address: ')

phone_number = input('phone number: ')

job_title = input('job title: ')

id_number = input('ID number: ')

print ('The ID card is:')
print (last_name.upper()+(', ')+first_name.capitalize()) 
print (job_title.capitalize())
print('ID#: ' + id_number)
print()
print(email_address)
print(phone_number)