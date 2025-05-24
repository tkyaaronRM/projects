def calculateBMI(mass, height):
    return mass / (height * height)

print('BMI calculator')
print('Note: This BMI calculator ONLY GIVES YOU AN ESTIMATION!')
print()

name   = input('What is your name? > ')
mass   = float(input('What is your mass? (please enter w/o units) > '))
height = float(input('What is your height? (please enter w/o units) > '))

BMI = calculateBMI(mass, height)
print(f'\nHi {name}, your BMI (Body Mass Index) is {str(BMI)}.')

if BMI < 18.5:
    print('You are underweight! Please eat more')

elif BMI > 18.5 and BMI < 25:
    print('You are healthy! Keep it up!')

elif BMI > 25 and BMI < 30:
    print('You are overweight! Please eat less and exercise!')

else:
    print('You are severely overweight!!!')
