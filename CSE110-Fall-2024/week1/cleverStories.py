#created by: Matthew Rosenthal
# After 'family.' on line 19 I added the following sentence and had the user input a 2nd exclamation and a 4th verb.

#get input from the user
print('Please enter the follow words:')
adjective=input('adj:')
animal=input('animal:')
verb_1=input('verb:')
exclamation_1=input('exclamation:')
verb_2=input('verb:')
verb_3=input('verb:')
exclamation_2=input('exclamation:')
verb_4=input('verb:')

#output the story with the words entered from the user
print('The other day, I was really in trouble. It all started when I saw a very')
print(adjective+' '+animal+' '+ verb_1+' down the hallway.'+' '+exclamation_1.capitalize()+'! I yelled. But all')
print('I could think to do was to '+verb_2+' over and over. Miraculously,')
print('that caused it to stop, but not before it tried to '+verb_3)
print(' right in front of my family. Causing them to exclaim '+exclamation_2+ ' ,as they '+verb_4+' around the room to capture the '+animal+'.') 
