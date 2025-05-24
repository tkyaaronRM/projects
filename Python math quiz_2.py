import sys, os

questions = [
    'How many legs does an insect have?',
    'What special property does an Amphibian have?',
    'Which group of animals give birth to young alive?',
    'What special property does a Bird have?',
    'What is the atomic number for Oxygen?',
    'What do chloroplasts do?',
    'What special property does a mammal have?'
]

options = [
    ['1. 3',
     '2. 4',
     '3. 5',
     '4. 6'],

    ['1. Moist Skin',
     '2. Scales',
     '3. Fur',
     '4. Feathers'],

    ['1. Mammals',
     '2. Birds',
     '3. Reptiles',
     '4. Fish'],

    ['1. Moist Skin',
     '2. Scales',
     '3. Fur',
     '4. Feathers'],

    ['1. 6',
     '2. 7',
     '3. 8',
     '4. 9'],

    ['1. Make food',
     '2. Controls most activities in the cell',
     '3. Protects the cell from injuries',
     '4. Controls substances moving in and out of the cell'],

    ['1. Moist Skin',
     '2. Scales',
     '3. Fur',
     '4. Feathers']
]

ans = [4, 1, 1, 4, 3, 1, 3]
choices = [1, 2, 3, 4]

score = 0
start = True

while start:
    print()

    for i in range(7):
        
        flag = True
        while flag:
            print(f'Q{str(i + 1)}. {questions[i]}')
        
            for j in range(4):
                print('   ' + options[i][j])
            userAns = int(input('Ans: '))

            if userAns in choices:
                flag = False

            else:
                print('You can only input either 1, 2, 3 or 4.')
                os.system('clear')

        if userAns == ans[i]:
            print('Correct!')
            score += 1

        else:
            print('Incorrect!')
        print()

    if score == 7:
        print('Congradulations!')

    else:
        print(f'You got {str(score)} out of 5 questions correct.')

    stop = input('\nDo you want to try again? (Y/N)')
    if stop == 'Y':
        print('Thanks for playing!')
        sys.exit()

    elif stop == 'N':
        os.system('clear')
        continue

    else:
        print('Error')
        sys.exit()
