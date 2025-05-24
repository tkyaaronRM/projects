def calculateMass(BMI, height):
    return BMI * height * height

import sys

height   = float(input("What's your desired BMI? "))
BMI      = float(input('What is your height? '))
currMass = float(input('What is you current mass? '))

newMass = calculateMass(BMI, height)

if newMass < currMass:
    print(f'\nYou need to lose {currMass - newMass} kg.')
    sys.exit()

elif newMass > currMass:
    print(f'\nYou need to gain {newMass - currMass} kg.')
    sys.exit()

elif newMass == currMass:
    print(f'\nYou don not have to do anything!')
    sys.exit()

