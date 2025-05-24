'''
Shopping App, by Aaron Tan

Usage:

1. Adds a new item into the shopping list
2. Displays the shopping list
3. Removes an item from the shopping list. When prompted, please enter an integer or the app will break!
4. Empties the shopping list (i.e. removes all items)
5. Exits the shopping app.

- I have yet to impliment ValueError handlings, so please enter the right data type when prompted

- You can just key in `Ctrl+C` or `Cmd+C` to exit the program

'''

import sys, os

## Variables
cart = []

## Functions

def displayCart():
    if len(cart) > 0:
        for i in range(len(cart)):
            print(f'Item {i+1}: {cart[i]}')
            
        input('\nPress enter to continue...')

    else:
        print('Shopping cart is empty!')
        input('\nPress enter to continue...')

def removeItem():
    if len(cart) > 0:
        choice2 = int(input(f'Which item to remove? (1-{len(cart)} '))

        try:
            del cart[choice2 - 1]

        except IndexError:
            print('\nInvalid Choice')

        input('\nPress enter to continue...')

    else:
        print('Shopping cart is empty!')
        input('\nPress enter to continue...')

## Main Code

try:
    while True:
        os.system('cls')
        
        print('Main Menu')
        print('--------------------------')
        print('1. Add a new item')
        print('2. Display shopping cart')
        print('3. Remove an item')
        print('4. Empty cart')
        print('5. Quit (or ^C)')
        print('--------------------------')
        print()
        choice = str(input('Enter your choice (1-4): '))

        if choice == '1':
            os.system('cls')
            itemToAdd = str(input('What do you want to add? '))
            cart.append(itemToAdd)

        if choice == '2':
            os.system('cls')
            displayCart()

        if choice == '3':
            os.system('cls')
            removeItem()

        if choice == '4':
            os.system('cls')
            cart = []

            print('\nCart emptied!')
            input('\nPress enter to continue...')
            
        if choice == '5':
            print('\nExiting program...')
            sys.exit()

        else:
            continue

except KeyboardInterrupt:
    print('\nExiting program...')
    sys.exit()
