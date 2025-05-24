import pandas as pd
import matplotlib.pyplot as plt

steps = []
UV = []
calBurnt = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday']

colours = ['red', 'yellow', 'orange', 'purple', 'brown', 'green', 'blue']
plt.style.use('seaborn-v0_8')

print('Steps, Sun Exposure and Calorie Calculator')

for i in range(7):
    inputs1 = int(input(f'\nOn {days[i]}, how many steps? '))
    steps.append(inputs1)
    
    inputs2 = int(input('How many calories burnt? '))
    calBurnt.append(inputs2)

    inputs3 = int(input('UV index: '))
    UV.append(inputs3)

avgSteps = sum(steps) // 7
avgCalBurnt = sum(calBurnt) // 7
avgUV = sum(UV) // 7

data = {'DAYS': days,
        'STEPS': steps,
        'CALS BURNT': calBurnt,
        'UV': UV,
        'AVG STEPS': avgSteps,
        'AVG CALS BURNT': avgCalBurnt,
        'AVG UV': avgUV,
        }
dataFrame = pd.DataFrame(data)

if avgUV > 6:
    print('\nYou should exercise more in the morning or evening instead of the afternoon!')

if avgSteps < 500 or avgCalBurnt < 600:
    print('\nYou should exercise more regularly!')
    
print('\nSummary:')
print(dataFrame)

plt.bar(days, steps, color=colours)
plt.xticks(days, ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
plt.title('Steps')

plt.show()
