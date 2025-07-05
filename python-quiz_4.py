import sys, os

def showTitle():
    print()
    print('Short Answers Quiz')
    print('Press Ctrl+C to quit')
    print('------------------')

questions =[
    'What is the full form of MRT?',
    'Name a food that came from Italy'
]

answers = [
    'mass rapid transit',
    ['spaghetti', 'pasta', 'pizza']
]

try:
    score = 0

    showTitle()
    print('     Welcome!')
    name = input('Please enter your name: ')
    email = ''
    phoneNumber = 0

    while '@' not in email:
        email = input('Please enter your email: ')


    flag = True
    while flag:
        try:
            phoneNumber = int(input('\nEnter your phone number, no spaces! (country code + phone number): '))
            flag = False
            
        except ValueError:
            print('Numbers only!')
            print()

        os.system('clear')

    input('Press Enter to start the quiz...')
    os.system('clear')

    showTitle()
    for i in range(len(questions)):
        print(f'\nQuestion {str(i+1)} out of {str(len(questions))}')
        print(questions[i])
        userAnswer = input('Enter your answer: ')

        if isinstance(answers[i], list):
            if userAnswer.lower() in answers[i]:
                print('\nCorrect!')
                score += 1

            else:
                print('\nIncorrect!')

        else:
            if userAnswer.lower() == answers[i]:
                print('\nCorrect!')
                score += 1

            else:
                print('\nIncorrect!')

    os.system('clear')
    if score == len(questions):
        print('\nYou got everything correct!')
        sys.exit()

    else:
        print(f'\nYou got {score} out of {len(questions)} correct.')
        
except KeyboardInterrupt:
    print('\nThanks for playing!')
    sys.exit()
