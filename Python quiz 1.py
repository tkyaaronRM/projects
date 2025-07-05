import sys, os

questions = [
    'Which continent is Malaysia in?',
    'How many prefectures (都道府県-todōfuken) does Japan (日本-nihon) have?',
    'What is the capital of China (中国-Zhōng guó)',
    'How many oceans does Earth have?',
    'Which continent is Canada in'
]

options = [
    ['1. Asia',
     '2. Europe',
     '3. Africa',
     '4. South America'],

    ['1. 25',
     '2. 30',
     '3. 37',
     '4. 47'],

    ['1. Nánjīng 南京',
     '2. Shànghǎi 上海',
     '3. Hong Kong (香港-Xiāng gǎng)',
     '4. Běijīng 北京'],

    ['1. 2',
     '2. 3',
     '3. 5',
     '4. 1'],

    ['(1) South America',
     '(2) Australia',
     '(3) North America',
     '(4) Europe']
]

correctAnswers = [1, 4, 4, 3, 1]

score = 0
start = True

print('For every question, you must keyin the correct answer.\n')

while start:
    for i in range(5):
        print(f'Q{str(i + 1)}. {questions[i]}')

        for j in range(4):
            print(f'  {options[i][j]}')
        userAnswer = int(input('Ans: '))

        if userAnswer == correctAnswers[i]:
            score += 1
            print('Correct!')

        else:
            print('Incorrect!')
        print('\n')

    if score == 5:
        print('Congratulations! You got everything correct!')

    else:
        print(f'You got {str(score)} out of 5 questions correct.')

    stop = input('\nDo you want to try again? (Y/N) ')
    if stop == 'N':
        print('Thanks for playing!')
        sys.exit()

    elif stop == 'Y':
        os.system('clear')
        continue

    else:
        print('Error')
        sys.exit()
