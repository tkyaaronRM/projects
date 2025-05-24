import pandas as pd

print('Caffeine Calculator')

tea = int(input('\nHow many cups of tea did you have today? '))
coffee = int(input('How many cups of coffee did you have today? '))
cola = int(input('How many cups of cola did you have today? '))
espresso = int(input('How many cups of espresso did you have today? '))
energyDrinks = int(input('How many cups of energy drinks did you have today? '))

total = (tea * 50) + (coffee * 100) + (cola * 40) + (energyDrinks * 80) + (espresso * 45)

print(f'\nCaffeine consumed today: {str(total)} mg')

data = {'DRINKS': ['Tea', 'Coffee', 'Cola', 'Espresso', 'Energy Drinks'],
        'AMOUNT OF SERVINGS': [tea, coffee, cola, espresso, energyDrinks],
        'CAFFEINE (mg)': [(tea * 50), (coffee * 100), (cola * 400), (energyDrinks * 80),
                          (espresso * 45)]}

dataFrame = pd.DataFrame(data)
print('\nSummary:')
print(dataFrame)

if total < 400:
    print('\nGood Job! Keep it up!')

else:
    print('\nYou are consuming too much caffeine')
