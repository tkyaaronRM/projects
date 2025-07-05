questions = ['Which countries are in Asia?',
             'Which countries are in ASEAN?',
             'Which countries speak Spanish?',
             'Which cities are in UK?']

options = [
    ['A. China',
     'B. Malaysia',
     'C. Taiwan',
     'D. Italy'],

    ['A. China',
     'B. Brunei',
     'C. Thailand',
     'D. Singapore'],

    ['A. Spain',
     'B. Peru',
     'C. France',
     'D. Mexico'],

    ['A. Liverpool',
     'B. Ansterdam',
     'C. Manchester',
     'D. Oxford']
]

ans = [
    ['1', '2', '3'],
    ['2', '3', '4'],
    ['1', '2', '4'],
    ['1', '3', '4']
]

score = 0
for i in range(4):
    print()
    print(questions[i])

    for j in range(4):
        print(options[i][j])

    user = input("Enter your choices: (use ', ' to separate your answers, not case sensitive. Use spaces aft commas!) ")
    userAns = user.split(',')

    for x in range(len(userAns)):
        if userAns[x].upper() in ans[i]:
            score += 10

print()
print(f'Your score is {str(score)}.')
