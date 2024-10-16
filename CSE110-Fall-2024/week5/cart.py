def menu():
    cart = []
    choice = 0
    while choice != 5:
        print('                            ')
        print('----------------------------')
        print('           Menu             ')
        print('----------------------------')
        print('1. Add new Item             ')
        print('2. Display contents of Cart ')
        print('3. Remove Item from Cart    ')
        print('4. Total                    ')
        print('5. Quit                     ')
        print('----------------------------')
        print('                            ')
        try:
            choice = int(input('What would you like to do?: '))
        except:
            print('Not a valid choice please enter a number between 1 - 5:')
            continue           
            #Add item to cart
        if choice == 1:
            
            items=str(input('Add to cart: '))
            item_price:.2 = float(input('How much does it cost?: '))
            quantity = int(input('How many?: '))
            if quantity >= 1:
                cart.append([items,item_price,quantity])
            else:
                return
        #Display contents of Cart
        elif choice == 2:
            for i, items in enumerate(cart): 
                print(f'{i+1}. {items[0]} - ${items[1]:.2f} Qty-{items[2]}')
            
        elif choice == 3:
            if cart:
                print("The contents of the shopping cart are:")
                for i, items in enumerate(cart, 1):
                    print(f"{i}. {items[0]} Qty-{items[2]}")
                items = int(input('Select the number of item you would like to remove? '))
                
                if 1 <= items <= len(cart):
                    qty = int(input('How many do you want to remove?: '))
                    if qty >= 1:
                        del cart[quantity - qty]
                        print(f'{qty} removed.')
                    else:
                        break
                else:
                    print('Sorry, that is not a valid item number.')
            else:
                print('The shopping cart is empty.')
            
        elif choice == 4:
            subtotal = sum(items[1] * items[2] for items in cart)
            print(f'Subtotal  $ {subtotal:.2f}')
            tax=.3
            print(f'Tax          {tax}%')
            total = subtotal + (subtotal * tax)
            print(f'Total     $ {total:.2f}')
            
        elif choice == 5:
            return
    

menu()