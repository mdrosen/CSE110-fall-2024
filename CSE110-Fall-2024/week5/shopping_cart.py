#created by Matthew Rosenthal



cart=[]
price=[]
def menu():
    choice=0
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
            cart.append(items)
            
            item_price=float(input('How much does it cost? :'))
            
            price.append(item_price)
            
        elif choice == 2:
            
            print(cart)
            print(price)
            
        elif choice == 3:
            print ('remove')
        elif choice == 4:
            subtotal=sum(price)
            print(f'Subtotal:$ {subtotal:.2f}')
            tax=3.3
            print('total')
        elif choice == 5:
            return
        else:
            print('not a valid choice')

menu()