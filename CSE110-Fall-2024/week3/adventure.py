#created by Matthew Rosenthal
# I created serval layers past the requirements I also had my wife try it out and had a friend from work look it over,
# I also created a function to handle the choice selection

print('')
print('You enter a dark room in an old house and pull out of your pocket a [FLASHLIGHT] or a [GLOW STICK].\n')


def choice(option1, option2):
    choice_1 = option1.upper()
    choice_2 = option2.upper()
    choice_made = ''
    while choice_made != choice_1 or choice_made != choice_2:   
        temp = input(f'What do you want to do? {choice_1} or {choice_2}: ')
        choice_made = temp.upper()
        if choice_made == choice_1:
            decision = 1
            return decision     
        elif choice_made == choice_2:
            decision = 2
            return decision
        else: print('Invalid Choice')


    
decision1 = choice('FLASHLIGHT','GLOW STICK')
#flashlight
if decision1 == 1:
    print('')
    print('''    You turn on the flashlight but it is dim because the batteries are dying
    but you can see some stairs that spiral going up too the floor [ABOVE] 
    you and also [BELOW] to what looks like they are going into the basement''')
    print('')
    decision2 = choice('ABOVE','BELOW')
    #above
    if decision2 == 1:
        print('')
        print('''    As you walk up the stairs you can smell the sent of old books
    and as you enter the room you see bookcases filled with books covering most of the walls
    except one with a fireplace with logs ready to be lit,
    you decide to [LIGHT] the fireplace or [EXPLORE] the room further''')
        print('')
        decision3 = choice('LIGHT','EXPLORE')
        #light
        if decision3 == 1:
            print('')
            print('''    You find a match and light the fireplace and see a comfy chair with a side table
                you decide to [SIT] in the chair or [LOOK] for a book to read. ''')
            decision4 = choice('SIT','LOOK')
            #sit
            if decision4 == 1:
                print('')
                print ('you fall asleep as you watch the fire slow burn and crackle. [THE END]')
                print('')
            #look
            elif decision4 == 2:
                print('')
                print('''You look over the books and find one to your liking and sit in the chair and read till dawn,
                    listening to the fire crackle as it burns while reading your book till dawn.[THE END]''')
                print('')
        #explore
        elif decision3 == 2:
            print('')
            print('''You find a passage to a room that has a bed in it and you here the sound of breathing
            softly coming from behind the bed.Do you [ENTER] the room or go [BACK]''')
            print('')
            decision4 = choice('ENTER','BACK')
            if decision4 == 1:
                print('')
                print('walk around the bed and find an old dog a sleep on a rug next to the bed\n')
            elif decision4 == 2:
                print('you go to the chair in the room and sit down and fall asleep listening to the sound of crickets outside.[THE END] ')
    #below
    elif decision2 == 2:
        print('')
        print('''As you walk down the stairs you see 3 different rooms one as you glance in,
        it looks like a kitchen and the other 2 look like bedrooms, you decide to go into the [KITCHEN] or one of the [BEDROOMS]\n''')
        
        decision3 = choice('KITCHEN','BEDROOMS')
        #kitchen
        if decision3 == 1:
            print('')
            print('''you trigger a laser from the future that vaporizes you.[THE END]\n''')
        #bedrooms
        elif decision3 == 2:
            print('')
            print(' You trigger a trap door and fall into a pit of lava.[THE END]\n')
#glow stick                   
elif decision1 == 2:
    print('')
    print('''You crack the glow stick and soft dim light comes off the glow stick and you notice something glowing on the wall
        that looks like a [SWITCH] and then you also notice a spiral [STAIR] case going to the floor above and below you\n''')
    decision2 = choice('SWITCH','STAIR')
    #switch
    if decision2 == 1:
        print('')
        print('''You enter a room with test tubes and other lab equipment and looks like something from the future.
            do you investigate the [LAB] further or [LEAVE] the room to the previous room\n''')
        decision3 = choice('LAB','LEAVE')
        #lab
        if decision3 == 1:
            print('')
            print('''You discover that it is in deed from the future and begin following the instructions for an experiment 
                and discover that they have the formula to an amazing chemical that lets you teleport.[THE END]\n ''')
        #leave
        elif decision3 == 2:
            print('')
            print(' You trip on the stairs and fall down them and hit your head and it knocks you unconscious. [THE END]\n')
        #up
    elif decision2 == 2:
        print('')
        print('You go to the stairs do you go [UP] or [DOWN]')
        decision3 = choice('UP','DOWN')
        if decision3 == 1:
                print('')
                print('''When you go upstairs you find a Library but it is hard to see with only a glow stick,
                    you can see a painting of a woman that seems to be reacting to the light from the glow stick, 
                    sitting on the mantle above a fireplace.The woman appears to pointing to a bookcase on the left side of the room.
                    the fireplace looks to have logs in it ready to be lit, do you go the the [BOOKCASE] or [LIGHT] the fireplace\n''')
                decision4 = choice('BOOKCASE','LIGHT')
                #bookcase
                if decision4 == 1:
                    print('')
                    print('''you step in front of the book case and see a strange glow on one of the books from the light from the glow stick
                        and as you pull on the book bookcase pops out off the wall and you can see it can swing like a door, you open in it
                        farther to see what is behind it and you find a Secret staircase to the Attic.Do you go up the [STAIRCASE] or [STAY]\n ''')
                    decision5 = choice('STAIRCASE','STAY')
                    #staircase to attic
                    if decision5 == 1:
                        print('')
                        print('''you go upstairs to find that you it filled with items from different times and you can make out an old rocking chair
                            with a table and photo albums next it. And then you sit in the rocking chair looking at the photo album till the wee hours of dawn.[THE END]\n''')
                    #stay
                    elif decision5 ==2:
                        print('You look around to find a book to read and as you pull the book off the shelf the bookcase fall over pinning you under it. [THE END]')
                elif decision4 ==2:
                            print('You look around the room after lighting the fireplace and find a book to your liking and sit in the chair sitting in the corner of the room and read the book till noon the next day.[THE END]\n')
                            print('')
        #down     
        elif decision3 == 2:
            print('')
            print('you hear some music thumping and see glowing stuff all over the walls. You realize it is a party and you join the fun.[THE END]\n')
    #stair                      
    
                    
    
