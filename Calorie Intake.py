import sys

calorieIntake = []


desiredIntake = int(input('What is your desired calorie intake for the next few days in total? '))
days = int(input('How many days do you want to input? '))
print()

for x in range(days):
    newIntake = int(input(f'Calorie intake for day {x + 1}: '))
    calorieIntake.append(newIntake)

print('\nHere are the calorie intakes for the past seven days:')
for i in range(days):
    print(f'Day {i + 1}: {str(calorieIntake[i])}')

totCalorie = sum(calorieIntake)
avCalorie = totCalorie // days

print(f'\nYour total calorie intake is {totCalorie}.')
print(f'Your average calorie intake is approx. {avCalorie}.')

if desiredIntake == totCalorie:
    print("You've reached your goal!")

elif desiredIntake < totCalorie:
    print('You are eating less. Eat more!')

elif desiredIntake > totCalorie:
    print('You are eating too much! Eat less!')
