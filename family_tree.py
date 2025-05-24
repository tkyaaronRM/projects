### Classes, variables, libraries

import os, sys

parents = []
children = []

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def showName(self):
        return self.firstName
    
class Parent(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.children = []

    def addChild(self, Child):
        self.children.append(Child)

    def removeChild(self, Child):
        self.children.remove(Child)
    
class Child(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.parents = []

    def addParent(self, Parent):
        self.parents.append(Parent)

    def removeChild(self, Child):
        self.parents.remove(Parent)

### Main

while True:
    os.system('cls')

    print('An interactive Family Database')
    print()
    print('Please choose an option: (1-7)')
    print('-----------------------------')
    print('1. Add parent')
    print('2. Add Child')
    print()
    print('3. Remove parent')
    print('4. Remove child')
    print()
    print('5. Show parents')
    print('6. Show children')
    print()
    print('7. Add parent to child')
    print('8. Add child to parent')
    print()
    print('9. Remove child from parent')
    print('10. Remove parent from child')
    print()
    print('11. Exit programme')
    print('-----------------------------')
    print()
    choice = input('>> ')

    if choice == '1':
        os.system('cls')
        parentFirst = input("New parent's first name: ")
        parentLast = input("New parent's last name: ")

        parents.append(Parent(parentFirst, parentLast))

        input('New parent added! Press enter to continue...')

    if choice == '2':
        os.system('cls')
        childFirst = input("New child's first name: ")
        childLast = input("New child's last name: ")

        children.append(Parent(childFirst, childLast))

        input('New child added! Press enter to continue...')

    if choice == '3':
        os.system('cls')
        parentFirst = input("Parent's first name: ")

        for i in parents:
            if Parent.showName(i) == parentFirst:
                parents.remove(i)
                break

        input('Parent removed! Press enter to continue...')

    if choice == '4':
        os.system('cls')
        childFirst = input("Child's first name: ")

        for i in children:
            if Child.showName(i) == childFirst:
                children.remove(i)
                break

        input('Child removed! Press enter to continue...')

    if choice == '5':
        os.system('cls')

        for i in parents:
            print(Parent.showName(i))

        print()
        input('Press enter to continue...')

    if choice == '6':
        os.system('cls')

        for i in children:
            print(Child.showName(i))

        print()
        input('Press enter to continue...')

    if choice == '7':
        os.system('cls')
        selectedChild = ''
        selectedParent = ''

        newParentFirst = input("New parent's first name: ")
        childFirst = input("Child's first name: ")

        try:
            for i in children:
                if Child.showName(i) == childFirst:
                    selectedChild = i
                    break

            for i in parents:
                if Parent.showName(i) == newParentFirst:
                    selectedParent = i
                    break

            Parent.addChild(selectedParent, selectedChild)

        except:
            print()
            print('Child/parent does not exist!')
            input('Press enter to continue...')

    if choice == '8':
        os.system('cls')
        selectedChild = ''
        selectedParent = ''

        newChildFirst = input("New child's first name: ")
        parentFirst = input("Parent's first name: ")

        try:
            for i in parents:
                if Parent.showName(i) == parentFirst:
                    selectedParent = i
                    break

            for i in children:
                if Child.showName(i) == newChildFirst:
                    selectedChild = i
                    break

            Parent.addChild(selectedParent, selectedChild)

        except:
            print()
            print('Child/parent does not exist!')
            input('Press enter to continue...')

    if choice == '9':
        os.system('cls')
        selectedChild = ''
        selectedParent = ''

        childFirst = input("Child to remove (enter first name): ")
        parentFirst = input("Parent's first name: ")

        try:
            for i in parents:
                if Parent.showName(i) == parentFirst:
                    selectedParent = i
                    break

            for i in children:
                if Child.showName(i) == childFirst:
                    selectedChild = i
                    break

            Parent.removeChild(selectedParent, selectedChild)
        
        except:
            print()
            print('Child/parent does not exist!')
            input('Press enter to continue...')

    if choice == '10':
        os.system('cls')
        selectedChild = ''
        selectedParent = ''

        childFirst = input("Child's first name: ")
        parentFirst = input("Parent to remove (enter parent's first name)")

        try:
            for i in children:
                if Child.showName(i) == childFirst:
                    selectedChild = i
                    break

            for i in parents:
                if Parent.showName(i) == parentFirst:
                    selectedParent = i
                    break

            Child.removeParent(selectedchild, selectedParent)

        except:
            print()
            print('Child/parent does not exist!')
            input('Press enter to continue...')

    if choice == '11':
        sys.exit()