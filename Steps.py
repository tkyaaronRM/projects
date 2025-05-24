import matplotlib.pyplot as plt

""" Demo Program:

values = [5, 3, 2, 4, 3]
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Guavas']
colours = ['red', 'yellow', 'orange', 'purple', 'brown']

plt.bar(labels, values, color=colours)
plt.ylim(0, 12)
plt.xticks(labels, ('AP', 'BA', 'OR', 'GR', 'GV'))
plt.title('My Fruits')
plt.show()
"""

## Config

# Variables and constants
steps = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday']
less = []
colours = ['red', 'yellow', 'orange', 'purple', 'brown', 'green', 'blue']
fig, ax = plt.subplots()

# Matplotlib
plt.style.use('seaborn-v0_8')

for s in range(7):
    inputs = int(input(f'How many steps on {days[s]}?'))
    steps.append(inputs)

avg = sum(steps) // 7
print(f'\nYour average step(s) this week is {avg}')

if avg < 5000:
    print('You should try walking more to stay healthy!')

elif avg > 5000:
    print('Great job! Keep up the good work!')

for l in range(7):
    if steps[l] < 10000:
        less.append(days[l])

if len(less) == 0:
    print('Great Job! You walked more than 10K steps every day!')

else:
    print('\nThese are the days you walked less than 10K steps:')
    for x in range(len(less)):
        print(less[x])

plt.bar(days, steps, color=colours)
plt.xticks(days, ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
plt.title('Steps')

print('\nSummary:')
plt.show()
