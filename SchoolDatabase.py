"""
A school database application

"""

## Variables and Initialisation

import sys, os

class Person:
    def __init__(self, name):
        self.name = name

    def description(self):
        return self.name

    def update(self):
        self.name = str(input('Enter his/her name: '))

class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def description(self):
        return 'Succesfully added teacher: ' + super().description() + ' ($' + str(self.salary)

    def update(self):
        choice = str(input('What do you want to update? '))
        print('---------------------------')
        print('1. Name')
        print('2. Salary')
        print('---------------------------')

        if choice == '1':
            super().update()

        elif choice == '2':
            self.salary = str(input('Enter his/her salary: (no units)'))

        else:
            print('Invalid')

class Student(Person):
    def __init__(self, name, ID):
        super().__init__(name)
        self.ID = ID

    def description(self):
        return 'Successfully added student: ' + super().description() + ' (ID: ' + str(self.ID)

    def update(self):
        print('---------------------------')
        print('1. Name')
        print('2. Student ID')
        print('---------------------------')
        choice = str(input('What do you want to update? '))

        if choice == '1':
            super().update()

        elif choice == '2':
            self.ID = str(input('Enter his/her student ID: '))

        else:
            print('Invalid')

def create(dataList, mode): ## 1: Teacher, 2: Student
    name = input('Enter his/her name: ')

    if mode == '1':
        ID = str(input('Enter his/her student ID: '))
        newRecord = Student(name, ID)

    elif mode == '2':
        salary = input('Enter his/her salary: (no units)')
        newRecord = Teacher(name, salary)

    else:
        print('Invalid')

    dataList.append(newRecord)

def read(dataList):
    if len(dataList) > 0:
        for records in dataList:
            print(records.description())

    else:
        print('No Record')

def update(dataList):
    if len(dataList) > 0:
        read(dataList)
        index = int(input('Which record to update? ')) - 1
        dataList[index].update()

    else:
        print('No Record')

def delete(dataList):
    if len(dataList) > 0:
        read(dataList)
        index = int(input('Which record do you want to delete? ')) - 1
        del dataList[index]

def menuB(dataList, mode, DBname):
    while True:
        os.system('cls')
        print('Main Menu')
        print('========================')
        print('1. Create a new record')
        print('2. View records')
        print('3. Update record')
        print('4. Delete record')
        print('5. Exit')
        print('========================')

        choice = str(input('\nEnter your choice: (1-5)'))

        if choice == '1':
            os.system('cls')
            create(dataList, mode)
            input('\nPress enter to continue...')

        elif choice == '2':
            os.system('cls')
            read(dataList)
            input('\nPress enter to continue...')

        elif choice == '3':
            os.system('cls')
            update(dataList)
            input('\nPress enter to continue...')

        elif choice == '4':
            os.system('cls')
            delete(dataList)
            input('\nPress enter to continue...')

        elif choice == '5':
            print('\nBye!')
            sys.exit()

        else:
            continue


## Main Code

teacherList = []
studentList = []

try:
    while True:
        os.system('cls')
        print('Databases')
        print('----------')
        print('1. Teacher')
        print('2. Student')
        print('3. Exit the program')
        print('----------')

        mode = input('\nWhich database do you want to access? ')

        if mode == '1':
            menuB(teacherList, mode, 'Teacher Database')

        elif mode == '2':
            menuB(studentList, mode, 'Student Database')

        elif mode == '3':
            print('\nBye!')
            sys.exit()

        else:
            continue

except KeyboardInterrupt:
    print('\nBye!')
