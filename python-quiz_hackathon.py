import sys
import time

questions = [
    # Multiple Choice Questions
    ['Which country is in ASEAN?',
     'Which language is in Japanese?',
     'Which mountain range does Mount Everest belong to?',
     'Which MRT station is in the Thomson-East Coast line?',
     'What is the official language of Uzbekistan?' ],

    # Multiple Response Questions
    ['What languages do the people in the Xinjiang Uyghur Autonomous Region شىنجاڭ ئۇيغۇر ئاپتونوم رايونى speak?',
     'The Mekong River 湄公河 မဲခေါင်မြစ် Sông Mê Kông ទន្លេមេគង្គ flows through a few contries. What are they?'],

    # Short Answer Questions
    ['What is the full form of MRT',
     'What is the full form of ASEAN']

]

options = [
    [
        ['(1) Malaysia',
         '(2) India',
         '(3) China',
         '(4) Sri Lanka'],

        ['(1) こんにちは',
         '(2) 你好',
         '(3) Bonjour',
         '(4) Xin chào'],

        ['(1) Andes',
         '(2) Tianshan',
         '(3) Himalayas',
         '(4) Kunlun'],

        ['(1) Gardens by the Bay',
         '(2) Bayfront',
         '(3) Bishan',
         '(4) Downtown'],

        ['(1) Chinese',
         '(2) Uyghur ئۇيغۇر',
         '(3) Uzbek',
         '(4) Arabic']
    ],

    [
        ['(1) Arabic',
         '(2) Uyghur ئۇيغۇر',
         '(3) Chinese 中文',
         '(4) English'],

        ['(1) Cambodia',
         '(2) Malaysia',
         '(3) China 中国',
         '(4) Vietnam']
    ]
]

answers = [['1', '1', '3', '1', '3'],
           [['2', '3', '4'], ['1', '3', '4']],
           ['mass rapid Transit', 'association of southeast asian nations']]

try:
    print('Welcome to Hard Quiz™!')
    print('Press Ctrl+C to quit.')
    print('----------------------')
    print()

    score = 0
    name = input('Your name: ')
    email = ''
    phoneNum = 0

    while '@' not in email:
        email = input('Enter your email: ')

    flag = True
    while flag:
        try:
            phoneNum = int(input('\nEnter your phone number, no spaces! (country code + phone number): '))
            flag = False

        except ValueError:
            print('Numbers only!')

    input('\nPress enter to start the quiz...')
    print()
    print()

    for a in range(len(questions[0])):
        print()
        print(questions[0][a])

        for i in range(4):
            print(f'  {options[0][a][i]}')

        userAns = input('Ans: ')
        print('Drumroll...')
        time.sleep(2)

        if userAns == answers[0][i]:
            print('Correct!')
            score += 1

        else:
            print('Incorrect!')

    for b in range(len(questions[1])):
        print()
        print(questions[1][b])

        for j in range(4):
            print(f'  {options[0][b][j]}')

        user = input("Enter your choices: (use ', ' to separate your answers. Use spaces aft commas!) ")
        userAns1 = user.split(', ')
        print('Drumroll...')
        time.sleep(2)

        for x in range(len(userAns1)):
            if userAns1 in answers[1][x]:
                print('Correct!')
                score += 2

    for c in range(len(questions[2])):
        print()
        print(questions[2][c])
        userAns2 = input('Ans: ')

        if isinstance(answers[2][c], list):
            if userAns2.lower() in answers[c]:
                print('\nCorrect!')
                score += 3

            else:
                print('\nIncorrect!')

        else:
            if userAn2.lower() == answers[c]:
                print('\nCorrect!')
                score += 3

            else:
                print('\nIncorrect!')

    print('\nYour score is {score}')
    if score == 15:
        print('Congrats!')

except KeyboardInterrupt:
    print('Thanks for playing!')
    sys.exit()
