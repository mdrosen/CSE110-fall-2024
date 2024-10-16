#created by Matthew Rosenthal

#cart = {}

def returnSum(cart):

    price = []
    for i in cart:
        price.append(cart[i])
    total = sum(price)
    return total

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
        choice= int(input('What would you like to do?: '))
        if choice == 1:
            
            items=input('Add to cart: ')
            item_price:.2 = float(input('How much does it cost?: '))
            pair=[(items , item_price)]
            cart=cart.append(pair)
            
            
        elif choice == 2:
            for index, pair in (cart): 
                print(index, pair)
            
        elif choice == 3:
            for index, pair in enumerate(cart): 
                print(index, pair) 
            items=input('What item do you want to remove?: ')
            del (cart[items])
            
        elif choice == 4:
            for items in cart:
                print(items,' $',cart[items])
            print('--------------------------')
            subtotal = returnSum(cart)
            print(f'Subtotal: $ {subtotal:.2f}')
            tax = 0.3
            print(f'Tax:        {tax} %')
            total = subtotal + (subtotal * tax)
            print(f'Total:    $ {total:.2f}')
            
        elif choice == 5:
            return
        else:
            print('not a valid choice')

menu()