#created by Matthew Rosenthal



print('You enter a dark room in an old house and pull out of your pocket a [FLASHLIGHT] or a [GLOW STICK].')

def choice('option1', 'option2'):

        choice_1 = 'option1.upper()'
        choice_2 = 'option2.upper()'
    
        choice_made=input('What do you want to do?: ')
        if choice_made == choice_1:
            decision=1
            return decision     
        elif choice_made == choice_2:
            decision=2
            return decision
        else: print('Invalid Choice')
        choice_made=input('What do you want to do?: ')

    
decision1=choice('FLASHLIGHT','GLOW STICK')
if decision1==1:
    print('You turn on the flashlight but it is dim because the batteries are dying but you can see some stairs that spiral going up too the floor [ABOVE] you and also [DOWN] to what looks like they are going into the basement')
    decision2=choice('ABOVE','BELOW')
    if decision2==1:
        print('As you walk up the stairs you can smell the sent of old books and as you enter the room you see bookcases filled with books covering most of the walls except one with a fireplace with logs ready to be lit, you decide to[LIGHT] the fireplace or [EXPLORE] the room further')
        decision3=choice('LIGHT','EXPLORE')
        if decision3==1:
            print('')
            decision4=choice('','')
        elif decision3==2:
            print('')
            decision4=choice('','')
    elif decision2==2:
        print('')
        decision3=choice('','')
        
elif decision1==2:
    print('You crack the glow stick and soft dim light comes off the glow stick and you notice something glowing on the wall that looks like a SWITCH and then you also notice a spiral STAIR case going to the floor above and below you ')
    decision2=choice('SWITCH','STAIRS')
    if decision2==1:
        print('')
        decision3=choice('','')
        if decision3==1:
            print('')
            decision4=choice('','')
        elif decision3==2:
            print('')
            decision4=choice('','')
    elif decision2==2:
            print('')
            decision3=choice('','')