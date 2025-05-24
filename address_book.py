import sys, os
import pickle

contacts = [[], []]

def loadContacts():
    try:
        with open("contacts.pkl", "rb") as file:
            contacts = pickle.load(file)

    except (FileNotFoundError, EOFError):
        contacts = [[], []]

    return contacts

def saveContacts(contacts):
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)

contacts = loadContacts()

while True:
    os.system('cls')

    print('An interactive address book')
    print()
    print('---------------------------')
    print('1. Create a contact')
    print('2. Update a contact')
    print('3. Delete a contact')
    print('4. Display all contacts')
    print('5. Exit Programme')
    print('---------------------------')
    choice = input('Choose an option (1-5): ')

    if choice == '1':
        os.system('cls')

        name = input('Enter his/her/your name: ')
        print('Enter phone number (Form: 00[international dialing code][phone number]')
        phoneNumber = input('>> ')

        contacts[0].append(name)
        contacts[1].append(phoneNumber)

        saveContacts(contacts)

        input('\nPress enter to continue...')

    if choice == '2':
        os.system('cls')
        name = input('Whose contact to update: ')
        phoneNumber = input('Enter new phone number (same form): ')

        index = 0

        for i in range(len(contacts[0])):
            index = contacts[0].index(contacts[0][i])

        contacts[1][index] = phoneNumber

        saveContacts(contacts)

        input('\nPhone number successfully updated! Press enter to continue...')

    if choice == '3':
        os.system('cls')

        name = input('Whose contact to delete: ')

        index = 0

        for i in range(len(contacts[0])):
            index = contacts[0].index(contacts[0][i])

        del contacts[1][index]

        saveContacts(contacts)

        input('\nPress enter to continue...')

    if choice == '4':
        os.system('cls')

        for i in range(len(contacts[0])):
            print(f'{contacts[0][i]}: {contacts[1][i]}')

        input('\nPress enter to continue...')

    if choice == '5':
        sys.exit()